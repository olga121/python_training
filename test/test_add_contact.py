# -*- coding: utf-8 -*-

from model.new_contact import New_contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.new_contact.fill_new_contact_form(New_contact(name="Olga", last_name="Ivanova", home_number="84957777777", email="email@mail.ru"))
    app.session.logout()
