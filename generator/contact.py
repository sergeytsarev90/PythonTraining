from model.contact import Contact
import os.path
import jsonpickle
import getopt
import sys
from generator.random_strings import random_string

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



testdata = [
    Contact(firstname="", middlename="", lastname="", nickname="", address="",homephone="", mobilephone="",workphone="",
                      secondaryphone="", email="", email2="", email3="")]+[
    Contact(firstname=random_string("",10,"letters"), middlename=random_string("",20,"letters"),
            lastname=random_string("",20,"letters"), nickname=random_string("", 10, "letters"),
            address=random_string("", 20, "allstring"),homephone=random_string("", 20, "digits"),
            mobilephone=random_string("", 10, "digits"),workphone=random_string("", 10, "digits"),
            secondaryphone=random_string("", 20, "digits"), email=random_string("", 20, "allstring"),
            email2=random_string("", 20, "allstring"), email3=random_string("", 20, "allstring"))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",f)
with open(file,"w") as out:
    jsonpickle.set_encoder_options("json",indent=2)
    out.write(jsonpickle.encode(testdata))