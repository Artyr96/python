# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job_1(self):
        driver = self.driver
        driver.get("https://starkportal.solardigital.com.ua/login")
        self.login(driver, username="artur", password="artur")
        self.add_user(driver, name="te1", username="te1", password="321")
        #logout
        driver.find_element_by_xpath("//div[@id='app']/aside/div[2]/div/div[2]/div/div/div/div").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def test_app_dynamics_job_2(self):
        driver = self.driver
        driver.get("https://starkportal.solardigital.com.ua/login")
        self.login(driver, username="artur", password="artur")
        self.add_user(driver, name="te2", username="te2", password="321")
        #logout
        driver.find_element_by_xpath("//div[@id='app']/aside/div[2]/div/div[2]/div/div/div/div").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def add_user(self, driver, name, username, password):
        driver.find_element_by_xpath("//div[@id='app']/aside/div[2]/nav/ul/li[4]/button/span").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_xpath("//div[@id='app']/header/div/div/button").click()
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(name)
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath(
            "//div[@id='app']/main/form/div/div[2]/div/div[4]/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath(
            "//div[@id='app']/main/form/div/div[2]/div/div[4]/div/div[2]/div/div/div/div/div[3]/ul/li/span").click()
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()

        def add_user(self, driver, name, username, password):
            driver.find_element_by_xpath("//div[@id='app']/aside/div[2]/nav/ul/li[4]/button/span").click()
            driver.find_element_by_link_text("Users").click()
            driver.find_element_by_xpath("//div[@id='app']/header/div/div/button").click()
            driver.find_element_by_name("name").click()
            driver.find_element_by_name("name").clear()
            driver.find_element_by_name("name").send_keys(name)
            driver.find_element_by_name("username").click()
            driver.find_element_by_name("username").clear()
            driver.find_element_by_name("username").send_keys(username)
            driver.find_element_by_name("password").click()
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(password)
            driver.find_element_by_xpath(
                "//div[@id='app']/main/form/div/div[2]/div/div[4]/div/div[2]/div/div/div/div/div").click()
            driver.find_element_by_xpath(
                "//div[@id='app']/main/form/div/div[2]/div/div[4]/div/div[2]/div/div/div/div/div[3]/ul/li/span").click()
            driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()

    def login(self, driver, username, password):
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
