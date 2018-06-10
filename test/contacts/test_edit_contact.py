# -*- coding: utf-8 -*-
from model.contact import Contact

login ='admin'
password ='secret'
first_name = 'test_firstname1_new'
middle_name = 'test_middlename1_new'
last_name = 'test_lastname1_new'
nick_name = 'kotik'
title = 'test_title1_new'
company = 'test_company1_new'
address = 'test_address1_new'
tel_home = '777345'
tel_mobile = '777098'
tel_work = '777321'
tel_fax = '777'
email = 'test_mylo@test.test.new'
email2 = 'test_mylo2@test.test.new'
email3 = 'test_mylo3@test.test.new'
homepage = 'https://test.page.new'
byear = '1988'
ayear = '1998'
address2 = 'test_address1_new'
phone2 = '777000'
note = 'test_note1_new'


def test_add_contact(appl):
    appl.session.login(login, password)
    appl.contact.edit(Contact(first_name, middle_name,
                               last_name, nick_name,
                               title, company,
                               address, tel_home,
                               tel_mobile, tel_work,
                               tel_fax, email,
                               email2, email3,
                               homepage, byear,
                               ayear, address2,
                               phone2, note))
    appl.session.logout()