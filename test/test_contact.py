# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contast_list()
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Ivan", mobile="8915439323", email="ivanov@ya.ru"))



def test_delete_first_contact(app):
    app.contact.open_start_page()
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="test"))
    app.contact.delete_first_contact()


def test_edit_first_contact(app):
    app.contact.open_start_page()
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact(firstname="Vasiliy", middlename="Vasilich", lastname="Vasin", nickname="Vasya", mobile="890322439323", email="vasin@ya.ru"))


