# -*- coding: utf-8 -*-
#import pytest
#from data.groups import test_data
from model.group import Group
import pytest


#@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(appl, db, check_ui, json_groups):                          #data_groups - fixture for file data/groups.py usage
    group=json_groups                                           #json_groups - fixture for test generator usage
    #old_group_list = appl.group.get_group_list()    #takes a list from ui
    with pytest.allure.step('Given a group list'):
        old_group_list = db.get_group_list()
        #print("old_group_list1 lenth = "+str(len(old_group_list1)))
    with pytest.allure.step('When I add a group %s to the list' % group):
        appl.group.create(group)
    with pytest.allure.step('Then a new group list is equal to the old list with an added group'):
   # assert len(old_group_list) + 1 == appl.group.count()        #is need only for uimatches (as heshing)
        new_group_list = db.get_group_list()
        old_group_list.append(group)
        assert old_group_list == new_group_list
    with pytest.allure.step('Then if %s is True do the same checks on ui' % check_ui):
        if check_ui:
            def clean(group):
                return Group(_id=group.id, _name=appl.clear_dobble_space(group.name.strip()))
            new_group_list_ui = appl.group.get_group_list()
            assert sorted(map(clean, new_group_list), key=appl.sorted_by_id) == sorted(new_group_list_ui, key=appl.sorted_by_id)




