
class sessionHelper:

    def __init__(self, App):
        self.app = App

    # login method
    def login(self, _login, _password):
        wd = self.app.wd
        self.app.navigation.openStartPage()
        self.app.set_text_field("user", _login)
        self.app.set_text_field("pass", _password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[@type='submit']").click()

    # logout
    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()