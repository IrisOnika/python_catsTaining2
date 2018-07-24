# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import pytest


def test_delete_contact(appl, db, check_ui):
    with pytest.allure.step('Prestets. Create a contact if no one exists'):
        if appl.contact.count()==0:
            appl.contact.create(Contact(_firstname="test"))
    with pytest.allure.step('Given a contact list'):
        old_contact_list = db.get_contact_list()
    #index = randrange(len(old_contact_list))
    #appl.contact.delete(index)
    #assert len(old_contact_list) - 1 == appl.contact.count()

    with pytest.allure.step('Given a contact'):
        contact = random.choice(old_contact_list)
    with pytest.allure.step('When I delete contact %s' % contact):
        appl.contact.delete_by_id(contact.id)
    with pytest.allure.step('Then a new contact list is equal to the old contact list with vo deleted contact'):
        new_contact_list = db.get_contact_list()
        #old_contact_list[index-1:index] = []
        old_contact_list.remove(contact)
        assert old_contact_list == new_contact_list
    with pytest.allure.step('Then if %s is True do the same checks on ui' % check_ui):
        if check_ui:
            def clean(contact):
                return Contact(_id=contact.id,
                               _firstname=appl.clear_dobble_space(contact.firstname.strip()),
                               _lastname=appl.clear_dobble_space(contact.lastname.strip()),
                               _address=appl.clear_dobble_space(contact.address.strip()),
                               _all_phones=contact.all_phones,
                               _all_emails=contact.all_emails
                               )
            new_contact_list_ui = appl.contact.get_contact_list()
            assert sorted(map(clean, new_contact_list), key=appl.sorted_by_id) == sorted(new_contact_list_ui, key=appl.sorted_by_id)