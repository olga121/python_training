from model.new_contact import New_contact
from random import randrange
import re
#import random
#import string


def test_contact_on_home_page(app):
    if app.new_contact.count() == 0:
        app.new_contact.fill_new_contact_form(New_contact(name="test"))
    length_of_contacts_list = app.new_contact.get_contact_list()
    index = randrange(len(length_of_contacts_list))
    print ("index="+str(index))
    contact_from_home_page = app.new_contact.get_contact_list()[index]
    contact_from_edit_page = app.new_contact.get_contact_info_from_edit_page(index)
    assert clear_newline_whitespace(contact_from_home_page.name) == clear_newline_whitespace(contact_from_edit_page.name)
    assert clear_newline_whitespace(contact_from_home_page.last_name) == clear_newline_whitespace(contact_from_edit_page.last_name)
    assert clear_newline_whitespace(contact_from_home_page.address) == clear_newline_whitespace(contact_from_edit_page.address)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def clear_newline_whitespace(s):
    return re.sub(" ", "", "".join(re.findall(".+", s)))
#    return re.sub("[\n]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join (filter( lambda x: x != "",
                       map(lambda x: clear(x) ,
                           filter(lambda x: x is not None,
                                  [contact.home_number, contact.mobile_number, contact.work_number, contact.secondary_number]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join (filter( lambda x: x != "",
                       map(lambda x: clear(x) ,
                           filter(lambda x: x is not None,
                                  [contact.email, contact.email2, contact.email3]))))