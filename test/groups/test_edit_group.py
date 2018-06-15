# -*- coding: utf-8 -*-
from model.group import Group

group_name = '!!testName1_new!!'
group_logo = 'testLogo1_new'
group_comment = '!!comment1_new!!'


def test_add_group(appl):
    if appl.group.count()==0:
        appl.group.create(Group(_name="test"))
    old_group_list = appl.group.get_group_list()
    appl.group.edit(Group(_name = group_name, _comment = group_comment))
    new_group_list = appl.group.get_group_list()
    assert len(old_group_list) == len(new_group_list)