

class navigationHelper:
    def __init__(self, App):
        self.app = App

    def openStartPage(self):
        wd = self.app.wd
        wd.get("http://127.0.0.1/addressbook/")

    def openMenu(self, _tab):
        wd = self.app.wd
        wd.find_element_by_link_text(_tab).click()