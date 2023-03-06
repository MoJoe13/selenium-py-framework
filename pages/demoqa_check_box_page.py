from base.base_driver import BaseDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class DemoqaCheckBoxPage(BaseDriver):

    # These are locator constants (find a way to externalize them)
    # Expand buttons
    EXPAND_ALL_BTN = "//button[@title='Expand all']//*[name()='svg']"
    COLLAPSE_ALL_BTN = "//button[@title='Collapse all']//*[name()='svg']"

    # Toggle buttons
    TOGGLE_HOME = "//body/div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[" \
                  "@class='row']/div[@class='col-12 mt-4 col-md-6']/div[@class='check-box-tree-wrapper']/div[" \
                  "@id='tree-node']/ol/li[@class='rct-node rct-node-parent rct-node-expanded']/span[" \
                  "@class='rct-text']/button[1]//*[name()='svg']//*[name()='path' and contains(@d,'M7.41 7.84')]"

    TOGGLE_DESKTOP = "//body/div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[" \
                     "@class='row']/div[@class='col-12 mt-4 col-md-6']/div[@class='check-box-tree-wrapper']/div[" \
                     "@id='tree-node']/ol/li[@class='rct-node rct-node-parent rct-node-expanded']/ol/li[1]/span[" \
                     "1]/button[1]//*[name()='svg']//*[name()='path' and contains(@d,'M7.41 7.84')]"

    TOGGLE_DOCUMENTS = "//body/div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[" \
                       "@class='row']/div[@class='col-12 mt-4 col-md-6']/div[@class='check-box-tree-wrapper']/div[" \
                       "@id='tree-node']/ol/li[@class='rct-node rct-node-parent rct-node-expanded']/ol/li[2]/span[" \
                       "1]/button[1]//*[name()='svg']//*[name()='path' and contains(@d,'M7.41 7.84')]"

    TOGGLE_WORKSPACE = "//body//div[@id='app']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[" \
                       "@class='rct-node rct-node-parent rct-node-expanded']//li[1]//span[1]//button[1]//*[name(" \
                       ")='svg']//*[name()='path' and contains(@d,'M7.41 7.84')]"

    TOGGLE_OFFICE = "//body//div[@id='app']//li[@class='rct-node rct-node-parent rct-node-expanded']//li[" \
                    "@class='rct-node rct-node-parent rct-node-expanded']//li[2]//span[1]//button[1]//*[name()='svg']"

    TOGGLE_DOWNLOADS = "//li[3]//span[1]//button[1]//*[name()='svg']"

    # Checkbox locators
    CHECKBOX_HOME = "//label[@for='tree-node-home']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_DESKTOP = "//label[@for='tree-node-desktop']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_NOTES = "//label[@for='tree-node-notes']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_COMMANDS = "//label[@for='tree-node-commands']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_DOCUMENTS = "//label[@for='tree-node-documents']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_WORKSPACE = "//label[@for='tree-node-documents']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_REACT = "//label[@for='tree-node-react']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_ANGULAR = "//label[@for='tree-node-angular']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_VEU = "//label[@for='tree-node-veu']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_OFFICE = "//label[@for='tree-node-office']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_PUBLIC = "//label[@for='tree-node-public']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_PRIVATE = "//label[@for='tree-node-private']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_CLASSIFIED = "//label[@for='tree-node-classified']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_GENERAL = "//label[@for='tree-node-general']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_DOWNLOADS = "//label[@for='tree-node-downloads']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_WORD_FILE = "//label[@for='tree-node-wordFile']//span[@class='rct-checkbox']//*[name()='svg']"
    CHECKBOX_EXCEL_FILE = "//label[@for='tree-node-excelFile']//span[@class='rct-checkbox']//*[name()='svg']"

    def __init__(self, driver):
        super().__init__(driver)

    # Methods for locating expand buttons
    def get_expand_all_btn(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.EXPAND_ALL_BTN)

    def get_collapse_all_btn(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.COLLAPSE_ALL_BTN)

    # Methods for locating toggle buttons
    def get_toggle_home_btn(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.TOGGLE_HOME)

    def get_toggle_desktop_btn(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.TOGGLE_DESKTOP)

    def get_toggle_documents_btn(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.TOGGLE_DOCUMENTS)

    def get_toggle_workspace_btn(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.TOGGLE_WORKSPACE)

    def get_toggle_office_btn(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.TOGGLE_OFFICE)

    def get_toggle_downloads_btn(self):
        self.wait_for_element_to_be_clickable(By.XPATH, self.TOGGLE_DOWNLOADS)

    # Methods for locating checkboxes
    def get_home_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_HOME)

    def get_desktop_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_DESKTOP)

    def get_notes_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_NOTES)

    def get_commands_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_COMMANDS)

    def get_documents_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_DOCUMENTS)

    def get_workspace_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_WORKSPACE)

    def get_react_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_REACT)

    def get_angular_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_ANGULAR)

    def get_veu_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_VEU)

    def get_office_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_OFFICE)

    def get_public_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_PUBLIC)

    def get_private_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_PRIVATE)

    def get_classified_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_CLASSIFIED)

    def get_general_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_GENERAL)

    def get_downloads_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_DOWNLOADS)

    def get_word_file_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_WORD_FILE)

    def get_excel_file_checkbox(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.CHECKBOX_EXCEL_FILE)

    # Button action methods

    def click_on_expand_all(self):
        self.get_expand_all_btn().click()
        time.sleep(1)

    def click_on_collapse_all(self):
        self.get_collapse_all_btn().click()
        time.sleep(1)

    def expand_home_toggle(self):
        self.get_toggle_home_btn().click()
        time.sleep(1)

    def collapse_home_toggle(self):
        self.expand_home_toggle()
        self.get_toggle_home_btn().click()
        time.sleep(1)

    def expand_desktop_toggle(self):
        self.expand_home_toggle()
        self.get_toggle_desktop_btn().click()
        time.sleep(1)

    def collapse_desktop_toggle(self):
        self.expand_desktop_toggle()
        self.get_toggle_desktop_btn().click()
        time.sleep(1)

    def expand_documents_toggle(self):
        self.expand_home_toggle()
        self.get_toggle_documents_btn().click()
        time.sleep(1)

    def collapse_documents_toggle(self):
        self.expand_documents_toggle()
        self.get_toggle_documents_btn().click()
        time.sleep(1)

    def expand_workspace_toggle(self):
        self.expand_documents_toggle()
        self.get_toggle_workspace_btn().click()
        time.sleep(1)

    def collapse_workspace_toggle(self):
        self.expand_workspace_toggle()
        self.get_toggle_workspace_btn().click()
        time.sleep(1)

    def expand_office_toggle(self):
        self.expand_documents_toggle()
        self.get_toggle_office_btn().click()
        time.sleep(1)

    def collapse_office_toggle(self):
        self.expand_office_toggle()
        self.get_toggle_office_btn().click()
        time.sleep(1)

    def expand_downloads_toggle(self):
        self.expand_home_toggle()
        self.get_toggle_downloads_btn().click()
        time.sleep(1)

    def collapse_downloads_toggle(self):
        self.expand_downloads_toggle()
        self.get_toggle_downloads_btn().click()
        time.sleep(1)

    # Checkbox action methods

    def select_home_checkbox(self):
        self.get_home_checkbox().click()
        time.sleep(1)

    def unselect_home_checkbox(self):
        self.select_home_checkbox()
        self.get_home_checkbox().click()
        time.sleep(1)

    def select_desktop_checkbox(self):
        self.expand_desktop_toggle()
        self.get_desktop_checkbox().click()
        time.sleep(1)

    def unselect_desktop_checkbox(self):
        self.select_desktop_checkbox()
        self.get_desktop_checkbox().click()
        time.sleep(1)

    def select_notes_checkbox(self):
        self.expand_desktop_toggle()
        self.get_notes_checkbox().click()
        time.sleep(1)

    def unselect_notes_checkbox(self):
        self.select_notes_checkbox()
        self.get_notes_checkbox().click()
        time.sleep(1)

    def select_commands_checkbox(self):
        self.expand_desktop_toggle()
        self.get_commands_checkbox().click()
        time.sleep(1)

    def unselect_commands_checkbox(self):
        self.select_commands_checkbox()
        self.get_commands_checkbox().click()
        time.sleep(1)

    def select_documents_checkbox(self):
        self.expand_documents_toggle()
        self.get_documents_checkbox().click()
        time.sleep(1)

    def unselect_documents_checkbox(self):
        self.select_documents_checkbox()
        self.get_documents_checkbox().click()
        time.sleep(1)

    def select_workspace_checkbox(self):
        self.expand_workspace_toggle()
        self.get_workspace_checkbox().click()
        time.sleep(1)

    def unselect_workspace_checkbox(self):
        self.select_workspace_checkbox()
        self.get_workspace_checkbox().click()
        time.sleep(1)

    def select_react_checkbox(self):
        self.expand_workspace_toggle()
        self.get_react_checkbox().click()
        time.sleep()

    def unselect_react_checkbox(self):
        self.select_react_checkbox()
        self.get_react_checkbox().click()
        time.sleep(1)

    def select_angular_checkbox(self):
        self.expand_workspace_toggle()
        self.get_angular_checkbox().click()
        time.sleep(1)

    def unselect_angular_checkbox(self):
        self.select_angular_checkbox()
        self.get_angular_checkbox().click()
        time.sleep(1)

    def select_veu_checkbox(self):
        self.expand_workspace_toggle()
        self.get_veu_checkbox().click()
        time.sleep(1)

    def unselect_veu_checkbox(self):
        self.select_veu_checkbox()
        self.get_veu_checkbox().click()
        time.sleep(1)






