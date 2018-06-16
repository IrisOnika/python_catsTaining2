# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(appl):
    if appl.contact.count()==0:
        appl.contact.create(Contact(_firstname="test"))
    old_contact_list = appl.contact.get_contact_list()
    appl.contact.delete()
    new_contact_list = appl.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)
    old_contact_list[0:1] = []
    assert old_contact_list == new_contact_list