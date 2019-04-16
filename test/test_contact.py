# -*- coding: utf-8 -*-
from model.contact import Contact
import re
from random import randrange
import random


def test_add_contact(app,db,check_ui, json_contacts):
    contact=json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_delete_some_contact(app,db,check_ui):
    app.contact.open_start_page()
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_edit_some_contact(app,db,check_ui):
    app.contact.open_start_page()
    if app.contact.count()==0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="Vasiliy", middlename="Vasilich", lastname="Vasin", nickname="Vasya", mobilephone="890322439323", email="vasin@ya.ru")
    contact_for_edit = random.choice(old_contacts)
    contact.id=contact_for_edit.id
    app.contact.edit_contact_by_id(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(contact_for_edit)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_phones_on_home_page(app,db):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)



def test_phones_on_view_page(app):
    index = 0#randrange(app.contact.count())
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def test_assert_all_members_from_home_page_with_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="vasya", middlename="vasin", lastname="voviy"))
    else:
        pass
    contacts_from_home_page = app.contact.get_contact_list()
    contact_from_data_base = db.get_contact_list()
    assert len(contacts_from_home_page) == len(contact_from_data_base)

    contacts_from_home_page_sorted = sorted(contacts_from_home_page, key=Contact.id_or_max)
    contact_from_data_base_sorted = sorted(contact_from_data_base, key=Contact.id_or_max)
    for x in range(len(contacts_from_home_page_sorted)):
        assert contacts_from_home_page_sorted[x].firstname == contact_from_data_base_sorted[x].firstname.strip()
        assert contacts_from_home_page_sorted[x].lastname == contact_from_data_base_sorted[x].lastname.strip()
        assert contacts_from_home_page_sorted[x].address == contact_from_data_base_sorted[x].address
        assert contacts_from_home_page_sorted[x].all_emails_from_home_page == merge_emails_like_on_home_page(
            contact_from_data_base_sorted[x])
        assert contacts_from_home_page_sorted[x].all_phones_from_home_page == merge_phones_like_on_home_page(
            contact_from_data_base_sorted[x])

def clear(s):
    return re.sub("[() -]","",s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))