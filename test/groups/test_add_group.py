# -*- coding: utf-8 -*-
from model.group import Group

group_name = 'testName3'
group_logo = 'testLogo3'
group_comment = 'comment3'


def test_add_group(appl):
    old_group_list = appl.group.get_group_list()
    appl.group.create(Group(group_name, group_logo, group_comment))
    new_group_list = appl.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)



