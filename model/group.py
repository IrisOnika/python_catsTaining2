

class Group():

    def __init__(self,  _name=None, _logo=None, _comment=None, _id=None):
        self.name=_name
        self.logo = _logo
        self.comment = _comment
        self.id = _id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id == other.id or self.id == None or other.id == None) and self.name == other.name
