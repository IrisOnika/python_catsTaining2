# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(appl):
    if appl.contact.count()==0:
        appl.contact.create(Contact(_firstname="test"))
    appl.contact.delete()