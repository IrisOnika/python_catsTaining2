from model.contact import Contact
from random import randrange
import pytest


def test_verify_contact_from_list(appl):
    with pytest.allure.step('Presteps. Create a contact if no one exists'):
        if appl.contact.count()==0:
            appl.contact.create(Contact(_firstname="test"))
    index = randrange(len(appl.contact.get_contact_list()))
    print('index=' + str(index))
    with pytest.allure.step('Given contact data from a list'):
        contact_data_from_list = appl.contact.get_contact_list()[index]
    with pytest.allure.step('Given contact data from contact form'):
        contact_data_from_edit_form = appl.contact.get_edit_form_data_for_home_page(index=index + 1)
    with pytest.allure.step("Then contact's data fron the list %s and from contact form %s is equal" % (contact_data_from_list, contact_data_from_edit_form)):
        assert contact_data_from_list == contact_data_from_edit_form