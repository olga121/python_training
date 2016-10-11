from model.new_contact import New_contact

def test_contact_list(app,db):
    ui_list = app.new_contact.get_contact_list()
    def clean(contact):
        return New_contact(id=contact.id, name=contact.name.strip(), last_name=contact.last_name.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=New_contact.id_or_max) == sorted(db_list, key=New_contact.id_or_max)