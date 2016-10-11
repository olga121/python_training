import mysql.connector

connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
#finally:
#   connection.close()
    cursor_contacts = connection.cursor()
    cursor_contacts.execute("select * from addressbook where deprecated='0000-00-00 00:00:00'")
    for row in cursor_contacts.fetchall():
        print(row)
finally:
    connection.close()