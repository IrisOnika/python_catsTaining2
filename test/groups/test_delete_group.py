# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest


def test_delete_group(appl, db, check_ui):
    with pytest.allure.step('Prestets. Create a group if no one exists'):
        if appl.group.count()==0:
            appl.group.create(Group(_name="test"))
    with pytest.allure.step('Given an group list'):
        old_group_list = db.get_group_list()
    with pytest.allure.step('Given a group'):
        group = random.choice(old_group_list)
    with pytest.allure.step('When I delete a group %s' % group):
        appl.group.delete_group_by_id(group.id)
    with pytest.allure.step('Then a new group list is equal to old group list with no deleted group'):
        new_group_list = db.get_group_list()
        old_group_list.remove(group)
        assert sorted(old_group_list, key=appl.sorted_by_id) == sorted(new_group_list, key=appl.sorted_by_id)
    with pytest.allure.step('Then if %s is True do the same checks on ui' % check_ui):
        if check_ui:
            def clean(group):
                return Group(_id=group.id, _name=appl.clear_dobble_space(group.name.strip()))
            new_group_list_ui = appl.group.get_group_list()
            assert sorted(map(clean, new_group_list), key=appl.sorted_by_id) == sorted(new_group_list_ui, key=appl.sorted_by_id)
