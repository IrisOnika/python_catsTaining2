# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import App

login = 'admin'
password = 'secret'
group_name = 'testName3'
group_logo = 'testLogo3'
group_comment = 'comment3'


@pytest.fixture()
def appl(request):
    fixture = App()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(appl):
    appl.login(login, password)
    appl.groupForm(Group(group_name, group_logo, group_comment))
    appl.logout()




