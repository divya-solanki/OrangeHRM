import time

from selenium.webdriver.common.by import By
from src.locators.ClaimLocators import ClaimLocators
from src.library.CommonFunc import CommonFunc


class Claim(ClaimLocators):

    def __init__(self, driver):
        self.driver = driver
        self.common = CommonFunc(self.driver)

    def click_claim_page(self):
        self.common.wait_and_click(self.CLAIM_PAGE)

    def verify_claim_page(self):
        check_value = 'Claim'
        self.common.verify_page(self.VERIFY_CLAIM_PAGE, check_value)

    def view_record_details(self):

        all_records = self.driver.find_elements(By.CLASS_NAME, 'oxd-table-row')
        no_of_records = len(all_records)

        if no_of_records > 1:
            for x in range(1,no_of_records):
                employee_name = self.driver.find_element(By.XPATH,
                                                         "//div[@class = 'oxd-table-body']/div[" + str(x) + "]/div[@role='row']/div[2]/div").text
                print(employee_name)
                if employee_name == 'sai Raval':
                    self.driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[" + str(x) + "]/div[@role ='row']/div[9]/div/button").click()
                    time.sleep((5))
                    break
        else:
            print('No record found')



