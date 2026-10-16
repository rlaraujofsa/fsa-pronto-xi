import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class Pronto:
    """
    This class represents the Pronto Environment
    """

    def __init__(self, wd: WebDriver):
        self.wd = wd
        wd.maximize_window()
        self.selectors = {
            "login-username": (By.ID, "login-username"),
            "login-password": (By.ID, "login-password"),
            "login-button": (By.ID, "login-button"),
            "right-top-menu": (By.CSS_SELECTOR, "div#header-user-menu"),
            "logout-button": (By.CSS_SELECTOR, "li#um-logout"),
            "logout-confirm-button": (By.CSS_SELECTOR, "button[name=' &Yes']"),
        }
        self.wait = WebDriverWait(self.wd, 10)

    def login(self, username, password) -> None:
        username_input = self.wd.find_element(*self.selectors["login-username"])
        password_input = self.wd.find_element(*self.selectors["login-password"])
        login_button = self.wd.find_element(*self.selectors["login-button"])

        username_input.clear()
        username_input.send_keys(username)

        password_input.clear
        password_input.send_keys(password)
        login_button.click()

    def logout(self) -> None:
        right_top_menu = self.wait.until(
            EC.element_to_be_clickable(self.selectors["right-top-menu"])
        )
        right_top_menu.click()

        logout_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["logout-button"])
        )
        logout_button.click()

        logout_confirm_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["logout-confirm-button"])
        )
        logout_confirm_button.click()

    def is_element_clickable(self, locator, timeout=3):
        try:
            WebDriverWait(self.wd, timeout).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False


class Inventory(Pronto):
    """
    This class represents the Pronto Environment

    """

    # Constructor
    def __init__(self, wd: WebDriver, company) -> None:
        super().__init__(wd)
        self.wd = wd

        # selectors
        self.selectors = self.selectors | {
            # Inventory Maintenance Section
            "company-name-div": (
                By.CSS_SELECTOR,
                "li.pro-toolbar-item div#sidenav-company-name",
            ),
            "company-button": (
                By.CSS_SELECTOR,
                f"ul.company-list li[data-company='{company}'] > button",
            ),  #  > button.text-icon-option
            "inventory-button": (By.ID, "&Inventory"),
            "maintain-inventory-button": (By.ID, "&Maintain Inventory"),
            "inventory-maintenance-button": (By.ID, "&Inventory Maintenance/Enquiry"),
            "sidenav-home-div": (By.ID, "sidenav-home"),
            "find-button": (By.NAME, "&Find"),
            "correct-button": (By.NAME, "&Correct"),
            "entry-button": (By.NAME, "&Entry"),
            "ok-button": (By.NAME, "OK"),
            "cancel-button": (By.NAME, "Cancel"),
            "pack-quantity-modal-error": (
                By.CSS_SELECTOR,
                "div.field-placement button[name='OK']",
            ),
            "card-dialog": (By.ID, "card-dialog"),
            "item-code-already-exists-close-button": (
                By.CSS_SELECTOR,
                "div.runtime-dialog button[id='modal-close']",
            ),
            "yes-button": (By.NAME, "&Yes"),
            # Item Section
            "item-code-input": (By.NAME, "stock-code"),
            "description-1-input": (By.NAME, "stk-description"),
            "description-2-input": (By.NAME, "stk-desc-line-2"),
            "description-3-input": (By.NAME, "stk-desc-line-3"),
            # Hierarchy section
            "group-input": (By.NAME, "stock-group"),
            # Item Type section
            "item-type-input": (By.NAME, "stk-stock-status"),
            "condition-input": (By.NAME, "stk-condition-code"),
            "abc-class-input": (By.NAME, "stk-abc-class"),
            "process-requirement-input": (By.NAME, "stk-issue-control-code"),
            "warranty-input": (By.NAME, "stk-warranty-type-flag"),
            "cyclic-code-input": (By.NAME, "stk-cyclic-code"),
            "movement-type-input": (By.NAME, "stk-movement-code"),
            "shelf-life-input": (By.NAME, "stk-shelf-life-days"),
            "stock-user-input": (By.NAME, "x:21,y:21"),
            "sales-type-input": (By.NAME, "stk-sales-type-code"),
            "user-group-input": (By.NAME, "x:21,y:23"),
            "storage-type-input": (By.NAME, "stk-storage-type-flag"),
            "keep-by-serial-nos-input": (By.NAME, "stk-serialized-flag"),
            "sort-code-input": (By.NAME, "stk-sort-analysis-code"),
            "brand-input": (By.NAME, "stk-brand"),
            # "brand-desc-input": (By.NAME, "x:21,y:28"),
            # Item Dimensions section
            "unit-description-input": (By.NAME, "stk-unit-desc"),
            "alternative-unit-description-input": (By.NAME, "stk-alt-unit-desc"),
            "conversion-factor-input": (By.NAME, "stk-conversion-factor"),
            "pack-description-input": (By.NAME, "stk-pack-desc"),
            "pack-quantity-input": (By.NAME, "stk-pack-qty"),
            "pack-cubic-size-input": (By.NAME, "stk-pack-cubic-size"),
            "pack-weight-input": (By.NAME, "stk-pack-weight"),
            "import-tariff-input": (By.NAME, "stk-import-tariff-code"),
            # Item Costs section
            "excise-qty-input": (By.NAME, "stk-exise-qty"),
            # Planning and Control section
            "reorder-policy-input": (By.NAME, "stk-reorder-policy"),
            "planning-policy-input": (By.NAME, "stk-reorder-review"),
            "buyer-planner-input": (By.NAME, "stk-reorder-buyer"),
            "innovation-level-input": (By.NAME, "stk-origin-flag"),
            "origin-source-input": (By.NAME, "stk-origin-source"),
            "price-protection-input": (By.NAME, "stk-price-protection"),
            "allocation-code-input": (By.NAME, "stk-allocation-code"),
        }

        # TODO: Set default values in the dictionary
        self.columns = {
            "Item Code",
            "Description 1",
            "Description 2",
            "Description 3",
            "Group",
            "Item Type",
            "Condition",
            "ABC Class",
            "Process Requirement",
            "Warranty",
            "Cyclic code",
            "Movement Type",
            "Shelf Life",
            "Stock User",
            "Sales Type",
            "User Group",
            "Storage Type",
            "Keep by Serial Nos",
            "Sort Code",
            "Brand",
            "Unit Description",
            "Alternative Unit Description",
            "Conversion Factor",
            "Pack Description",
            "Pack Quantity",
            "Pack Cubic Size",
            "Pack Weight",
            "Import Tariff",
            "Excise Qty",
            "Reorder Policy",
            "Planning Policy",
            "Buyer/Planner",
            "Innovation Level",
            "Origin Source",
            "Price Protection",
            "Allocation Code",
        }

    # updates item properties
    def __update_item_property(self, item_property, item_property_value) -> None:
        item_property_key = item_property.lower().replace(" ", "-")
        item_property_input = self.wait.until(
            EC.element_to_be_clickable(self.selectors[item_property_key + "-input"])
        )
        item_property_input.send_keys(item_property_value)

    def __next_element(self, times) -> None:
        for i in range(0, times):
            ActionChains(self.wd).send_keys(Keys.ENTER).perform()
            time.sleep(0.2)

    # Access maintain inventory section
    def access_maintain_inventory_section(self) -> None:
        time.sleep(2)
        company_name_div = self.wait.until(
            EC.element_to_be_clickable(self.selectors["company-name-div"])
        )
        company_name_div.click()

        time.sleep(1)

        company_button = self.wait.until(EC.element_to_be_clickable(self.selectors["company-button"]))
        company_button.click()        

        sidenav_home_div = self.wait.until(
            EC.element_to_be_clickable(self.selectors["sidenav-home-div"])
        )
        sidenav_home_div.click()

        time.sleep(1)

        inventory_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["inventory-button"])
        )
        inventory_button.click()

        time.sleep(1)

        maintain_inventory_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["maintain-inventory-button"])
        )
        maintain_inventory_button.click()

        inventory_maintenance_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["inventory-maintenance-button"])
        )
        inventory_maintenance_button.click()

    # Update item descriptions
    def update_item_descriptions(self, row) -> None:
        print(
            "-------------------------------------------------------------------------------"
        )
        print("Updating descriptions on: " + row["Item Code"])

        find_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["find-button"])
        )
        find_button.click()

        ActionChains(self.wd).send_keys(Keys.ESCAPE).perform()

        find_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["find-button"])
        )
        find_button.click()

        time.sleep(1)

        stock_code_input = self.wait.until(
            EC.element_to_be_clickable(self.selectors["item-code-input"])
        )
        stock_code_input.clear()
        stock_code_input.send_keys(row["Item Code"] + Keys.ENTER)

        correct_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["correct-button"])
        )
        correct_button.click()

        new_description_1_input = self.wait.until(
            EC.element_to_be_clickable(self.selectors["description-1-input"])
        )
        new_description_1_input.clear()
        new_description_1_input.send_keys(row["New Description1"])

        new_description_2_input = self.wait.until(
            EC.element_to_be_clickable(self.selectors["description-2-input"])
        )
        new_description_2_input.click()
        new_description_2_input = self.wait.until(
            EC.element_to_be_clickable(self.selectors["description-2-input"])
        )
        new_description_2_input.clear()
        new_description_2_input.send_keys(row["New Description2"])

        new_description_3_input = self.wait.until(
            EC.element_to_be_clickable(self.selectors["description-3-input"])
        )
        new_description_3_input.click()
        new_description_3_input = self.wait.until(
            EC.element_to_be_clickable(self.selectors["description-3-input"])
        )
        if row["New Description3"]:
            new_description_3_input.send_keys(row["New Description3"])
            print(f"Sending Keys: {row['New Description3']}")
        else:
            new_description_3_input.send_keys(Keys.CONTROL + "a")
            new_description_3_input.send_keys(Keys.DELETE)
            print(f"Clearing Up: {row['New Description3']}")

        ok_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["ok-button"])
        )
        ok_button.click()

        # Modal: Pack Quantity must be 1 if Pack and Unit Descriptions are the same.
        if self.is_element_clickable(self.selectors["pack-quantity-modal-error"], 1):
            print("The element is ready to be clicked!")

            ok_error_button = self.wait.until(
                EC.element_to_be_clickable(self.selectors["pack-quantity-modal-error"])
            )
            ok_error_button.click()

            ok_button = self.wait.until(
                EC.element_to_be_clickable(self.selectors["ok-button"])
            )
            ok_button.click()

    # Inserts a new item
    def insert_item(self, row) -> None:
        print(
            "-------------------------------------------------------------------------------"
        )
        print("Inserting new item: " + row["FSA Code"])

        entry_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["entry-button"])
        )
        entry_button.click()

        time.sleep(0.4)
        ActionChains(self.wd).send_keys(row["FSA Code"] + Keys.ENTER).perform()
        time.sleep(0.4)

        # Modal: Item Code already exists
        if self.is_element_clickable(self.selectors["card-dialog"], 1):
            print("This item code already exists!")

            close_button = self.wait.until(
                EC.element_to_be_clickable(
                    self.selectors["item-code-already-exists-close-button"]
                )
            )
            close_button.click()

            ActionChains(self.wd).send_keys(Keys.ESCAPE).perform()

            if self.is_element_clickable(self.selectors["card-dialog"], 1):
                yes_button = self.wait.until(
                    EC.element_to_be_clickable(self.selectors["yes-button"])
                )
                yes_button.click()

            return

        # Item section
        ActionChains(self.wd).send_keys(row["FSA Description 1"] + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(row["FSA Description 2"] + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(row["FSA Description 3"] + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(Keys.ENTER).perform()

        # Hierarchy section
        ActionChains(self.wd).send_keys(row["Group"] + Keys.ENTER).perform()

        # Item Type section
        self.__next_element(14)

        ActionChains(self.wd).send_keys(row["Brand"] + Keys.ENTER).perform()

        # Modal: Brand does not exist
        if self.is_element_clickable(self.selectors["card-dialog"], 1):
            print("This Brand does not exist! Please add it first before adding the item.")
            exit

        # Item Dimensions section
        ActionChains(self.wd).send_keys(row["UOM"] + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(row["Pack"] + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(row["Pack Qty"] + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(row["Buy Price"] + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(row["Tarrif"] + Keys.ENTER).perform()

        self.__next_element(12)

        time.sleep(0.5)

        # Supplier screen
        # Supplier Details section
        ActionChains(self.wd).send_keys(row["Supplier"] + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(row["Supplier Code"] + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(
            row["Supplier Description"] + Keys.ENTER
        ).perform()
        ActionChains(self.wd).send_keys(row["Supp Priority"] + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(Keys.ENTER).perform()

        # Pack Details section
        ActionChains(self.wd).send_keys(
            row["Pack2"] + Keys.ENTER
        ).perform()
        ActionChains(self.wd).send_keys("1" + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(row["Pack Qty2"] + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(Keys.ENTER).perform()

        #Shipping Details section
        ActionChains(self.wd).send_keys(row["EOQ"] + Keys.ENTER).perform()
        self.__next_element(7)

        # Price Details section
        # Details section
        ActionChains(self.wd).send_keys(row["Buy Price"] + Keys.ENTER).perform()
        ActionChains(self.wd).send_keys(Keys.ENTER).perform()

        cancel_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["cancel-button"])
        )
        cancel_button.click()

        if self.is_element_clickable(self.selectors["card-dialog"], 1):
            yes_button = self.wait.until(
                EC.element_to_be_clickable(self.selectors["yes-button"])
            )
            yes_button.click()

        time.sleep(0.5)

        self.__next_element(4)
        # Pricing Details section
        for i in range(0, 5):
            ActionChains(self.wd).send_keys(
                f"{float(row['STD']):.2f}" + Keys.ENTER
            ).perform()
            if i < 4:
                ActionChains(self.wd).send_keys(Keys.ENTER).perform()

        ActionChains(self.wd).send_keys(
            f"{float(row['Retail']):.2f}" + Keys.ENTER
        ).perform()

        self.__next_element(3)

        cancel_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["cancel-button"])
        )
        cancel_button.click()

        # Warehouse screen
        # Warehouse details section
        self.__next_element(2)
        # TODO: Do not hardcode default bin location, at least put it in a config file
        ActionChains(self.wd).send_keys("ZZ" + Keys.ENTER).perform()

        self.__next_element(10)

        time.sleep(0.5)

        cancel_button = self.wait.until(
            EC.element_to_be_clickable(self.selectors["cancel-button"])
        )
        cancel_button.click()

        time.sleep(0.5)
        ActionChains(self.wd).send_keys(Keys.ESCAPE).perform()
        time.sleep(0.5)
        ActionChains(self.wd).send_keys(Keys.ESCAPE).perform()
        time.sleep(0.5)

    def old_stuff(self):
        pass
        # Inserts a new item
        # def insert_item(self, row) -> None:
        #     print("-------------------------------------------------------------------------------")
        #     print("Inserting new item: " + row['Item Code'])

        #     entry_button = self.wait.until(EC.element_to_be_clickable(self.selectors["entry-button"]))
        #     entry_button.click()

        #     time.sleep(0.8)

        #     # Modal: Item Code already exists
        #     if self.is_element_clickable(self.selectors["card-dialog"], 1):
        #         print("This item code already exists!")

        #         close_button = self.wait.until(EC.element_to_be_clickable(self.selectors["item-code-already-exists-close-button"]))
        #         close_button.click()

        #         ActionChains(self.wd).send_keys(Keys.ESCAPE).perform()

        #         if self.is_element_clickable(self.selectors["card-dialog"], 1):
        #             yes_button = self.wait.until(EC.element_to_be_clickable(self.selectors["yes-button"]))
        #             yes_button.click()

        #         return

        #     for item_property in self.columns:
        #         item_property_value = row[item_property]
        #         self.__update_item_property(item_property, item_property_value)
        #         time.sleep(0.5)

        #     ok_button = self.wait.until(EC.element_to_be_clickable(self.selectors["ok-button"]))
        #     ok_button.click()

        #     print("-------------------------------------------------------------------------------")

        # item_code_input = self.wait.until(EC.element_to_be_clickable(self.selectors["item-code-input"]))
        # item_code_input.send_keys(row['Item Code'] + Keys.ENTER)

        # new_description_1_input = self.wait.until(EC.element_to_be_clickable(self.selectors["description-1-input"]))
        # new_description_1_input.send_keys(row['New Description1'])

        # new_description_2_input = self.wait.until(EC.element_to_be_clickable(self.selectors["description-2-input"]))
        # new_description_2_input.send_keys(row['New Description2'])

        # new_description_3_input = self.wait.until(EC.element_to_be_clickable(self.selectors["description-3-input"]))
        # new_description_3_input.send_keys(row['New Description3'])

        # # Hierarchy Section
        # stock_group_input = self.wait.until(EC.element_to_be_clickable(self.selectors["group-input"]))
        # stock_group_input.send_keys(row['Group'])

        # # Item Type Section
        # item_type_input = self.wait.until(EC.element_to_be_clickable(self.selectors["item-type-input"]))
        # item_type_input.send_keys(row['Item Type'])

        # condition_input = self.wait.until(EC.element_to_be_clickable(self.selectors["condition-input"]))
        # condition_input.send_keys(row['Condition'])

        # abc_class_input = self.wait.until(EC.element_to_be_clickable(self.selectors["abc-class-input"]))
        # abc_class_input.send_keys(row['ABC Class'])

        # process_requirement_input = self.wait.until(EC.element_to_be_clickable(self.selectors["process-requirement-input"]))
        # process_requirement_input.send_keys(row['Process Requirement'])

        # warranty_input = self.wait.until(EC.element_to_be_clickable(self.selectors["warranty-input"]))
        # warranty_input.send_keys(row['Warranty'])

        # cyclic_code_input = self.wait.until(EC.element_to_be_clickable(self.selectors["cyclic-code-input"]))
        # cyclic_code_input.send_keys(row['Cyclic code'])

        # movement_type_input = self.wait.until(EC.element_to_be_clickable(self.selectors["movement-type-input"]))
        # movement_type_input.send_keys(row['Movement Type'])

        # shelf_life_input = self.wait.until(EC.element_to_be_clickable(self.selectors["shelf-life-input"]))
        # shelf_life_input.send_keys(row['Shelf Life'])

        # stock_user_input = self.wait.until(EC.element_to_be_clickable(self.selectors["stock-user-input"]))
        # stock_user_input.send_keys(row['Stock User'])

        # sales_type_input = self.wait.until(EC.element_to_be_clickable(self.selectors["sales-type-input"]))
        # sales_type_input.send_keys(row['Sales Type'])

        # user_group_input = self.wait.until(EC.element_to_be_clickable(self.selectors["user-group-input"]))
        # user_group_input.send_keys(row['User Group'])

        # storage_type_input = self.wait.until(EC.element_to_be_clickable(self.selectors["storage-type-input"]))
        # storage_type_input.send_keys(row['Storage Type'])

        # keep_by_serial_no_input = self.wait.until(EC.element_to_be_clickable(self.selectors["serialized-flag-input"]))
        # keep_by_serial_no_input.send_keys(row['Keep by Serial Nos'])

        # sort_code_input = self.wait.until(EC.element_to_be_clickable(self.selectors["sort-code-input"]))
        # sort_code_input.send_keys(row['Sort Code'])

        # brand_input = self.wait.until(EC.element_to_be_clickable(self.selectors["brand-input"]))
        # brand_input.send_keys(row['Brand'])

        # brand_desc_input = self.wait.until(EC.element_to_be_clickable(self.selectors["brand-desc-input"]))
        # brand_desc_input.send_keys(row['Brand Desc'])

        # # Item Dimensions Section
        # unit_description_input = self.wait.until(EC.element_to_be_clickable(self.selectors["unit-description-input"]))
        # unit_description_input.send_keys(row['Unit Description'])

        # unit_description_alt_input = self.wait.until(EC.element_to_be_clickable(self.selectors["unit-description-alt-input"]))
        # unit_description_alt_input.send_keys(row['Unit Description Alternative'])

        # conversion_factor_input = self.wait.until(EC.element_to_be_clickable(self.selectors["conversion-factor-input"]))
        # conversion_factor_input.send_keys(row['Conversion Factor'])

        # pack_description_input = self.wait.until(EC.element_to_be_clickable(self.selectors["pack-description-input"]))
        # pack_description_input.send_keys(row['Pack Description'])

        # pack_quantity_input = self.wait.until(EC.element_to_be_clickable(self.selectors["pack-quantity-input"]))
        # pack_quantity_input.send_keys(row['Pack Quantity'])

        # pack_cubic_size_input = self.wait.until(EC.element_to_be_clickable(self.selectors["pack-cubic-size-input"]))
        # pack_cubic_size_input.send_keys(row['Pack Cubic Size'])

        # pack_weight_input = self.wait.until(EC.element_to_be_clickable(self.selectors["pack-weight-input"]))
        # pack_weight_input.send_keys(row['Pack Weight'])

        # import_tariff_input = self.wait.until(EC.element_to_be_clickable(self.selectors["import-tariff-input"]))
        # import_tariff_input.send_keys(row['Import Tariff'])

        # # Item Costs Section
        # excise_qty_input = self.wait.until(EC.element_to_be_clickable(self.selectors["excise-qty-input"]))
        # excise_qty_input.send_keys(row['Excise Qty'])

        # # Planning and Control Section
        # reorder_policy_input = self.wait.until(EC.element_to_be_clickable(self.selectors["reorder-policy-input"]))
        # reorder_policy_input.send_keys(row['Reorder Policy'])

        # planning_policy_input = self.wait.until(EC.element_to_be_clickable(self.selectors["planning-policy-input"]))
        # planning_policy_input.send_keys(row['Planning Policy'])

        # reorder_policy_input = self.wait.until(EC.element_to_be_clickable(self.selectors["reorder-policy-input"]))
        # reorder_policy_input.send_keys(row['Reorder Policy'])

        # planning_policy_input = self.wait.until(EC.element_to_be_clickable(self.selectors["planning-policy-input"]))
        # planning_policy_input.send_keys(row['Planning Policy'])

        # buyer_planner_input = self.wait.until(EC.element_to_be_clickable(self.selectors["buyer-planner-input"]))
        # buyer_planner_input.send_keys(row['Buyer/Planner'])

        # innovation_level_input = self.wait.until(EC.element_to_be_clickable(self.selectors["innovation-level-input"]))
        # innovation_level_input.send_keys(row['Innovation Level'])

        # origin_source_input = self.wait.until(EC.element_to_be_clickable(self.selectors["origin-source-input"]))
        # origin_source_input.send_keys(row['Origin Source'])

        # price_protection_input = self.wait.until(EC.element_to_be_clickable(self.selectors["price-protection-input"]))
        # price_protection_input.send_keys(row['Price Protection'])

        # allocation_code_input = self.wait.until(EC.element_to_be_clickable(self.selectors["allocation-code-input"]))
        # allocation_code_input.send_keys(row['Allocation Code'])
        
