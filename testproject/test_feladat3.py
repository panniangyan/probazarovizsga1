from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# feladat URL-je
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html"


def test_timesheet():
    # oldal betöltése
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    browser.get(URL)

    # TC01 üres kitöltés helyessége
    next_btn = browser.find_element_by_xpath('//*[@id="buttons"]/input')
    assert next_btn.get_attribute("disabled")

    email = browser.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[1]')
    email.send_keys("a@")
    assert next_btn.get_attribute("disabled")


    # TC02 kitöltés
    email.clear()
    email.send_keys("test@bela.hu")
    browser.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[2]').send_keys("2")
    browser.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[3]').send_keys("0")
    browser.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/textarea').send_keys("working hard")
    browser.find_element_by_xpath("//select[@name='dropDown']/option[text()='Time working on visual effects for movie']").click()

    next_btn.click()
    time.sleep(2)
    assert browser.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[2]/span[1]').text == "2"
    assert browser.find_element_by_xpath('//*[@id="section-thankyou"]/div/p[2]/span[2]').text == "0"

    browser.quit()
