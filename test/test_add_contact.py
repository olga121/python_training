# -*- coding: utf-8 -*-

from model.new_contact import New_contact


def test_add_contact(app):
    old_contacts = app.new_contact.get_contact_list()
    app.new_contact.fill_new_contact_form(New_contact(name="Olga", last_name="Ivanova", home_number="84957777777", email="email@mail.ru"))
    new_contacts = app.new_contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

