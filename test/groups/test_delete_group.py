# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_delete_group(appl, db, check_ui):
    if appl.group.count()==0:
        appl.group.create(Group(_name="test"))
    old_group_list = db.get_group_list()
    group = random.choice(old_group_list)
    appl.group.delete_group_by_id(group.id)
    new_group_list = db.get_group_list()
    old_group_list.remove(group)
    assert sorted(old_group_list, key=appl.sorted_by_id) == sorted(new_group_list, key=appl.sorted_by_id)
    if check_ui:
        def clean(group):
            return Group(_id=group.id, _name=appl.clear_dobble_space(group.name.strip()))
        new_group_list_ui = appl.group.get_group_list()
        assert sorted(map(clean, new_group_list), key=appl.sorted_by_id) == sorted(new_group_list_ui, key=appl.sorted_by_id)
