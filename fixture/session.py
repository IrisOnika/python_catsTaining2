
class sessionHelper:

    def __init__(self, App):
        self.app = App

    # login method
    def login(self, _login, _password):
        wd = self.app.wd
        self.app.navigation.openStartPage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(_login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(_password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[@type='submit']").click()

    # logout
    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()