
from selenium.webdriver.firefox.webdriver import WebDriver

class App:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    #login method
    def login(self, _login, _password):
        wd = self.wd
        self.openStartPage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(_login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(_password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[@type='submit']").click()

    def openStartPage(self):
        wd = self.wd
        wd.get("http://127.0.0.1/addressbook/")

    def openMenu(self, _tab):
        wd = self.wd
        wd.find_element_by_link_text(_tab).click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
            self.wd.quit()

    #create group method
    def groupForm(self, Group):
        wd = self.wd
        menu_tab = "groups"
        self.openMenu(_tab=menu_tab)
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
        self.openMenu(_tab=menu_tab)