# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.open_home_page()
    app.session.login()
    app.group.open_page()
    app.group.create(Group(name="new_group", header="new_header", footer="new_footer"))
    app.group.return_to_page()
    app.session.logout()

def test_add_contact(app):
    app.open_home_page()
    app.session.login()
    app.contact.open_add_page()
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Ivan", mobile="8915439323", email="ivanov@ya.ru"))
    app.session.logout()

