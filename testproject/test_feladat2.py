from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

# feladat URL-je
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html"


def test_salestax():
    # oldal betöltése
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    browser.maximize_window()
    browser.get(URL)


    # # TC01 üres kitöltés helyessége
    subtotal_btn = browser.find_element_by_id("subtotalBtn")
    subtotal_btn.click()
    subtotal = browser.find_element_by_id("subtotal")

    time.sleep(1)
    assert subtotal.get_attribute("value") == "0.00"                    # subtotal= 0.00

    # # TC02 6x6 volcanic ice 1db
    browser.find_element_by_xpath("//select[@name='price']/option[text()='6\" x 6\" Volkanik Ice']").click()
    browser.find_element_by_id("quantity").send_keys('1')
    subtotal_btn.click()

    subtotal = browser.find_element_by_id("subtotal")
    assert subtotal.get_attribute("value") == "4.95"

    time.sleep(1)
    browser.quit()
