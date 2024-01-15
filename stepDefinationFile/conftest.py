import pytest
from selenium import webdriver

@pytest.fixture(scope="package")
def browserInvoke():
    driver= webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="package")
def flightUrl():
    url1 = "https://www.makemytrip.com/flights/"
    return url1

@pytest.fixture(scope="package")
def hotelUrl():
    url2 = "https://www.makemytrip.com/hotels/"
    return url2