# -*- coding: utf-8 -*-
import pytest
from new_contact import New_contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.fill_new_contact_form(New_contact(name="Olga", last_name="Ivanova", home_number="84957777777", email="email@mail.ru"))
    app.logout()
