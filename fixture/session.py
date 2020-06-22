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