# -*- coding: utf-8 -*-
from model.group import Group

group_name = '!!testName1_new!!'
group_logo = 'testLogo1_new'
group_comment = '!!comment1_new!!'


def test_add_group(appl):
    appl.group.edit(Group(_name = group_name, _comment = group_comment))