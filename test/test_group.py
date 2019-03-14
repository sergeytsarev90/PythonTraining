# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.open_page()
    app.group.create(Group(name="new_group", header="new_header", footer="new_footer"))



def test_delete_first_group(app):
    app.group.open_page()
    if app.group.count()==0:
        app.group.create(Group(name="test"))

    app.group.delete_first_group()


def test_edit_first_group(app):
    app.group.open_page()
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group(name="group_edit", header="header_edit", footer="footer_edit"))

