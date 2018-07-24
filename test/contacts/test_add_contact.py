# -*- coding: utf-8 -*-
#import pytest
#from data.contacts import test_data
from model.contact import Contact
import pytest


#@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(appl, db, check_ui, json_contacts):                                                #fixture contact - just contacts discribed in test_data from data/contact.py
    new_contact = json_contacts                                                             #used with @pytest.mark.parametrize
    with pytest.allure.step('Given a contacts list'):
        old_contact_list = db.get_contact_list()
    with pytest.allure.step('When I create a contact %s' % new_contact):
        appl.contact.create(new_contact)
    with pytest.allure.step('Then a new contact list is equal to the old list with an added contact'):
        # assert len(old_contact_list) + 1 == appl.contact.count()
        new_contact_list = db.get_contact_list()
        old_contact_list.append(new_contact)
        assert sorted(old_contact_list, key=appl.sorted_by_id) == sorted(new_contact_list, key=appl.sorted_by_id)
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