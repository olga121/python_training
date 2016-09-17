# -*- coding: utf-8 -*-

from model.new_contact import New_contact


def test_add_contact(app):
    old_contacts = app.new_contact.get_contact_list()
    contact = New_contact(name="Olga", last_name="Ivanova", home_number="84957777777", email="email@mail.ru")
    app.new_contact.fill_new_contact_form(contact)
    assert len(old_contacts) + 1 == app.new_contact.count()
    new_contacts = app.new_contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=New_contact.id_or_max) == sorted(new_contacts, key=New_contact.id_or_max)
