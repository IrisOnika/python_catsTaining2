

class navigationHelper:
    def __init__(self, App):
        self.app = App

    def openStartPage(self, isLogin=True):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/"):
            if isLogin:
                if len(wd.find_elements_by_name("MainForm"))>0:
                    return
            else:
                if len(wd.find_elements_by_name("LoginForm"))>0:
                    return
        wd.get("http://127.0.0.1/addressbook/")

    def openMenu(self, _tab):
        wd = self.app.wd
        wd.find_element_by_link_text(_tab).click()