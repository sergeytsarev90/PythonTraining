from model.group import Group
from data.random_strings import random_string


constant = [
    Group(name="name1",header="header1",footer="footer1"),
    Group(name="name2",header="header2",footer="footer2")
]


testdata = [
    Group(name="", header="", footer="")]+\
           [
    Group(name=random_string("name",10,"allstring"), header=random_string("header",20,"allstring"), footer=random_string("footer",20,"allstring"))
    for i in range(5)
           ]
