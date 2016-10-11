from model.new_contact import New_contact
import random

def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.new_contact.fill_new_contact_form(New_contact(name = "test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.new_contact.del_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.new_contact.count()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(app.new_contact.get_contact_list(), key=New_contact.id_or_max) == sorted(new_contacts, key=New_contact.id_or_max)

