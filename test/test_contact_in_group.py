from model.contact import Contact
from model.group import Group
from random import randrange
import random


def test_add_contact_in_group(app,orm):
    prepare_contact_group_for_test(app, orm)
    group = random.choice(orm.get_group_list())
    contact = random.choice(orm.get_contact_list())
    old_contact_list_in_group = orm.get_contacts_in_group(group)
    app.contact.add_contact_in_group(contact,group)
    new_contact_list_in_group = orm.get_contacts_in_group(group)
    old_contact_list_in_group.append(contact)
    assert sorted(old_contact_list_in_group,key=Contact.id_or_max) == sorted(new_contact_list_in_group, key=Contact.id_or_max)


def test_delete_contact_from_group(app,orm):
    prepare_contact_group_for_test(app,orm)
    group = random.choice(orm.get_group_list())
    app.contact.go_to_group(group)
    old_contact_list_in_group = orm.get_contacts_in_group(group)
    contact = random.choice(old_contact_list_in_group)
    app.contact.delete_contact_from_group(contact)
    new_contact_list_in_group = orm.get_contacts_in_group(group)
    old_contact_list_in_group.remove(contact)
    assert sorted(old_contact_list_in_group,key=Contact.id_or_max) == sorted(new_contact_list_in_group, key=Contact.id_or_max)


def prepare_contact_group_for_test(app, orm):
    app.group.open_page()
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    app.contact.open_start_page()
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))