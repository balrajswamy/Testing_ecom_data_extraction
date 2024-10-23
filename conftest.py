# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="session")
def driver():

    # Initialize the WebDriver

    driver = webdriver.Chrome()

    # Maximize the window (optional)
    driver.maximize_window()

    # Return the driver to the test function
    yield driver

    # Quit the driver after the session
    driver.quit()
