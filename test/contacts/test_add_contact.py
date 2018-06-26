# -*- coding: utf-8 -*-
import pytest
from data.contacts import test_data


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(appl, contact):
    new_contact = contact
    old_contact_list = appl.contact.get_contact_list()
    appl.contact.create(new_contact)
    assert len(old_contact_list) + 1 == appl.contact.count()
    new_contact_list = appl.contact.get_contact_list()
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=appl.sorted_by_id) == sorted(new_contact_list, key=appl.sorted_by_id)