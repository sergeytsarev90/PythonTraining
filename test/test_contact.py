# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.open_home_page()
    app.session.login()
    app.contact.open_add_page()
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Ivan", mobile="8915439323", email="ivanov@ya.ru"))
    app.contact.open_start_page()
    app.session.logout()
    pass

def test_delete_first_contact(app):
    app.open_home_page()
    app.session.login()
    app.contact.open_start_page()
    app.contact.delete_first_contact()
    app.contact.open_start_page()
    app.session.logout()

def test_edit_first_contact(app):
    app.open_home_page()
    app.session.login()
    app.open_home_page()
    app.contact.edit_first_contact(Contact(firstname="Vasiliy", middlename="Vasilich", lastname="Vasin", nickname="Vasya", mobile="890322439323", email="vasin@ya.ru"))
    app.contact.open_start_page()
    app.session.logout()

