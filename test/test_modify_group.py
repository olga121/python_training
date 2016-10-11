from model.group import Group
#from random import randrange
import random

def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    print ("id= ", group.id)
    new_data = Group(name="New name")
    app.group.modify_group_by_id(group.id, new_data)
    new_groups = db.get_group_list()
    for x in range(len(old_groups)):
        if old_groups[x].id == group.id:
            old_groups[x].name = new_data.name
    assert len(old_groups) == app.group.count()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="new header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="new footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
