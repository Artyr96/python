from selenium import webdriver
from fixture.session import SessionHelper
from fixture.newuser import NuserHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.newuser = NuserHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_page(self):
        driver = self.driver
        driver.get("https://starkportal.solardigital.com.ua/login")

    def destroy(self):
        self.driver.quit()
