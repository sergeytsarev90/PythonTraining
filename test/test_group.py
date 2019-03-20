# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.open_page()
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="new_group", header="new_header", footer="new_footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)



def test_delete_first_group(app):
    app.group.open_page()
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups)-1 == len(new_groups)
    old_groups[0:1]=[]
    assert old_groups == new_groups


def test_edit_first_group(app):
    app.group.open_page()
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="group_edit", header="header_edit", footer="footer_edit"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

