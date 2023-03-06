import pytest

from pages.demoqa_text_box_page import DemoqaTextBoxPage


@pytest.mark.usefixtures("tc_setup")
class TestTxtBoxCase01():

    def test_txt_box_tc_01(self):

        # 01. Launch the demoqa website and navigate to text box page
        txt_bx_page = DemoqaTextBoxPage(self.driver)
        txt_bx_page.navigate_to_text_box_page()

        # 02. Enter full name
        txt_bx_page.enter_full_name(DemoqaTextBoxPage.full_name)

        # 03. Enter email
        txt_bx_page.enter_email(DemoqaTextBoxPage.email)

        # 04. Enter current address
        txt_bx_page.enter_address(DemoqaTextBoxPage.address)

        # 05. Enter permanent address
        txt_bx_page.enter_perm_address(DemoqaTextBoxPage.perm_address)

        # 06. Click on Submit
        # 6a, it is necessary to scroll down so that the button is available for clicking in the UI
        txt_bx_page.page_scroll()
        # 6b, click on the submit button
        txt_bx_page.click_on_submit()

        # 07. Verify that the information is submitted
        result_txt_box = DemoqaTextBoxPage(self.driver)
        result_txt_box.test_verify_input()
