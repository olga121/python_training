from sys import maxsize

class New_contact:
    def __init__(self, name=None, last_name=None, id=None, home_number=None, mobile_number = None, work_number = None,
                 secondary_number = None, email=None, email2 = None, email3 = None, address = None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.name = name
        self.last_name = last_name
        self.home_number =home_number
        self.work_number = work_number
        self.mobile_number = mobile_number
        self.secondary_number = secondary_number
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize