from model.contact import Contact
from random import randrange


def test_verify_contact_from_list(appl):
    if appl.contact.count()==0:
        appl.contact.create(Contact(_firstname="test"))
    index = randrange(len(appl.contact.get_contact_list()))
    print('index=' + str(index))
    contact_data_from_list = appl.contact.get_contact_list()[index]
    contact_data_from_eidt_form = appl.contact.get_edit_form_data_for_home_page(index=index + 1)
    assert contact_data_from_list == contact_data_from_eidt_form