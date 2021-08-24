from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


# feladat URL-je
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html"


def test_lottery():
    # oldal betöltése
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    browser.get(URL)

    # TC01 nincs szám
    assert browser.find_element_by_id("container").text == ""

    # TC02 lottóhúzás
    # click 6 times
    i = 0
    generate = browser.find_element_by_id("draw-number")
    while i < 6:
        generate.click()
        i = i + 1

    # kiszedem a számokat és ellenőrzöm, hogy pontosan 6 számot kaptunk
    numbers = browser.find_elements_by_xpath('//*[@class="balls"]')
    assert len(numbers) == 6

    # ellenőrzöm hogy a számok 1 és 59 között vannak
    for i in numbers:
    #    print(i.text)
        assert 1 <= int(i.text) <= 59

    # TC03 hetedik szám, reset ellenőrzöm, hogy továbbra is csak 6 számot kaptunk
    generate.click()
    numbers = browser.find_elements_by_xpath('//*[@class="balls"]')
    assert len(numbers) == 6

    # reset gomb megnyomása, ellenőrzöm hogy nem jelenik meg egyetlen szám is
    browser.find_element_by_id("reset-numbers").click()
    assert browser.find_element_by_id("container").text == ""
    time.sleep(1)

    browser.quit()
