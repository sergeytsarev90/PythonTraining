from model.contact import Contact
from data.random_strings import random_string



testdata = [
    Contact(firstname="", middlename="", lastname="", nickname="", address="",homephone="", mobilephone="",workphone="",
                      secondaryphone="", email="", email2="", email3="")]+[
    Contact(firstname=random_string("",10,"letters"), middlename=random_string("",20,"letters"),
            lastname=random_string("",20,"letters"), nickname=random_string("", 10, "letters"),
            address=random_string("", 20, "allstring"),homephone=random_string("", 20, "digits"),
            mobilephone=random_string("", 10, "digits"),workphone=random_string("", 10, "digits"),
            secondaryphone=random_string("", 20, "digits"), email=random_string("", 20, "allstring"),
            email2=random_string("", 20, "allstring"), email3=random_string("", 20, "allstring"))
    for i in range(5)
]