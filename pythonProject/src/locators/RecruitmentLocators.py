from selenium.webdriver.common.by import By


class RecruitmentLocators:
    ADD_FIRST_NAME = (By.NAME, "firstName")
    ADD_LAST_NAME = (By.NAME, "lastName")
    ADD_CONTACT_NO = (By.XPATH, "(//input[@placeholder= 'Type here'])[2]")
    SAVE_BUTTON = (By.XPATH, "//button[@type= 'submit']")
    EMAIL_ID = (By.XPATH, "(//input[@placeholder= 'Type here'])[1]")
    RECRUITMENT_PAGE = (By.LINK_TEXT, 'Recruitment')
    ADD_BUTTON = (By.CLASS_NAME, 'bi-plus')

    ADD_CANDIDATE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate'
    DROPDOWN_VACANCY = (By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active']/div")

    DROPDOWN_VACANCY_SELECT_VALUE = (By.XPATH, "//*[contains(text(),'Associate IT Manager')]")
    VERIFY_RECRUITMENT_PAGE = (By.TAG_NAME, "h6")
