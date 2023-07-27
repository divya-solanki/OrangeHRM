from selenium.webdriver.common.by import By


class HomePageLocators:



    INPUT_USERNAME = (By.NAME, 'username')
    INPUT_PASSWORD = (By.NAME, 'password')
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    VERIFY_HOMEPAGE = (By.TAG_NAME, "h6")