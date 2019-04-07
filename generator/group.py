from model.group import Group
import os.path
import jsonpickle
import getopt
import sys
from generator.random_strings import random_string

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

testdata = [Group(name="", header="", footer="")]+\
           [Group(name=random_string("name",10,"allstring"), header=random_string("header",20,"allstring"),
                  footer=random_string("footer",20,"allstring"))
            for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",f)
with open(file,"w") as out:
    jsonpickle.set_encoder_options("json",indent=2)
    out.write(jsonpickle.encode(testdata))