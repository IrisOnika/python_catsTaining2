# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import App
import pytest


test_data = [Group(_name='',
                   _logo='',
                   _comment='')] + [
             Group(_name=App.random_string(App, 'Name', 11),
                   _logo=App.random_string(App, 'Logo', 22),
                   _comment=App.random_string(App, 'Comment', 44))
             for i in range(5)
             ]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(appl, group):
    old_group_list = appl.group.get_group_list()
    appl.group.create(group)
    assert len(old_group_list) + 1 == appl.group.count()
    new_group_list = appl.group.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=appl.sorted_by_id) == sorted(new_group_list, key=appl.sorted_by_id)




