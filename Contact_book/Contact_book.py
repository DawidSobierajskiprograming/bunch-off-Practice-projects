import sqlite3
from sqlite3.dbapi2 import Cursor, connect


conn = sqlite3.connect("Contactbook.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (
    first_name text,
    last_name text,
    phone_number text,
    email_address text
    )""")

conn.close()


def viewall():
    print ("These are all current contacts in the database")
    conn1 = sqlite3.connect("Contactbook.db")
    cursor1 = conn1.cursor()
    cursor1.execute("SELECT * FROM contacts")
    contacts = cursor1.fetchall()
    for item in contacts:
        print(item[0])
    conn1.commit
    conn1.close


def insertcontact():
    conn1 = sqlite3.connect("Contactbook.db")
    cursor1 = conn1.cursor()
    f_name = input ("Please input the first name: ")
    l_name = input ("Please input the last name: ")
    p_num = int(input("Please input the phone number: "))
    email = input("Please input the email address: ")
    insertdetails = """INSERT INTO contacts
                    (first_name, last_name, phone_number, email_address)
                    VALUES(?,?,?,?)"""
    data_tuple = (f_name,l_name,p_num,email)
    cursor1.execute(insertdetails,data_tuple)
    conn1.commit
    conn1.close

def deletecontact():
    conn1 = sqlite3.connect("Contactbook.db")
    cursor1 = conn1 .cursor()
    name_del = input("Please Input the name of the individual you would like to delete: ")
    deletequery = "DELETE from contacts WHERE first_name = VALUES(?)"
    cursor1.execute(deletequery,name_del)
    conn1.commit
    conn1.close
    

viewall()
insertcontact()
insertcontact()
insertcontact()
viewall()
deletecontact()