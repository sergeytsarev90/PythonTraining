# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Ivan", mobile="8915439323", email="ivanov@ya.ru")
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



def test_delete_some_contact(app):
    app.contact.open_start_page()
    old_contacts = app.contact.get_contact_list()
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="test"))
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts[index:index+1]=[]
    assert old_contacts == new_contacts


def test_edit_some_contact(app):
    app.contact.open_start_page()
    old_contacts = app.contact.get_contact_list()
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="test"))
    contact = Contact(firstname="Vasiliy", middlename="Vasilich", lastname="Vasin", nickname="Vasya", mobile="890322439323", email="vasin@ya.ru")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


