# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(appl):
    appl.group.delete()
