from model.contact import Contact
import random
import string
from model.group import Group
import pytest


def test_add_contact_to_group(appl, orm):
    group = []
    contact = []
    with pytest.allure.step('Given an old contacts list'):
        group_list = orm.orm_get_group_list()
    with pytest.allure.step('Presteps. Create contact and/or group and/or delete contact from the group if it is needed'):
        if len(group_list) == 0:
            g_name = "test" + "".join([random.choice(string.digits) for i in range(4)])
            appl.group.create(Group(_name=g_name))
        for g in group_list:
            contacts = orm.get_contacts_out_of_group(g) # get group having contacts out of it
            if len(contacts) > 0:
                if group == []:
                    group.append(g)
                if contact == []:
                    contact.append(random.choice(contacts))
    with pytest.allure.step('Given a group and contact'):
        if group != []:
            gr = group[0]
            cont = contact[0]
        else:
            appl.contact.create(Contact(_firstname="testfirst44" + "".join([random.choice(string.digits) for i in range(7)]),
                                        _lastname="testlast44" + "".join([random.choice(string.digits) for i in range(4)])))
            gr = random.choice(orm.orm_get_group_list())
            cont = orm.get_contacts_out_of_group(gr)[0]

    with pytest.allure.step('When I add the contact %s to the group %s' % (cont, gr)):
        appl.contact.add_contact_to_group(cont, gr)
    with pytest.allure.step('Then verify that contact %s is displaying in the group %s' % (cont, gr)):
        is_in_group = False
        for c in orm.get_contacts_in_group(gr):
            if c.firstname == cont.firstname:
                is_in_group = True
        assert is_in_group













