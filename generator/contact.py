from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:    #o - is a name of option; a - is its option value
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 11
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(prefix, maxlen):
    phone_symbols = string.digits + " "*2 + "(" + ")" + "-" + "+"
    return prefix + "".join([random.choice(phone_symbols) for i in range(random.randrange(maxlen))])

def random_email(prefix, maxlen_n, maxlen_d):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen_n))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen_d))])

def random_year():
    year_symbols = string.digits
    return "".join([random.choice(year_symbols) for i in range(4)])


test_data = [Contact(_firstname='',
                     _middlename='',
                     _lastname='',
                     _nickname='',
                     _title='',
                     _company='',
                     _address='',
                     _thome='',
                     _tmobile='',
                     _twork='',
                     _tfax='',
                     _email='',
                     _email2='',
                     _email3='',
                     _homepage='',
                     _byear='',
                     _ayear='',
                     _address2='',
                     _phone2='',
                     _notes=''
                     )] + [
             Contact(_firstname=random_string('firstname', 7),
                     _middlename=random_string('middlename', 4),
                     _lastname=random_string('lastname', 7),
                     _nickname=random_string('nickname', 9),
                     _title=random_string('title', 11),
                     _company=random_string('company', 9),
                     _address=random_string('address', 44),
                     _thome=random_phone('home phone', 11),
                     _tmobile=random_phone('mobile phone', 11),
                     _twork=random_phone('work phone', 11),
                     _tfax=random_phone('fax', 9),
                     _email=random_email('email', 7, 7),
                     _email2=random_email('email2', 7, 7),
                     _email3=random_email('email3', 7, 7),
                     _homepage=random_string('homepage', 18),
                     _byear=random_year(),
                     _ayear=random_year(),
                     _address2=random_string('secondary address', 44),
                     _phone2=random_phone('secondary phone', 11),
                     _notes=random_string('notes', 77)
                    )
                    for i in range(n)
             ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as f_data:
    jsonpickle.set_encoder_options("json", indent=2)
    f_data.write(jsonpickle.encode(test_data))