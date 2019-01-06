# Test Booking class
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import support
import time


@pytest.mark.usefixtures("driver_get")
class BaseTest:
    pass


@pytest.mark.incremental
class TestBooking(BaseTest):

    def test_search_flight(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get("http://blazedemo.com/")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Find Flights']"))).click()
        time.sleep(1)



    def test_choose_any_flight(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Choose This Flight"))).click()
        text = self.driver.find_element_by_tag_name("h2").text
        assert text == "Your flight from Paris to Buenos Aires has been reserved."
        time.sleep(1)
        assert 0

