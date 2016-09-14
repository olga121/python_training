from sys import maxsize

class New_contact:
    def __init__(self, name=None, last_name=None, home_number=None, email=None, id=None):
        self.name = name
        self.last_name = last_name
        self.home_number =home_number
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize