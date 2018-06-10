# -*- coding: utf-8 -*-
from model.group import Group

login = 'admin'
password = 'secret'
group_name = 'testName3'
group_logo = 'testLogo3'
group_comment = 'comment3'


def test_add_group(appl):
    appl.session.login(login, password)
    appl.group.create(Group(group_name, group_logo, group_comment))
    appl.session.logout()




