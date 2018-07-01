
from selenium import webdriver
from fixture.session import sessionHelper
from fixture.group import groupHelper
from fixture.contact import contactHelper
from fixture.navigation import navigationHelper
from sys import maxsize
import re
import random
import string

class App:

    def __init__(self, browser, base_url):
       # self.wd = WebDriver(capabilities={"marionette": False})
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(2)
        self.session = sessionHelper(self)
        self.group = groupHelper(self)
        self.contact = contactHelper(self)
        self.navigation = navigationHelper(self)
        self.base_url = base_url

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

    def get_field_value(self, name):
        wd = self.wd
        return wd.find_element_by_name(name).get_attribute("value")


    def click_button(self, name):
        wd = self.wd
        wd.find_element_by_name(name).click()

    def sorted_by_id(self, entity):
        if entity.id:
            return int(entity.id)
        else:
            return maxsize

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def clear_dobble_space(self, s):
        return re.sub("  +", " ", s)

    def random_string(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits + " "*11
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

    def random_phone(self, prefix, maxlen):
        phone_symbols = string.digits + " "*2 + "(" + ")" + "-" + "+"
        return prefix + "".join([random.choice(phone_symbols) for i in range(random.randrange(maxlen))])

    def random_email(self, prefix, maxlen_n, maxlen_d):
        symbols = string.ascii_letters + string.digits
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen_n))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen_d))])

    def random_year(self):
        year_symbols = string.digits
        return "".join([random.choice(year_symbols) for i in range(4)])






