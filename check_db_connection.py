#import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group


#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = ORMFixture(_host="127.0.0.1", _database="addressbook", _user="root", _password="")

try:
    list = db.get_contacts_out_of_group(Group(_id=300))
    for item in list:
        print(item)
    print(len(list))
finally:
    pass #connection.close()












#try:
#    cursor = connection.cursor()
#    cursor.execute("select * from group_list")
#    for row in cursor.fetchall():              #fetchall returns all info as list of rows(like in db)
#        print(row)
#finally:
#    connection.close()