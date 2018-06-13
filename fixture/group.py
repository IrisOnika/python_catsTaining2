
class groupHelper:
    def __init__(self, App):
        self.app = App

    # GROUP
    # create group method
    def create(self, Group):
        self.app.navigation.openMenu("groups")
        self.app.click_button("new")
        self.set_group_fields(Group)
        self.app.click_button("submit")
        self.app.navigation.openMenu("groups")

    # edit group method
    def edit(self, Group):
        self.app.navigation.openMenu("groups")
        self.select_first_group()                   # self.select_group()
        self.app.click_button("edit")
        self.set_group_fields(Group)
        self.app.click_button("update")
        self.app.navigation.openMenu("groups")

    # delete group method
    def delete(self):
        self.app.navigation.openMenu("groups")
        self.select_first_group()                   # self.select_group()
        self.app.click_button("delete")
        self.app.navigation.openMenu("groups")

    # -''-
    def set_group_fields(self, Group):
        self.app.set_text_field("group_name", Group.name)
        self.app.set_text_field("group_header", Group.logo)
        self.app.set_text_field("group_footer", Group.comment)

    # -''-
    def select_first_group(self):
        wd = self.app.wd
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()