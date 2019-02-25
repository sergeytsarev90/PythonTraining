from selenium import webdriver

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[contains(text(),'group page')]").click()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def create_group(self, group):
        driver = self.driver
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()

    def open_group_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def login(self):
        driver = self.driver
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def open_add_contact_page(self):
        driver = self.driver
        driver.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        driver = self.driver
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("mobile").send_keys(contact.mobile)
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_xpath("//div[@id='content']//input[1][@name='submit']").click()

    def destroy(self):
        self.driver.quit()
