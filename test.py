import argparse
import config
import csv
import pronto
import time


def test():
    # Read params
    parser = argparse.ArgumentParser(
        description="Script with explicit key-value arguments"
    )

    # Define individual key-value pairs
    parser.add_argument(
        "--company", type=str, default="FSU", help="Database host address"
    )
    parser.add_argument(
        "--data", type=str, required=True, help="Data filepath i.e. c:\\data.csv"
    )

    # Parse arguments
    args = parser.parse_args()

    # Access values directly via attributes
    print(f"\033[91mConnecting to Pronto company {args.company}")
    print(f"\033[92mProcessing file {args.data}")
    print("\033[0m")


if __name__ == "__main__":
    test()
