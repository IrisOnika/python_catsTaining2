# -*- coding: utf-8 -*-
from model.group import Group

group_name = 'testName3'
group_logo = 'testLogo3'
group_comment = 'comment3'


def test_add_group(appl):
    old_group_list = appl.group.get_group_list()
    new_group = Group(group_name, group_logo, group_comment)
    appl.group.create(new_group)
    assert len(old_group_list) + 1 == appl.group.count()
    new_group_list = appl.group.get_group_list()
    old_group_list.append(new_group)
    assert sorted(old_group_list, key=appl.sorted_by_id) == sorted(new_group_list, key=appl.sorted_by_id)




