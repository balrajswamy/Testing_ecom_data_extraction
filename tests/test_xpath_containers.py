from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import pytest

def test_xpath_container_title_price():
    # Set up Chrome WebDriver

    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(3)
    # URL of the eBay search result page
    url = "https://www.ebay.com/"
    driver.get(url)
    time.sleep(3)

    search_box = driver.find_element(By.XPATH, '//input[@id="gh-ac"]')
    search_box.send_keys("Macmini")
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="gh-btn"]').click()
    # XPath for the product container
    product_containers = driver.find_elements(By.XPATH, '//div[@class="s-item__info clearfix"]')
    title_count = 0
    price_count = 0
    data = []
    for container in product_containers:
        # Extracting the product title
        try:
            title_element = container.find_element(By.XPATH, './/div[@class="s-item__title"]/span')
            title = title_element.text.strip()
            title_count=title_count+1
        except:
            title = None

        # Extracting the product price
        try:
            price_element = container.find_element(By.XPATH,
                                                   './/div[@class="s-item__detail s-item__detail--primary"]/span[@class="s-item__price"]')
            price = price_element.text.strip()
            price_count = price_count+1
        except:
            price = None

        # Check that titles and prices are fetched correctly
        #assert len(product_titles) > 0, "No product titles found"
        #assert len(product_prices) > 0, "No product prices found"

        # Printing the results

        if title and price:
            print(f"Title: {title} | Price: {price}")
            inner_list = [title, price]
            data.append(inner_list)


    assert title_count > 0, "No product titles found"
    assert price_count > 0, "No product prices found"
    print(f"total title is {title_count}")
    print(f"total prices is {price_count}")
    # Quit the WebDriver session
    driver.quit()


    df = pd.DataFrame(data=data, columns=["title","price"])
    df.to_csv("extracted_data.csv", index=False)

