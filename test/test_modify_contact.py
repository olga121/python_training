from model.new_contact import New_contact
from random import randrange

def test_modify_some_contact_name(app):
    if app.new_contact.count() == 0:
        app.new_contact.fill_new_contact_form(New_contact(name="test"))
    old_contacts = app.new_contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = New_contact(name="Dasha", last_name="Petrova")
    contact.id = old_contacts[index].id
    app.new_contact.modify_some_contact_name(index, contact)
    assert len(old_contacts) == app.new_contact.count()
    new_contacts = app.new_contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=New_contact.id_or_max) == sorted(new_contacts, key=New_contact.id_or_max)


