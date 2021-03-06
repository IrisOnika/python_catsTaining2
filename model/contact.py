

class Contact():

    def __init__(self,
                 _firstname=None,
                 _middlename=None,
                 _lastname=None,
                 _nickname=None,
                 _title=None,
                 _company=None,
                 _address=None,
                 _thome=None,
                 _tmobile=None,
                 _twork=None,
                 _tfax=None,
                 _all_phones=None,
                 _email=None,
                 _email2=None,
                 _email3=None,
                 _all_emails=None,
                 _homepage=None,
                 _byear=None,
                 _ayear=None,
                 _address2=None,
                 _phone2=None,
                 _notes=None,
                 _id=None):
        self.firstname=_firstname
        self.middlename = _middlename
        self.lastname = _lastname
        self.nickname = _nickname
        self.title = _title
        self.company = _company
        self.address = _address
        self.thome = _thome
        self.tmobile = _tmobile
        self.twork = _twork
        self.tfax = _tfax
        self.all_phones = _all_phones,
        self.email = _email
        self.email2 = _email2
        self.email3 = _email3
        self.all_emails = _all_emails
        self.homepage = _homepage
#        self.bmonth = _bmonth
        self.byear = _byear
#        self.aday = _aday
#        self.amonth = _amonth
        self.ayear = _ayear
        self.address2 = _address2
        self.phone2 = _phone2
        self.notes = _notes
        self.id = _id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.address, self.all_emails, self.all_phones)

    def __eq__(self, other):
        return (self.id == other.id or self.id == None or other.id == None) and self.firstname == other.firstname and self.lastname == other.lastname and self.address == other.address