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
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        driver = self.app.driver
        self.select_group_by_index(index)
        driver.find_element_by_name("delete").click()
        self.return_to_page()
        self.group_cache = None

    def edit_first_group(self, group):
        self.edit_group_by_index(0,group)

    def edit_group_by_index(self,index, group):
        driver = self.app.driver
        self.select_group_by_index(index)
        driver.find_element_by_name("edit").click()
        self.fill_group_form(group)
        driver.find_element_by_name("update").click()
        self.return_to_page()
        self.group_cache = None

    def select_group_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()


    def select_group_by_index(self,index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()

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

    group_cache= None

    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_page()
            self.group_cache = []
            for element in driver.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

