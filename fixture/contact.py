from model.contact import Contact


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
        # need to add check opened page here
        self.open_contacts_page()
        self.contact_list_actions("Edit", index)  # self.first_contact_list_actions("Edit")
        self.set_contact_fields(Contact)
        self.contact_actions("Update", 2)
        self.app.navigation.openMenu("home")
        self.contactListCache = None

    # delete contact method
    def delete(self, index):
        # need to add check opened page here
        # need to make xpath depended of contact name
        self.open_contacts_page()
        self.contact_list_actions("Edit", index)        #self.first_contact_list_actions("Edit")
        self.contact_actions("Delete")
        self.app.navigation.openMenu("home")
        self.contactListCache = None

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
        print(_index)
        wd.find_element_by_xpath("//tr[@name='entry'][" + str(_index) + "]//a[img[@title='" + action + "']]").click()

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
                id = i.find_element_by_xpath("td[1]/input").get_attribute("value")
                self.contactListCache.append(Contact(_firstname=first_name, _lastname=last_name, _address=address, _id=id))
        return list(self.contactListCache)