# -*- coding: utf-8 -*-
from model.group import Group

group_name = 'testName3'
group_logo = 'testLogo3'
group_comment = 'comment3'


def test_add_group(appl):
    appl.group.create(Group(group_name, group_logo, group_comment))




