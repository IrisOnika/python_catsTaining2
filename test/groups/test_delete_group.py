# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_group(appl):
    if appl.group.count()==0:
        appl.group.create(Group(_name="test"))
    old_group_list = appl.group.get_group_list()
    appl.group.delete()
    new_group_list = appl.group.get_group_list()
    assert len(old_group_list) - 1 == len(new_group_list)
    old_group_list[0:1] = []
    assert old_group_list == new_group_list