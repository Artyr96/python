class NuserHelper:

    def __init__(self, app):
        self.app = app

    def add(self, new_user_data):
        driver = self.app.driver
        self.app.open_page()
        driver.find_element_by_xpath("//div[@id='app']/aside/div[2]/nav/ul/li[4]/button/span").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_xpath("//div[@id='app']/header/div/div/button").click()
        self.fill_user_form(new_user_data)
        driver.find_element_by_xpath("//div[@id='app']/main/form/div/div[2]/div/div[4]/div/div[2]/div/div/div/div/div").click()
        driver.find_element_by_xpath("//div[@id='app']/main/form/div/div[2]/div/div[4]/div/div[2]/div/div/div/div/div[3]/ul/li/span").click()
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()

    def change_field(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def fill_user_form(self, new_user):
        self.change_field("name", new_user.name)
        self.change_field("username", new_user.username)
        self.change_field("password", new_user.password)

    def delete_user(self):
        driver = self.app.driver
        self.app.open_page()
        driver.find_element_by_xpath("//div[@id='app']/aside/div[2]/nav/ul/li[4]/button/span").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_css_selector(
            "#gen-table-row-15 > div.gen-table-group.gen-table-group--actions > div.gen-table-cell.gen-table-cell__actions > div.btn-gen-table-delete-wrap > button.btn-gen-table-delete > svg").click()
        driver.find_element_by_xpath("//div[@id='gen-table-row-15']/div[4]/div/div[3]/button/div/button[2]").click()

    def modify(self, new_user_data):
        driver = self.app.driver
        self.app.open_page()
        driver.find_element_by_xpath("//div[@id='app']/aside/div[2]/nav/ul/li[4]/button/span").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_css_selector(
            "#gen-table-row-15>div.gen-table-group.gen-table-group--actions>div.gen-table-cell.gen-table-cell__actions > div.btn-gen-table-edit-wrap > button.btn-gen-table-edit > svg").click()
        self.fill_user_form(new_user_data)
        driver.find_element_by_xpath("//*[@id='app']/main/form[2]/div/div[1]/div[3]/button").click()
