# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.open_home_page()
    app.session.login()
    app.group.open_page()
    app.group.create(Group(name="new_group", header="new_header", footer="new_footer"))
    app.group.return_to_page()
    app.session.logout()


