# -*- coding: utf-8 -*-
from model.contact import Contact

first_name = 'test_firstname2'
middle_name = 'test_middlename2'
last_name = 'test_lastname2'
nick_name = 'kotik'
title = 'test_title2'
company = 'test_company2'
address = 'test_address2'
tel_home = '777345'
tel_mobile = '777098'
tel_work = '777321'
tel_fax = '777'
email = 'test_mylo@test.test'
email2 = 'test_mylo2@test.test'
email3 = 'test_mylo3@test.test'
homepage = 'https://test.page'
byear = '1988'
ayear = '1998'
address2 = 'test_address2'
phone2 = '777000'
note = 'test_note'


def test_add_contact(appl):
    old_contact_list = appl.contact.get_contact_list()
    appl.contact.create(Contact(first_name,
                                middle_name,
                                last_name,
                                nick_name,
                                title,
                                company,
                                address,
                                tel_home,
                                tel_mobile,
                                tel_work,
                                tel_fax,
                                email,
                                email2,
                                email3,
                                homepage,
                                byear,
                                ayear,
                                address2,
                                phone2,
                                note))
    new_contact_list = appl.contact.get_contact_list()
    assert len(old_contact_list) + 1 == len(new_contact_list)