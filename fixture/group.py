from model.group import Group

class groupHelper:
    def __init__(self, App):
        self.app = App

    # GROUP
    # create group method
    def create(self, Group):
        self.open_groups_page()
        self.app.click_button("new")
        self.set_group_fields(Group)
        self.app.click_button("submit")
        self.app.navigation.openMenu("groups")
        self.groupListCache = None

    # edit group method
    def edit(self, Group, index):
        self.open_groups_page()
        self.select_group(index)           #self.select_first_group()
        self.app.click_button("edit")
        self.set_group_fields(Group)
        self.app.click_button("update")
        self.app.navigation.openMenu("groups")
        self.groupListCache = None

    def edit_by_id(self, Group, id):
        self.open_groups_page()
        self.select_group_by_id(id)           #self.select_first_group()
        self.app.click_button("edit")
        self.set_group_fields(Group)
        self.app.click_button("update")
        self.app.navigation.openMenu("groups")
        self.groupListCache = None

    # delete group method
    def delete(self, index):
        self.open_groups_page()
        self.select_group(index)           #self.select_first_group()
        self.app.click_button("delete")
        self.app.navigation.openMenu("groups")
        self.groupListCache = None

    def delete_group_by_id(self, id):
        self.open_groups_page()
        self.select_group_by_id(id)  # self.select_first_group()
        self.app.click_button("delete")
        self.app.navigation.openMenu("groups")
        self.groupListCache = None

    #-''-
    def open_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0:
            return
        self.app.navigation.openMenu("groups")

    # -''-
    def set_group_fields(self, Group):
        self.app.set_text_field("group_name", Group.name)
        self.app.set_text_field("group_header", Group.logo)
        self.app.set_text_field("group_footer", Group.comment)

    # -''-
    def select_first_group(self):
        self.select_group(0)

    def select_group(self, index):
        wd = self.app.wd
        if not wd.find_elements_by_name("selected[]")[index].is_selected():
            wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        if not wd.find_element_by_css_selector("input[value='%s']" % id).is_selected():
            wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def count(self):
        wd = self.app.wd
        self.app.navigation.openMenu("groups")
        return len(wd.find_elements_by_name("selected[]"))

    groupListCache = None

    def get_group_list(self):
        if self.groupListCache is None:
            wd = self.app.wd
            self.app.navigation.openMenu("groups")
            self.groupListCache = []
            for i in wd.find_elements_by_css_selector("span.group"):
                name = i.text
                id = i.find_element_by_name("selected[]").get_attribute("value")
                self.groupListCache.append(Group(_name=name, _id=id))
        return list(self.groupListCache)