from model.new_contact import New_contact

def test_modify_contact_first_name(app):
    if app.new_contact.count() == 0:
        app.new_contact.fill_new_contact_form(New_contact(name="test"))
    old_contacts = app.new_contact.get_contact_list()
    contact = New_contact(name="Dasha", last_name="Petrova")
    contact.id = old_contacts[0].id
    app.new_contact.modify_first_contact_name(contact)
    assert len(old_contacts) == app.new_contact.count()
    new_contacts = app.new_contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=New_contact.id_or_max) == sorted(new_contacts, key=New_contact.id_or_max)
