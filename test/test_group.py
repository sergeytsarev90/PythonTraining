# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_add_group(app, db, json_groups,check_ui):
    group = json_groups
    app.group.open_page()
    old_groups = db.get_group_list()
    app.group.create(group)
    #assert len(old_groups)+1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_delete_some_group(app,db,check_ui):
    app.group.open_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups)-1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_edit_some_group(app,db,check_ui):
    app.group.open_page()
    if app.group.count()==0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group_for_edit = random.choice(old_groups)
    group = Group(name="group_edit", header="header_edit", footer="footer_edit",id=group_for_edit.id)
    app.group.edit_group_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(group_for_edit)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

