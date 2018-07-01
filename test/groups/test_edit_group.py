# -*- coding: utf-8 -*-
from model.group import Group
import random

group_name = 'testName9_new'
group_logo = 'testLogo9_new'
group_comment = 'comment9_new'


def test_edit_group(appl, db, check_ui):
    if appl.group.count()==0:
        appl.group.create(Group(_name="test"))
    old_group_list = db.get_group_list()
    group = random.choice(old_group_list)
    edited_group = Group(_name=group_name, _logo=group_logo, _comment=group_comment, _id=group.id)
    appl.group.edit_by_id(edited_group, group.id)
    new_group_list = db.get_group_list()
    old_group_list.remove(group)
    old_group_list.append(edited_group)
    assert sorted(old_group_list, key=appl.sorted_by_id) == new_group_list
    if check_ui:
        def clean(group):
            return Group(_id=group.id, _name=appl.clear_dobble_space(group.name.strip()))
        new_group_list_ui = appl.group.get_group_list()
        assert sorted(map(clean, new_group_list), key=appl.sorted_by_id) == sorted(new_group_list_ui, key=appl.sorted_by_id)