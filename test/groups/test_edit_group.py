# -*- coding: utf-8 -*-
from model.group import Group

login = 'admin'
password = 'secret'
group_name = 'testName1_new'
group_logo = 'testLogo1_new'
group_comment = 'comment1_new'


def test_add_group(appl):
    appl.session.login(login, password)
    appl.group.edit(Group(group_name, group_logo, group_comment))
    appl.session.logout()