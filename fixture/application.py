
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import sessionHelper
from fixture.group import groupHelper
from fixture.contact import contactHelper
from fixture.navigation import navigationHelper

class App:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = sessionHelper(self)
        self.group = groupHelper(self)
        self.contact = contactHelper(self)
        self.navigation = navigationHelper(self)

    def destroy(self):
            self.wd.quit()





