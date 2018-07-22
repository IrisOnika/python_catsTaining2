from model.contact import Contact
import time

class contactHelper:
    def __init__(self, App):
        self.app = App

    # CONTACT
    # create contact method
    def create(self, Contact):
        self.app.navigation.openMenu("add new")
        self.set_contact_fields(Contact)
        self.contact_actions("Enter", 2)
        self.app.navigation.openMenu("home")
        self.contactListCache = None

    # edit contact method
    def edit(self, Contact, index):
        self.open_contacts_page()
        self.contact_list_actions("Edit", index)  # self.first_contact_list_actions("Edit")
        self.set_contact_fields(Contact)
        self.contact_actions("Update", 2)
        self.app.navigation.openMenu("home")
        self.contactListCache = None

    def edit_by_id(self, Contact, id):
        self.open_contacts_page()
        self.contact_list_action_edit_by_id(id)  # self.first_contact_list_actions("Edit")
        self.set_contact_fields(Contact)
        self.contact_actions("Update", 2)
        self.app.navigation.openMenu("home")
        self.contactListCache = None

    # delete contact method
    def delete(self, index):
        # need to make xpath depended of contact name
        self.open_contacts_page()
        self.contact_list_actions("Edit", index)        #self.first_contact_list_actions("Edit")
        self.contact_actions("Delete")
        self.app.navigation.openMenu("home")
        self.contactListCache = None

    def delete_by_id(self, id):
        # need to make xpath depended of contact name
        self.open_contacts_page()
        self.contact_list_action_edit_by_id(id)  # self.first_contact_list_actions("Edit")
        self.contact_actions("Delete")
        self.app.navigation.openMenu("home")
        self.contactListCache = None

    def get_edit_form_data_for_home_page(self, index):
        self.open_contacts_page()
        self.contact_list_actions("Edit", index)
        firstname = self.app.get_field_value("firstname")
        lastname = self.app.get_field_value("lastname")
        address = self.app.get_field_value("address")
        thome = self.app.get_field_value("home")
        tmobile = self.app.get_field_value("mobile")
        twork = self.app.get_field_value("work")
        phone2 = self.app.get_field_value("phone2")
        all_phones = "\n".join(filter(lambda x: x!="",
                                      (map(lambda x: self.app.clear(x),
                                           filter(lambda x: x is not None,
                                                  [thome, tmobile, twork, phone2])))))
        email = self.app.get_field_value("email")
        email2 = self.app.get_field_value("email2")
        email3 = self.app.get_field_value("email3")
        all_emails = "\n".join(filter(lambda x: x != "",
                                        filter(lambda x: x is not None,
                                               [email, email2, email3])))
        id = self.app.get_field_value("id")
        self.app.navigation.openMenu("home")
        return Contact(_firstname=firstname,
                       _lastname=lastname,
                       _address=address,
                       _all_phones=all_phones,
                       _all_emails=all_emails,
                       _id=id)

    #-''-
    def open_contacts_page(self):
        self.app.navigation.openStartPage()

    #-''-
    def set_contact_fields(self, Contact):
        self.app.set_text_field("firstname", Contact.firstname)
        self.app.set_text_field("middlename", Contact.middlename)
        self.app.set_text_field("lastname", Contact.lastname)
        self.app.set_text_field("nickname", Contact.nickname)
        self.app.set_text_field("title", Contact.title)
        self.app.set_text_field("company", Contact.company)
        self.app.set_text_field("address", Contact.address)
        # phones
        self.app.set_text_field("home", Contact.thome)
        self.app.set_text_field("mobile", Contact.tmobile)
        self.app.set_text_field("work", Contact.twork)
        self.app.set_text_field("fax", Contact.tfax)
        #----
        self.app.set_text_field("email", Contact.email)
        self.app.set_text_field("email2", Contact.email2)
        self.app.set_text_field("email3", Contact.email3)
        self.app.set_text_field("homepage", Contact.homepage)
        #    if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
        #        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        #    if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
        #        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        self.app.set_text_field("byear", Contact.byear)
        #    if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").is_selected():
        #        wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[4]").click()
        #    if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").is_selected():
        #        wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[3]").click()
        self.app.set_text_field("ayear", Contact.ayear)
        self.app.set_text_field("address2", Contact.address2)
        self.app.set_text_field("phone2", Contact.phone2)
        self.app.set_text_field("notes", Contact.notes)

    #-''-
    def first_contact_list_actions(self, action):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[img[@title='" + action + "']]").click()

    def contact_list_actions(self, action, _index):
        wd = self.app.wd
        #print(_index)
        wd.find_element_by_xpath("//tr[@name='entry'][" + str(_index) + "]//a[img[@title='" + action + "']]").click()

    def contact_list_action_edit_by_id(self, id):
        wd = self.app.wd
        # print(_index)
        wd.find_element_by_xpath("//a[@href='edit.php?id=" + id + "']").click()

    def contact_actions(self, action, index=1):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']//input[@value='" + action + "'][" + str(index) + "]").click()

    def count(self):
        wd = self.app.wd
        self.app.navigation.openMenu("home")
        return len(wd.find_elements_by_name("entry"))

    contactListCache = None

    def get_contact_list(self):
        if self.contactListCache is None:
            wd = self.app.wd
            self.app.navigation.openMenu("home")
            self.contactListCache=[]
            for i in wd.find_elements_by_name("entry"):
                first_name = i.find_element_by_xpath("td[3]").text
                last_name = i.find_element_by_xpath("td[2]").text
                address = i.find_element_by_xpath("td[4]").text
                emails = i.find_element_by_xpath("td[5]").text
                phones = i.find_element_by_xpath("td[6]").text
                id = i.find_element_by_xpath("td[1]/input").get_attribute("value")
                self.contactListCache.append(Contact(_firstname=first_name,
                                                     _lastname=last_name,
                                                     _address=address,
                                                     _all_emails=emails,
                                                     _all_phones=phones,
                                                     _id=id))
        return list(self.contactListCache)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//input[@value='" + id + "']").is_selected():
            wd.find_element_by_xpath("//input[@value='" + id + "']").click()

    def add_contact_to_group(self, c, g):
        wd = self.app.wd
        self.app.navigation.openMenu("home")
        self.select_contact_by_id(c.id)
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='" + str(g.id) + "']").click()
        wd.find_element_by_name("add").click()

    def open_group_contacts_list_by_url(self, g):
        wd = self.app.wd
        if wd.current_url.endswith("?group=%s" % str(g.id)) and len(wd.find_elements_by_name("remove")) > 0:
            return
        wd.get(self.app.base_url + "?group=%s" % str(g.id))

    def open_group_contacts_list_by_select(self, g):
        wd = self.app.wd
        if wd.current_url.endswith("?group=%s" % str(g.id)) and len(wd.find_elements_by_name("remove")) > 0:
            return
        self.app.navigation.openMenu("home")
        wd.find_element_by_xpath("//select[@name='group']/option[@value='" + str(g.id) + "']").click()

    def delete_contact_from_group(self, c, g):
        wd = self.app.wd
        self.open_group_contacts_list_by_url(g)
        print(c.id)
        self.select_contact_by_id(c.id)
        wd.find_element_by_name("remove").click()



