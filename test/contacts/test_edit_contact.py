# -*- coding: utf-8 -*-
from model.contact import Contact

first_name = '!!test_firstname1_new!!'
middle_name = 'test_middlename1_new'
last_name = '!!test_lastname1_new!!'
nick_name = 'kotik'
title = 'test_title1_new'
company = 'test_company1_new'
address = '!!test_address1_new!!'
tel_home = '!!777345!!'
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


def test_add_contact(appl):
    if appl.contact.count()==0:
        appl.contact.create(Contact(_firstname="test"))
    appl.contact.edit(Contact(_firstname=first_name,
                              _lastname=last_name,
                              _address=address,
                              _thome=tel_home,
                              _email=email))