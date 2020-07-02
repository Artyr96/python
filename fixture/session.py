class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_page()
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_xpath("//div/div").click()
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//div[@id='app']/aside/div[2]/div/div[2]/div/div/div/div").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_xpath("//button[@type='submit']")) > 0

    def is_logged_in_as(self, username):
        driver = self.app.driver
        return driver.find_element_by_xpath("//div[@id='app']/aside/div[2]/div/div[2]/div/div/div/div").text == username

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)


