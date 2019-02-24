# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)


    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/group.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").send_keys("qwe")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Logout").click()
        pass

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

if __name__ == "__main__":
    unittest.main()
