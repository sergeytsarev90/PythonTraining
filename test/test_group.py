# -*- coding: utf-8 -*-
from model.group import Group
from model.random_strings import random_string

from random import randrange
import pytest


# def random_string(prefix,maxlen):
#     symbols = string.ascii_letters+string.digits+string.punctuation+" "*5
#     return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["",random_string("name",10,"allstring")]
    for header in ["",random_string("header",20,"allstring")]
    for footer in ["",random_string("footer",20,"allstring")]
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app,group):
    app.group.open_page()
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_delete_some_group(app):
    app.group.open_page()
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups)-1 == len(new_groups)
    old_groups[index:index+1]=[]



def test_edit_some_group(app):
    app.group.open_page()
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="group_edit", header="header_edit", footer="footer_edit")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

