class ContactHelper:
    def __init__(self,app):
        self.app = app

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