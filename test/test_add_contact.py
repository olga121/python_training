# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.new_contact import New_contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.new_contact.fill_new_contact_form(New_contact(name="Olga", last_name="Ivanova", home_number="84957777777", email="email@mail.ru"))
    app.session.logout()
