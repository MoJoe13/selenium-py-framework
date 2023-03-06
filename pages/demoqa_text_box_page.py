import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class DemoqaTextBoxPage(BaseDriver):

    full_name = "Milos Djordjevic"
    email = "mdjordje@test.com"
    address = "1428 Elm Street"
    perm_address = "Nowhere Street"

    # Text Field Locators
    TEXT_BOX_PAGE_SUBMIT_BTN = "//button[@id='submit']"
    NAME_FIELD = "//input[@id='userName']"
    EMAIL_FIELD = "//input[@id='userEmail']"
    ADDRESS_FIELD = "//textarea[@id='currentAddress']"
    PERM_ADDRESS_FIELD = "//textarea[@id='permanentAddress']"

    # Submit Result Locators
    NAME_TXT = "//p[@id='name']"
    EMAIL_TXT = "//p[@id='email']"
    CADDRESS_TXT = "//p[@id='currentAddress']"
    PADDRESS_TXT = "//p[@id='permanentAddress']"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Methods for getting appropriate text fields

    def get_name_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.NAME_FIELD)

    def get_email_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.EMAIL_FIELD)

    def get_address_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ADDRESS_FIELD)

    def get_perm_address_field(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.PERM_ADDRESS_FIELD)


    # Methods for entering test data text in the fields

    def enter_full_name(self, full_name):
        self.get_name_field().send_keys(self.full_name)
        time.sleep(1)

    def enter_email(self, email):
        self.get_email_field().send_keys(self.email)
        time.sleep(1)

    def enter_address(self, address):
        self.get_address_field().send_keys(self.address)
        time.sleep(1)

    def enter_perm_address(self, perm_address):
        self.get_perm_address_field().send_keys(self.perm_address)
        time.sleep(1)

    def click_on_submit(self):
        dtb_submit_btn = self.wait_for_element_to_be_clickable(By.XPATH, self.TEXT_BOX_PAGE_SUBMIT_BTN)
        dtb_submit_btn.click()
        time.sleep(1.5)


    # Method for veryfing the text input

    def test_verify_input(self):
        fname_info = self.find_element_on_page(By.XPATH, self.NAME_TXT).text
        email_info = self.find_element_on_page(By.XPATH, self.EMAIL_TXT).text
        caddress_info = self.find_element_on_page(By.XPATH, self.CADDRESS_TXT).text
        paddress_info = self.find_element_on_page(By.XPATH, self.PADDRESS_TXT).text

        assert fname_info == f"Name:{self.full_name}"
        assert email_info == f"Email:{self.email}"
        assert caddress_info == f"Current Address :{self.address}"
        assert paddress_info == f"Permananet Address :{self.perm_address}"
