
from model.group import Group
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 11
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [Group(_name='',
                   _logo='',
                   _comment='')] + [
             Group(_name=random_string('Name', 11),
                   _logo=random_string('Logo', 22),
                   _comment=random_string('Comment', 44))
             for i in range(5)
             ]


for_edit_data = [Group(_name='testName1_new',
                       _logo='testLogo1_new',
                       _comment='comment1_new')]
