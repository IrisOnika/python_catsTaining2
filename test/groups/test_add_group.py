# -*- coding: utf-8 -*-
import pytest
from data.groups import test_data


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(appl, group):
    old_group_list = appl.group.get_group_list()
    appl.group.create(group)
    assert len(old_group_list) + 1 == appl.group.count()
    new_group_list = appl.group.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=appl.sorted_by_id) == sorted(new_group_list, key=appl.sorted_by_id)




