# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import App
import pytest

test_data = [Contact(_firstname='',
                     _middlename='',
                     _lastname='',
                     _nickname='',
                     _title='',
                     _company='',
                     _address='',
                     _thome='',
                     _tmobile='',
                     _twork='',
                     _tfax='',
                     _email='',
                     _email2='',
                     _email3='',
                     _homepage='',
                     _byear='',
                     _ayear='',
                     _address2='',
                     _phone2='',
                     _notes=''
                     )] + [
             Contact(_firstname=App.random_string(App, 'firstname', 7),
                     _middlename=App.random_string(App, 'middlename', 4),
                     _lastname=App.random_string(App, 'lastname', 7),
                     _nickname=App.random_string(App, 'nickname', 9),
                     _title=App.random_string(App, 'title', 11),
                     _company=App.random_string(App, 'company', 9),
                     _address=App.random_string(App, 'address', 44),
                     _thome=App.random_phone(App, 'home phone', 11),
                     _tmobile=App.random_phone(App, 'mobile phone', 11),
                     _twork=App.random_phone(App, 'work phone', 11),
                     _tfax=App.random_phone(App, 'fax', 9),
                     _email=App.random_email(App, 'email', 7, 7),
                     _email2=App.random_email(App, 'email2', 7, 7),
                     _email3=App.random_email(App, 'email3', 7, 7),
                     _homepage=App.random_string(App, 'homepage', 18),
                     _byear=App.random_year(App),
                     _ayear=App.random_year(App),
                     _address2=App.random_string(App, 'secondary address', 44),
                     _phone2=App.random_phone(App, 'secondary phone', 11),
                     _notes=App.random_string(App, 'notes', 77)
                    )
                    for i in range(2)
             ]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(appl, contact):
    new_contact = contact
    old_contact_list = appl.contact.get_contact_list()
    appl.contact.create(new_contact)
    assert len(old_contact_list) + 1 == appl.contact.count()
    new_contact_list = appl.contact.get_contact_list()
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=appl.sorted_by_id) == sorted(new_contact_list, key=appl.sorted_by_id)