
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

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
            self.wd.quit()

    def set_text_field(self, name, value):
        wd = self.wd
        if not value==None:
            wd.find_element_by_name(name).click()
            wd.find_element_by_name(name).clear()
            wd.find_element_by_name(name).send_keys(value)

    def click_button(self, name):
        wd = self.wd
        wd.find_element_by_name(name).click()





