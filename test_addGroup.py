# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group

login='admin'
password='secret'
menu_tab='groups'
group_name='testName3'
group_logo='testLogo3'
group_comment='comment3'


class addGroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_(self):
        success = True
        wd = self.wd
        self.openStartPage(wd)
        self.login(wd, _login=login, _password=password)
        self.openMenu(wd, _tab=menu_tab)
        self.groupForm(wd, Group(_name=group_name, _logo=group_logo, _comment=group_comment))
        self.openMenu(wd, _tab=menu_tab)
        self.logout(wd)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

    def login(self, wd, _login, _password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(_login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(_password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def openStartPage(self, wd):
        wd.get("http://127.0.0.1/addressbook/")

    def groupForm(self, wd, Group):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.logo)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.comment)
        wd.find_element_by_name("submit").click()

    def openMenu(self, wd, _tab):
        wd.find_element_by_link_text(_tab).click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


if __name__ == '__main__':
    unittest.main()
