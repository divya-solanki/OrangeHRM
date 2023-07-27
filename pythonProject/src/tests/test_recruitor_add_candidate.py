import time
from src.library.ReadExcelFile import read_test_data_from_excel as testdata
from src.library.config_helpers import get_testdata_path
import pytest
from src.pages.Recruitment import Recruitment
from src.pages.HomePage import HomePage
from src.library.config_helpers import get_testdata_path


@pytest.mark.usefixtures("chrome_init_driver")
class TestRecruitment:
    @pytest.mark.parametrize("firstname, lastname, email, contact",
                             testdata.read_excel_file(get_testdata_path(), "recruitment", "tc02"))
    def test_add_candidate(self, firstname, lastname, email, contact):
        homepage = HomePage(self.driver)
        homepage.do_login()

        recruitment = Recruitment(self.driver)

        recruitment.click_recruitment_page()
        recruitment.click_add_button()
        recruitment.input_first_name(firstname)
        recruitment.input_last_name(lastname)
        recruitment.select_vacancy_dropdown()
        recruitment.select_value_from_dropdown_vacancy()
        recruitment.input_email_id(email)
        recruitment.input_contact_number(contact)
        recruitment.click_save_button()
