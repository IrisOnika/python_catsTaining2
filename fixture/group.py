
class groupHelper:
    def __init__(self, App):
        self.app = App

    # GROUP
    # create group method
    def create(self, Group):
        wd = self.app.wd
        self.app.navigation.openMenu("groups")
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.logo)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.comment)
        wd.find_element_by_name("submit").click()
        self.app.navigation.openMenu("groups")