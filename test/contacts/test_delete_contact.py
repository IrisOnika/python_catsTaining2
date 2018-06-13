# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(appl):
    appl.contact.delete()