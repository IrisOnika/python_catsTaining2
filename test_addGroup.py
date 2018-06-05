# -*- coding: utf-8 -*-
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
        self.app.login(login, password)
        self.app.groupForm(Group(group_name, group_logo, group_comment))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == '__main__':
    unittest.main()
