# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
from group import Group
from contact import Contact


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)


    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.open_group_page(driver)
        self.create_group(driver, Group(name="new_group",header="new_header",footer="new_footer"))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def test_add_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.open_add_contact_page(driver)
        self.create_contact(driver, Contact(firstname="Ivan",middlename="Ivanovich",lastname="Ivanov",nickname="Ivan",mobile="8915439323",email="ivanov@ya.ru"))
        self.logout(driver)

    def return_to_groups_page(self, driver):
        driver.find_element_by_xpath("//a[contains(text(),'group page')]").click()

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def create_group(self, driver, group):
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()

    def open_group_page(self, driver):
        driver.find_element_by_link_text("groups").click()

    def login(self, driver):
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def open_add_contact_page(self, driver):
        driver.find_element_by_link_text("add new").click()

    def create_contact(self, driver, contact):
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("mobile").send_keys(contact.mobile)
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_xpath("//div[@id='content']//input[1][@name='submit']").click()




if __name__ == "__main__":
    unittest.main()
