# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_add_contact(appl):
    if appl.contact.count()==0:
        appl.contact.create(Contact(_firstname="test"))
    old_contact_list = appl.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    appl.contact.delete(index)
    assert len(old_contact_list) - 1 == appl.contact.count()
    new_contact_list = appl.contact.get_contact_list()
    old_contact_list[index-1:index] = []
    assert sorted(old_contact_list, key=appl.sorted_by_id) == sorted(new_contact_list, key=appl.sorted_by_id)