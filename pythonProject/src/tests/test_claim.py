import time
import pytest
from src.pages.HomePage import HomePage
from src.pages.Claim import Claim


@pytest.mark.usefixtures("chrome_init_driver")
class TestClaimDetails:

    @pytest.mark.tcid03
    def test_claim_employee_details(self):
        homepage = HomePage(self.driver)
        homepage.do_login()

        claim = Claim(self.driver)
        claim.click_claim_page()
        claim.verify_claim_page()
        time.sleep(2)
        claim.view_record_details()
        time.sleep(10)



