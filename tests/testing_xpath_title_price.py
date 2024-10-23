# testing_xpath.py
import pytest
import allure
from selenium.webdriver.common.by import By
import time

# URL of the eBay search page for Macmini
URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2499334.m570.l1313&_nkw=Macmini&_sacat=0"

@allure.title(f"TestCASE#1 to visit {URL}")
@pytest.mark.parametrize("search_url", [URL])
def test_fetch_product_titles_and_prices(driver, search_url):
    driver.get(search_url)

    search_box = driver.find_element(By.XPATH,'//input[@id="gh-ac"]')
    search_box.send_keys("Macmini")
    time.sleep(1)

    driver.find_element(By.XPATH,'//*[@id="gh-btn"]').click()

    # Define XPath to locate product titles and prices
    title_xpath = '//div[@class="s-item__title"]/span[@role="heading"]/'.text
    price_xpath = '//span[@class="s-item__price"]'

    # Fetch all product titles
    product_titles = driver.find_elements(By.XPATH, title_xpath)

    # Fetch all product prices
    product_prices = driver.find_elements(By.XPATH, price_xpath)

    # Check that titles and prices are fetched correctly
    assert len(product_titles) > 0, "No product titles found"
    assert len(product_prices) > 0, "No product prices found"

    # Print titles and prices for reference
    for title, price in zip(product_titles, product_prices):
        print(f"Product: {title.text}, Price: {price.text}")

    # Additional checks can be added as per requirements
