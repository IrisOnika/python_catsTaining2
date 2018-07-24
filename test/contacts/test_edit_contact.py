# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import pytest


first_name = 'test_firstname7_new'
middle_name = 'test_middlename7_new'
last_name = 'test_lastname7_new'
nick_name = 'kotik'
title = 'test_title1_new'
company = 'test_company7_new'
address = 'test_address7_new'
tel_home = '777345'
tel_mobile = '777098'
tel_work = '777321'
tel_fax = '777'
email = '!!test_mylo@test.test.new!!'
email2 = 'test_mylo2@test.test.new'
email3 = 'test_mylo3@test.test.new'
homepage = 'https://test.page.new'
byear = '1988'
ayear = '1998'
address2 = 'test_address1_new'
phone2 = '777000'
note = 'test_note1_new'


def test_edit_contact(appl, db, check_ui):
    with pytest.allure.step('Presteps. Create a contact if no one exists'):
        if appl.contact.count()==0:
            appl.contact.create(Contact(_firstname="test"))
    with pytest.allure.step('Given a contact list'):
        old_contact_list = db.get_contact_list()
    with pytest.allure.step('Given a contact to be edited'):
        contact = random.choice(old_contact_list)
    with pytest.allure.step('When I edit a contact %s' % contact):
        edited_contact = Contact(_id=contact.id,
                             _firstname=first_name,
                             _lastname=last_name,
                             _address=address,
                             _thome=tel_home,
                             _email=email)
        appl.contact.edit_by_id(edited_contact, contact.id)
    with pytest.allure.step('Then a new contact list is equal to old contact list with %s instead of %s' % (edited_contact, contact)):
        new_contact_list = db.get_contact_list()
        old_contact_list.remove(contact)
        old_contact_list.append(edited_contact)
        assert sorted(old_contact_list, key=appl.sorted_by_id) == new_contact_list
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