from model.contact import Contact
import re

class ContactHelper:
    def __init__(self,app):
        self.app = app

    def open_start_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/index.php") and len(driver.find_elements_by_xpath("//input[@value='Delete']")) > 0):
            driver.find_element_by_link_text("home").click()

    def open_add_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/edit.php") and len(
                driver.find_elements_by_xpath("//div[@id='content']//input[1][@name='submit']")) > 0):
            driver.find_element_by_link_text("add new").click()

    def create(self, contact):
        driver = self.app.driver
        self.open_add_page()
        self.fill_contact_form(contact)
        driver.find_element_by_xpath("//div[@id='content']//input[1][@name='submit']").click()
        self.open_start_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        driver = self.app.driver
        self.select_contact_by_index(index)
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to_alert().accept()
        self.open_start_page()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)


    def edit_contact_by_index(self,index, contact):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        driver.find_element_by_name("update").click()
        self.open_start_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.open_start_page()
        driver.find_element_by_xpath("//tr[%s]//td[8]//img[@title='Edit']" % str(index+2)).click()

    def open_contact_to_view_by_index(self, index):
        driver = self.app.driver
        self.open_start_page()
        driver.find_element_by_xpath("//tr[%s]//td[7]//img[@title='Details']" % str(index+2)).click()


    def select_contact_by_index(self, index):
        driver = self.app.driver
        driver.find_elements_by_xpath("//tr//td[1]")[index].click()


    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("address", contact.address)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)


    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def count(self):
        driver = self.app.driver
        return len(driver.find_elements_by_xpath("//tr[@name = 'entry']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_start_page()
            self.contact_cache = []
            elements = driver.find_elements_by_xpath("//tr[@name = 'entry']")
            for element in elements:
                id = element.find_element_by_xpath(".//td[1]/input").get_attribute("id")
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                address = element.find_element_by_xpath(".//td[4]").text
                all_emails = element.find_element_by_xpath(".//td[5]").text
                all_phones = element.find_element_by_xpath(".//td[6]").text
                self.contact_cache.append(Contact(firstname=firstname,lastname=lastname,address=address, id=id,
                                                  all_phones_from_home_page = all_phones, all_emails_from_home_page= all_emails))
        return list(self.contact_cache)


    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element_by_name("firstname").get_attribute("value")
        lastname = driver.find_element_by_name("lastname").get_attribute("value")
        address = driver.find_element_by_name("address").get_attribute("value")
        id = driver.find_element_by_name("id").get_attribute("value")
        homephone = driver.find_element_by_name("home").get_attribute("value")
        workphone = driver.find_element_by_name("work").get_attribute("value")
        mobilephone = driver.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = driver.find_element_by_name("phone2").get_attribute("value")
        email = driver.find_element_by_name("email").get_attribute("value")
        email2 = driver.find_element_by_name("email2").get_attribute("value")
        email3 = driver.find_element_by_name("email3").get_attribute("value")

        return Contact(firstname=firstname,lastname=lastname, address=address,id=id,homephone=homephone,
                       workphone=workphone,mobilephone=mobilephone,secondaryphone=secondaryphone, email=email,
                       email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_to_view_by_index(index)
        text = driver.find_element_by_id("content").text
        homephone = re.search("H: (.*)",text).group(1)
        workphone = re.search("W: (.*)",text).group(1)
        mobilephone = re.search("M: (.*)",text).group(1)
        secondaryphone = re.search("P: (.*)",text).group(1)
        return Contact(homephone=homephone,workphone=workphone,mobilephone=mobilephone,
                       secondaryphone=secondaryphone)






