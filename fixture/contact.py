class ContactHelper:
    def __init__(self,app):
        self.app = app

    def open_start_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    def open_add_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def create(self, contact):
        driver = self.app.driver
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("mobile").send_keys(contact.mobile)
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_xpath("//div[@id='content']//input[1][@name='submit']").click()

    def delete_first_contact(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//tr[2]//td[1]").click()
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to_alert().accept()


    def edit_first_contact(self, contact):
        driver = self.app.driver
        driver.find_element_by_xpath("//tr[2]//td[1]").click()
        driver.find_element_by_xpath("//tr[2]//td[8]//img[@title='Edit']").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("update").click()


