import random
import string

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonFunc:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 5

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, self.default_timeout).until(
            EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(locator)).click()

    def random_email(self):
        random_name = ''.join(random.choice(string.ascii_lowercase) for x in range(7))
        email_id = random_name + '@testmail.com'
        return email_id

    def verify_page(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        web_element = WebDriverWait(self.driver, self.default_timeout).until(
            EC.visibility_of_element_located(locator))
        assert web_element.text == text

    def get_records_from_table(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        return WebDriverWait(self.driver, self.default_timeout).until(
            EC.visibility_of_all_elements_located(locator))
