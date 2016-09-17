from model.new_contact import New_contact
from random import randrange

def test_del_some_contact(app):
    if app.new_contact.count() == 0:
        app.new_contact.fill_new_contact_form(New_contact(name = "test"))
    old_contacts = app.new_contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.new_contact.del_contact_by_index(index)
    assert len(old_contacts) - 1 == app.new_contact.count()
    new_contacts = app.new_contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

