# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_group(appl):
    if appl.group.count()==0:
        appl.group.create(Group(_name="test"))
    appl.group.delete()
