from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, address=None, all_phones_from_home_page=None,
                 mobilephone=None, homephone=None, workphone=None, secondaryphone=None, email=None, email2=None, email3=None,
                 all_emails_from_home_page = None, id=None, all_phones_from_db=None, all_emails_from_db=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id
        self.all_phones_from_db = all_phones_from_db
        self.all_emails_from_db = all_emails_from_db

    def __repr__(self):
        return "%s : %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.lastname, self.firstname, self.address, self.homephone, self.mobilephone, self.workphone, self.secondaryphone,
            self.email, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and (
               self.address is None or other.address is None or self.address == other.address) and (
               self.homephone is None or other.homephone is None or self.homephone == other.homephone) and (
               self.mobilephone is None or other.mobilephone is None or self.mobilephone == other.mobilephone) and (
               self.workphone is None or other.workphone is None or self.workphone == other.workphone) and (
               self.secondaryphone is None or other.secondaryphone is None or self.secondaryphone == other.secondaryphone) and (
               self.email is None or other.email is None or self.email == other.email) and (
               self.email2 is None or other.email2 is None or self.email2 == other.email2) and (
               self.email3 is None or other.email3 is None or self.email3 == other.email3)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
