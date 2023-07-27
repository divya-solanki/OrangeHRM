
from selenium import webdriver
import pytest
from _pytest import scope


@pytest.fixture(scope='class')
def chrome_init_driver(request):
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(3)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.fixture(scope='class')
def firefox_init_driver(request):
    firefox_driver = webdriver.Firefox
    request.cls.driver = firefox_driver
    yield
    firefox_driver.close()
