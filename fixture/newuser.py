class NuserHelper:


    def __init__(self, app):
        self.app = app

    def open_page(self):
        driver = self.app.driver
        driver.get("https://starkportal.solardigital.com.ua/login")

    def add(self, new_user):
        driver = self.app.driver
        driver.find_element_by_xpath("//div[@id='app']/aside/div[2]/nav/ul/li[4]/button/span").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_xpath("//div[@id='app']/header/div/div/button").click()
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(new_user.name)
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(new_user.username)
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(new_user.password)
        driver.find_element_by_xpath(
            "//div[@id='app']/main/form/div/div[2]/div/div[4]/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath(
            "//div[@id='app']/main/form/div/div[2]/div/div[4]/div/div[2]/div/div/div/div/div[3]/ul/li/span").click()
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()

    def delete_user(self):
        driver = self.app.driver
        self.app.open_page()
        driver.find_element_by_xpath("//div[@id='app']/aside/div[2]/nav/ul/li[4]/button/span").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_css_selector("#gen-table-row-15 > div.gen-table-group.gen-table-group--actions > div.gen-table-cell.gen-table-cell__actions > div.btn-gen-table-delete-wrap > button.btn-gen-table-delete > svg").click()
        driver.find_element_by_xpath("//div[@id='gen-table-row-15']/div[4]/div/div[3]/button/div/button[2]").click()
