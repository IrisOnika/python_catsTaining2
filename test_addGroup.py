# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from application import App

login='admin'
password='secret'
group_name='testName3'
group_logo='testLogo3'
group_comment='comment3'


class addGroup(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_(self):
        self.app.login(_login=login, _password=password)
        self.app.groupForm(Group(_name=group_name, _logo=group_logo, _comment=group_comment))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

    def login(self, _login, _password):
        wd = self.wd
        self.openStartPage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(_login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(_password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[@type='submit']").click()

    def openStartPage(self):
        wd = self.wd
        wd.get("http://127.0.0.1/addressbook/")

    def groupForm(self, Group):
        wd = self.wd
        menu_tab = "groups"
        self.openMenu(_tab=menu_tab)
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
        self.openMenu(_tab=menu_tab)

    def openMenu(self, _tab):
        wd = self.wd
        wd.find_element_by_link_text(_tab).click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


if __name__ == '__main__':
    unittest.main()
