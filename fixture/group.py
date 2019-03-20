from model.group import Group


class GroupHelper:
    def __init__(self,app):
        self.app = app


    def open_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/groups.php") and len(driver.find_elements_by_name("new"))>0):
            driver.find_element_by_link_text("groups").click()

    def return_to_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/groups.php") and len(driver.find_elements_by_name("new")) > 0):
            driver.find_element_by_xpath("//a[contains(text(),'group page')]").click()

    def create(self, group):
        driver = self.app.driver
        driver.find_element_by_name("new").click()
        self.fill_group_form(group)
        driver.find_element_by_name("submit").click()
        self.return_to_page()

    def delete_first_group(self):
        driver = self.app.driver
        self.select_first_group()
        driver.find_element_by_name("delete").click()
        self.return_to_page()

    def edit_first_group(self, group):
        driver = self.app.driver
        self.select_first_group()
        driver.find_element_by_name("edit").click()
        self.fill_group_form(group)
        driver.find_element_by_name("update").click()
        self.return_to_page()

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def count(self):
        driver = self.app.driver
        return len(driver.find_elements_by_name("selected[]"))

    def get_group_list(self):
        driver = self.app.driver
        self.open_page()
        groups = []
        for element in driver.find_elements_by_css_selector('span.group'):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("Value")
            groups.append(Group(name=text, id=id))
        return groups

