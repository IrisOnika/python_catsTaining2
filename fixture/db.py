import pymysql.cursors
from model.group import Group
from model.contact import Contact
import re


class DbFixture:
    def __init__(self, _host, _database, _user, _password):
        self.host = _host
        self.database = _database
        self.user = _user
        self.password = _password
        self.connection = pymysql.connect(host=_host, database=_database, user=_user, password=_password)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('''select group_id, 
                                     group_name, 
                                     group_header, 
                                     group_footer 
                              from group_list''')
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(_id=str(id),
                                  _name=name,
                                  _logo=header,
                                  _comment=footer))
        finally:
            cursor.close()
        return list

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def get_contact_list(self):

        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('''select id,
                                     firstname,
                                     middlename,
                                     lastname,
                                     nickname,
                                     company,
                                     title,
                                     address,
                                     home,
                                     mobile,
                                     work,
                                     fax,
                                     email,
                                     email2,
                                     email3,
                                     homepage,
                                     byear,
                                     ayear,
                                     address2,
                                     phone2,
                                     notes
                              from addressbook''')
            for row in cursor:
                (id,
                 firstname,
                 middlename,
                 lastname,
                 nickname,
                 company,
                 title,
                 address,
                 home,
                 mobile,
                 work,
                 fax,
                 email,
                 email2,
                 email3,
                 homepage,
                 byear,
                 ayear,
                 address2,
                 phone2,
                 notes) = row
                list.append(Contact(_id=str(id),
                                    _firstname=firstname,
                                    _middlename=middlename,
                                    _lastname=lastname,
                                    _nickname=nickname,
                                    _company=company,
                                    _title=title,
                                    _address=address,
                                    _thome=home,
                                    _tmobile=mobile,
                                    _twork=work,
                                    _tfax=fax,
                                    _all_phones="\n".join(filter(lambda x: x!="",
                                                             (map(lambda x: self.clear(x),
                                                                filter(lambda x: x is not None,
                                                                    [home, mobile, work, phone2]))))),
                                    _email=email,
                                    _email2=email2,
                                    _email3=email3,
                                    _all_emails="\n".join(filter(lambda x: x != "",
                                                                filter(lambda x: x is not None,
                                                                       [email, email2, email3]))),
                                    _homepage=homepage,
                                    _byear=byear,
                                    _ayear=ayear,
                                    _address2=address2,
                                    _phone2=phone2,
                                    _notes=notes
                                  ))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()