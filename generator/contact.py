from model.new_contact import New_contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts","file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o =="-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))