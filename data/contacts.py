from model.new_contact import New_contact
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_letters(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_numbers(prefix, maxlen):
    symbols = string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [New_contact(name="", last_name="", home_number="", mobile_number = "", work_number = "",
                 secondary_number = "", email="", email2 = "", email3 = "", address = "")] + [
    New_contact(name=random_string_letters("name", 10), last_name=random_string_letters("last_name", 20),
                mobile_number = random_string_numbers("mobile_number", 20), work_number = random_string_numbers("work_number", 20),
                secondary_number= random_string_numbers("secondary_number", 20), email=random_string("email", 10),
                email2 = random_string("email2", 10), email3 = random_string("email3", 10), address = random_string("address", 20),
                home_number=random_string_numbers("home_number", 20))
    for i in range(5)
]