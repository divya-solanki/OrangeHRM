from selenium.webdriver.common.by import By


class ClaimLocators:
    VERIFY_CLAIM_PAGE = (By.TAG_NAME, "h6")
    EMPLOYEE_RECORDS = 'oxd-table-row'
    employee_name_path_1 = "//div[@class='oxd-table-body']/div["
    employee_name_path_2 = "]/div[@role='row']/div[2]/div"

    view_details_button_1 = "//div[@class='oxd-table-body']/div["
    view_details_button_2 = "]/div[@role ='row']/div[9]/div/button"
    x = 0

    CLAIM_PAGE = (By.LINK_TEXT, 'Claim')
