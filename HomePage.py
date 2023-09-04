import time

import allure
import pytest
from allure_commons.types import AttachmentType

from src.library.config_helpers import get_base_url
from src.locators.HomePageLocators import HomePageLocators
from src.library.CommonFunc import CommonFunc
from src.library.ReadExcelFile import read_test_data_from_excel as testdata
from src.library.config_helpers import get_testdata_path


class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.common = CommonFunc(self.driver)

    # def go_to_home_page(self):
    #     home_url = get_base_url()
    #     self.driver.get(home_url)
    #
    # def input_login_username(self, username):
    #     self.common.wait_and_input_text(self.INPUT_USERNAME, username)
    #
    # def input_login_password(self, password):
    #     self.common.wait_and_input_text(self.INPUT_PASSWORD, password)
    #
    # def click_login_button(self):
    #     self.common.wait_and_click(self.LOGIN_SUBMIT_BUTTON)
    #
    # def verify_homepage(self):
    #     check_value = 'Dashboard'
    #     self.common.verify_page(self.VERIFY_HOMEPAGE, check_value)

    # @pytest.mark.parametrize("username, password",
    #                          testdata.read_excel_file(get_testdata_path(), "loginDetails", "admin"))

    def do_login(self):
        # search_criteria = 'admin'
        # path = get_testdata_path()
        # sheet_name = 'loginDetails'
        # login_details = testdata.read_excel_file(path, sheet_name, search_criteria)

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.common.wait_and_input_text(self.INPUT_USERNAME, 'Admin')
        self.common.wait_and_input_text(self.INPUT_PASSWORD, 'admin1')
        self.common.wait_and_click(self.LOGIN_SUBMIT_BUTTON)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='login error',
                      attachment_type=AttachmentType.PNG)
        check_value = 'Dashboard'
        self.common.verify_page(self.VERIFY_HOMEPAGE, check_value)
