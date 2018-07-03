from pony.orm import *
from datetime import datetime
from pymysql.converters import encoders, decoders, convert_mysql_timestamp
from model.group import Group
from model.contact import Contact


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        logo = Optional(str, column='group_header')
        comment = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(str, column='deprecated')

    def __init__(self, _host, _database, _user, _password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=_host, database=_database, user=_user, password=_password, conv=conv)
        self.db.generate_mapping()

    @db_session
    def orm_get_group_list(self):
        return self.convert_to_model_group(list(select(g for g in ORMFixture.ORMGroup)))

    def convert_to_model_group(self, groups):
        def convert(group):
            return Group(_id=str(group.id), _name= group.name, _logo=group.logo, _comment=group.comment)
        return list(map(convert, groups))

    @db_session
    def orm_get_contact_list(self):
        #return self.convert_to_model_contact(list(select(c for c in ORMFixture.ORMContact if c.deprecated == '0000-00-00 00:00:00')))
        return self.convert_to_model_contact(list(select(c for c in ORMFixture.ORMContact if c.deprecated is None)))

    def convert_to_model_contact(self, contacts):
        def convert(contact):
            return Contact(_id=str(contact.id), _firstname=contact.firstname, _lastname=contact.lastname)
        return list(map(convert, contacts))



