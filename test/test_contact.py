# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.open_home_page()
    app.session.login()
    app.contact.open_add_page()
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Ivan", mobile="8915439323", email="ivanov@ya.ru"))
    app.session.logout()

