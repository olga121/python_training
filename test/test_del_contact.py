from model.new_contact import New_contact

def test_del_first_contact(app):
    if app.new_contact.count() == 0:
        app.new_contact.fill_new_contact_form(New_contact(name = "test"))
    old_contacts = app.new_contact.get_contact_list()
    app.new_contact.del_first_contact()
    assert len(old_contacts) - 1 == app.new_contact.count()
    new_contacts = app.new_contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts