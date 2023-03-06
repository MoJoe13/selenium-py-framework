import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    ELEMENTS = "//div[@class='category-cards']//div[1]//div[1]//div[1]"
    TEXT_BOX_PAGE = "//span[normalize-space()='Text Box']"
    CHECKBOX = "//div[@class='element-list collapse show']//li[@id='item-1']"

    def __init__(self, driver):
        self.driver = driver

    # Methods for getting the appropriate pages
    def get_elements_page(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ELEMENTS)

    def click_on_elements(self):
        self.get_elements_page().click()

    def get_text_box_page(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.TEXT_BOX_PAGE)

    def click_on_text_box_page(self):
        self.get_text_box_page().click()

    def navigate_to_text_box_page(self):
        self.click_on_elements()
        self.click_on_text_box_page()

    def get_checkbox_page(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX)

    def click_on_checkbox(self):
        self.get_checkbox_page().click()

    def navigate_to_checkbox_page(self):
        self.click_on_elements()
        self.click_on_checkbox()

    def page_scroll(self):
        page_length = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight); var pageLength = document.body.scrollHeight")
        match = False
        while (match == False):
            last_count = page_length
            time.sleep(3)
            page_length = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); var pageLength = document.body.scrollHeight")

            if last_count == page_length:
                match = True



    def wait_for_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        clickable_element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return clickable_element

    def find_element_on_page(self, locator_type, locator):
        element = self.driver.find_element(locator_type, locator)
        return element
