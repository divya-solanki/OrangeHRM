from src.locators.RecruitmentLocators import RecruitmentLocators
from src.library.CommonFunc import CommonFunc


class Recruitment(RecruitmentLocators):

    def __init__(self, driver):
        self.driver = driver
        self.common = CommonFunc(self.driver)

    def click_recruitment_page(self):
        self.common.wait_and_click(self.RECRUITMENT_PAGE)

    def click_add_button(self):
        self.common.wait_and_click(self.ADD_BUTTON)

    def input_first_name(self, firstname):
        self.common.wait_and_input_text(self.ADD_FIRST_NAME, firstname)

    def input_last_name(self, lastname):
        self.common.wait_and_input_text(self.ADD_LAST_NAME, lastname)

    def input_email_id(self, email):
        self.common.wait_and_input_text(self.EMAIL_ID, email)

    def input_contact_number(self, c_number):
        self.common.wait_and_input_text(self.ADD_CONTACT_NO, c_number)

    def select_vacancy_dropdown(self):
        self.common.wait_and_click(self.DROPDOWN_VACANCY)

    def select_value_from_dropdown_vacancy(self):
        self.common.wait_and_click(self.DROPDOWN_VACANCY_SELECT_VALUE)

    def click_save_button(self):
        self.common.wait_and_click(self.SAVE_BUTTON)

    def verify_recruitment_page(self):
        check_value = 'Recruitment'
        self.common.verify_page(self.VERIFY_RECRUITMENT_PAGE,check_value)
