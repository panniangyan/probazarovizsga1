from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# feladat URL-je
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html"


def test_landtransfertax():
    # oldal betöltése
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    browser.get(URL)

    # mezők keresése
    price = browser.find_element_by_id("price")
    go_btn = browser.find_element_by_xpath('//button')

    # TC01 üres kitöltés helyessége
    go_btn.click()
    assert price.text == ""
    assert browser.find_element_by_id("disclaimer").text == "Enter the property value before clicking Go button."

    # TC02
    browser.refresh()
    price = browser.find_element_by_id("price")
    go_btn = browser.find_element_by_xpath('/html/body/main/div/div/p[1]/button')

    price.send_keys("33333")
    go_btn.click()
    assert browser.find_element_by_id("tax").get_attribute("value") == "166.665"

    browser.quit()

