import pytest
from pages.demoqa_check_box_page import DemoqaCheckBoxPage
import time

@pytest.mark.usefixtures("tc_setup")
class TestCheckBoxCase02:
    def test_check_box_tc_02(self):
        # 01. Launch the demoqa website
        ch_bx_page = DemoqaCheckBoxPage(self.driver)
        ch_bx_page.navigate_to_checkbox_page()

        # 02.Click on Expand all button
        ch_bx_page.click_on_expand_all()
        time.sleep(2)

        # 03.Select the Home checkbox
        ch_bx_page.select_home_checkbox()
        time.sleep(2)

        # Verify (Assert) that all the checkboxes on the page are selected


