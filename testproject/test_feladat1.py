from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# feladat URL-je
URL = "https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html"


class TestFeladat1(object):
    def setup(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    def test_hogwards(self):
        # # utas adatai
        passenger_name = "Harry Potter"
        departure_date = "08/09/2021"
        departure_time = "0800AM"

        self.browser.find_element_by_id("passenger").send_keys(passenger_name)
        self.browser.find_element_by_id("departure-date").send_keys(departure_date)
        self.browser.find_element_by_id("departure-time").send_keys(departure_time)

        issue_ticket_btn = self.browser.find_element_by_id("issue-ticket").click()

        time.sleep(2)

        departure_date = "2021-08-09"
        departure_time = "08:00AM"


        assert self.browser.find_element_by_id("passenger-name").text == passenger_name.upper()
        assert self.browser.find_element_by_id("departure-date-text").text == departure_date
        assert self.browser.find_element_by_id("side-detparture-date").text == departure_date
        assert self.browser.find_element_by_id("departure-time-text").text == departure_time
        assert self.browser.find_element_by_id("side-departure-time").text == departure_time



