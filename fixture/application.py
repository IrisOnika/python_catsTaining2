
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import sessionHelper
from fixture.group import groupHelper
from fixture.contact import contactHelper

class App:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = sessionHelper(self)
        self.group = groupHelper(self)
        self.contact = contactHelper(self)


    def openStartPage(self):
        wd = self.wd
        wd.get("http://127.0.0.1/addressbook/")


    def openMenu(self, _tab):
        wd = self.wd
        wd.find_element_by_link_text(_tab).click()



    def destroy(self):
            self.wd.quit()





