from model.contact import Contact
import random
import string
from model.group import Group


def test_add_contact_to_group(orm):
    #print()
    group_list = orm.orm_get_group_list
    print(len(group_list))


#    def group_and_contact():
#        group_list = orm.orm_get_group_list
#        if len(group_list) == 0:
#            appl.group.create(Group(_name="test"))
#        for g in group_list:
#            contacts=orm.get_contacts_out_of_group(g) #get group having contacts out of it
#            if len(contacts) > 0:
#                group = g
#                contact = random.choice(contacts)
#                return group, contact
#            else:
#                pass
#        f_name = "testfirst44" + "".join([random.choice(string.digits) for i in 7])
#        l_name = "testlast44" + "".join([random.choice(string.digits) for i in 4])
#        contact = Contact(_firstname=f_name, _lastname=l_name)
#        appl.contact.create(contact)
#        group=random.choice(group_list)
#        return group, contact
#    group = group_and_contact().group
#    contact = group_and_contact().contact

#    print(group.name)
#    print(contact.firstname)







#    if appl.contact.count()==0:
#        appl.contact.create(Contact(_firstname="test"))