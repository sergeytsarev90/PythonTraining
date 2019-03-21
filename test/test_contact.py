# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Ivan", mobile="8915439323", email="ivanov@ya.ru"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)



def test_delete_first_contact(app):
    app.contact.open_start_page()
    old_contacts = app.contact.get_contact_list()
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="test"))
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts[0:1]=[]
    assert old_contacts == new_contacts


def test_edit_first_contact(app):
    app.contact.open_start_page()
    old_contacts = app.contact.get_contact_list()
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact(firstname="Vasiliy", middlename="Vasilich", lastname="Vasin", nickname="Vasya", mobile="890322439323", email="vasin@ya.ru"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


