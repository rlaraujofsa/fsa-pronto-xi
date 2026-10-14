import argparse
import csv
import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import InvalidElementStateException

from checkpoint import CheckPoint
from pronto import Inventory

load_dotenv()

def main():
    def check_csv_extension(file_path):
        # Check if the file ends with .csv (case-insensitive)
        if not file_path.lower().endswith(".csv"):
            raise argparse.ArgumentTypeError("File must have a .csv extension")
        return file_path

    # Read params
    parser = argparse.ArgumentParser(
        description="Script with explicit key-value arguments"
    )

    # Define individual key-value pairs
    parser.add_argument(
        "--company", type=str, default="FSU", help="Database host address"
    )
    parser.add_argument(
        "--data",
        type=check_csv_extension,
        required=True,
        help="Data filepath i.e. c:\\data.csv",
    )

    # Parse arguments
    args = parser.parse_args()

    # Exit if data file doesn't exist
    if not os.path.exists(args.data):
        print(f"\033[91mError: file '{args.data}' not found.")
        print("\033[0m")
        return

    # Access values directly via attributes
    print(f"Connecting to Pronto company {args.company}")
    print(f"Data file {args.data}")

    options = webdriver.ChromeOptions()
    wd = webdriver.Chrome(options=options)
    wd.get(os.getenv("PRONTO_URL"))
    wd.implicitly_wait(0.5)
    print(f"Starting Chrome browser. Page: {wd.title}")

    inventory = Inventory(wd, args.company)
    # TODO: Move to Server (Local) environment - or Cloud Secrets
    inventory.login(os.getenv("PRONTO_USERNAME"), os.getenv("PRONTO_PASSWORD"))
    inventory.access_maintain_inventory_section()

    checkpoint = CheckPoint()
    start_row = checkpoint.get_last_processed_row()
    print(f"Starting process. Last processed row was: {start_row}")

    with open(args.data, mode="r", newline="", encoding="utf-8-sig") as file:
        csv_reader = csv.DictReader(file)

        code_column = (
            "Item Code" if "FSA Code" not in csv_reader.fieldnames else "FSA Code"
        )

        for current_row, dirty_row in enumerate(csv_reader, start=1):
            # clean the row by stripping [\xa0] characters from the values
            row = {
                key: value.replace("\xa0", " ").strip()
                for key, value in dirty_row.items()
            }
            # Skip rows that have already been processed
            if current_row <= start_row:
                continue
            time.sleep(1)
            print(f"Row: {current_row}")
            attempts = 1
            while attempts <= int(os.getenv("PRONTO_MAX_ATTEMPTS")):
                try:
                    if code_column == "Item Code":
                        inventory.update_item_descriptions(row)
                    else:
                        inventory.insert_item(row)
                    break
                except InvalidElementStateException as ex:
                    print(
                        f"Processing Item Code: {row[code_column]} failed... Attempt {attempts} out of {os.getenv('PRONTO_MAX_ATTEMPTS')}"
                    )
                    attempts += 1
            # TODO: Write failed results in a file
            if attempts > int(os.getenv("PRONTO_MAX_ATTEMPTS")):
                print(
                    "\033[91m##############################################################"
                )
                print("######################### W A R N I N G!######################")
                print(
                    f"Process manually Item Code: {row[code_column]} - Row: {current_row}"
                )
                print("##############################################################")
                print("\033[0m")
            checkpoint.update_checkpoint(current_row)

    print("\033[92mCONGRATS! Process finished successfully :)")
    print("\033[0m")

    checkpoint.update_checkpoint(0)

    inventory.logout()

    wd.quit()


if __name__ == "__main__":
    main()
