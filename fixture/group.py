class GroupHelper:
    def __init__(self,app):
        self.app = app


    def open_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def return_to_page(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[contains(text(),'group page')]").click()

    def create(self, group):
        driver = self.app.driver
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()

    def delete_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()

    def edit_first_group(self, group):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("edit").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("update").click()