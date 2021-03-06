class SessionHelper:

    def __init__(self,app):
        self.app = app

    def login(self,user, password):
        driver = self.app.driver
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(user)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def ensure_login(self,user,password):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user,password)


    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, user):
        driver = self.app.driver
        return self.get_logged_user() == user

    def get_logged_user(self):
        driver = self.app.driver
        return driver.find_element_by_xpath("//div[1]/form[1]/b[1]").text[1:-1]
