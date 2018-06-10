# -*- coding: utf-8 -*-
from model.group import Group

login = 'admin'
password = 'secret'


def test_add_group(appl):
    appl.session.login(login, password)
    appl.group.delete()
    appl.session.logout()