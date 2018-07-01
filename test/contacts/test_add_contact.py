# -*- coding: utf-8 -*-
#import pytest
#from data.contacts import test_data
from model.contact import Contact


#@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(appl, db, check_ui, json_contacts):                                                #fixture contact - just contacts discribed in test_data from data/contact.py
    new_contact = json_contacts                                                             #used with @pytest.mark.parametrize
    old_contact_list = db.get_contact_list()
    appl.contact.create(new_contact)
    assert len(old_contact_list) + 1 == appl.contact.count()
    new_contact_list = db.get_contact_list()
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=appl.sorted_by_id) == sorted(new_contact_list, key=appl.sorted_by_id)
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