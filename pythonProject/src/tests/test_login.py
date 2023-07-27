import pytest
from src.pages.HomePage import HomePage


@pytest.mark.usefixtures("chrome_init_driver")
class TestLogin:

    @pytest.mark.tcid01
    def test_login_positive(self):
        homepage = HomePage(self.driver)

        homepage.do_login()
