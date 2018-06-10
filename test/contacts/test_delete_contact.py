# -*- coding: utf-8 -*-
from model.contact import Contact

login ='admin'
password ='secret'


def test_add_contact(appl):
    appl.session.login(login, password)
    appl.contact.delete()
    appl.session.logout()