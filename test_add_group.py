# -*- coding: utf-8 -*-
from group import Group
from contact import Contact
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.open_home_page()
    app.login()
    app.open_group_page()
    app.create_group(Group(name="new_group",header="new_header",footer="new_footer"))
    app.return_to_groups_page()
    app.logout()

def test_add_contact(app):
    app.open_home_page()
    app.login()
    app.open_add_contact_page()
    app.create_contact(Contact(firstname="Ivan",middlename="Ivanovich",lastname="Ivanov",nickname="Ivan",mobile="8915439323",email="ivanov@ya.ru"))
    app.logout()

