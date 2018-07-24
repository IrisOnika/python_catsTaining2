# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest


group_name = 'testName9_new'
group_logo = 'testLogo9_new'
group_comment = 'comment9_new'


def test_edit_group(appl, db, check_ui):
    with pytest.allure.step('Presteps. Create a group if no one exists'):
        if appl.group.count()==0:
            appl.group.create(Group(_name="test"))
    with pytest.allure.step('Given a groups list'):
        old_group_list = db.get_group_list()
    with pytest.allure.step('Given a group to be edited'):
        group = random.choice(old_group_list)
    with pytest.allure.step('When I edit a group %s' % group):
        edited_group = Group(_name=group_name, _logo=group_logo, _comment=group_comment, _id=group.id)
        appl.group.edit_by_id(edited_group, group.id)
    with pytest.allure.step('Then a new group list is equal to old group list with %s instead of %s' % (edited_group, group)):
        new_group_list = db.get_group_list()
        old_group_list.remove(group)
        old_group_list.append(edited_group)
        assert sorted(old_group_list, key=appl.sorted_by_id) == new_group_list
    with pytest.allure.step('Then if %s is True do the same checks on ui' % check_ui):
        if check_ui:
            def clean(group):
                return Group(_id=group.id, _name=appl.clear_dobble_space(group.name.strip()))
            new_group_list_ui = appl.group.get_group_list()
            assert sorted(map(clean, new_group_list), key=appl.sorted_by_id) == sorted(new_group_list_ui, key=appl.sorted_by_id)