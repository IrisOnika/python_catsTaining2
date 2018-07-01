from model.group import Group
import random
import string
import os.path
#import json
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/groups1.json"

for o, a in opts:    #o - is a name of option; a - is its option value
    if o == '-n':
        n = int(a)   # if option is number of groups - convert it to int
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 11
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(_name='4',
                   _logo='4',
                   _comment='4')] + [
             Group(_name=random_string('Name', 11),
                   _logo=random_string('Logo', 22),
                   _comment=random_string('Comment', 44))
             for i in range(n)
             ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as f_data:
    #f_data.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    f_data.write(jsonpickle.encode(test_data))
