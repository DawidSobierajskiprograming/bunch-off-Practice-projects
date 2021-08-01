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

def main():
    print("     THE CONTACTS BOOK       ")
    print("-----------------------------")
    print("There are 4 things you can do \n View your contacts \n Insert New contactm \n Update existing contact \n Delete a exising contact")
    print("use the commands View, Insert, Update, Delete, commands to view this again and stop if you want to leave the program")
    userinput = None
    while userinput != "stop":
        userinput = input("What would you like to do? ")
        if userinput == "View":
            viewall()
        if userinput == "Insert":
            insertcontact()
        if userinput == "Update":
            updatecontact()
        if userinput == "Delete":
            deletecontact()
        if userinput == "commands":
            commands()
        if userinput == "stop":
            break




def viewall():
    print ("These are all current contacts in the database")
    conn1 = sqlite3.connect("Contactbook.db")
    cursor1 = conn1.cursor()
    cursor1.execute("SELECT * FROM contacts")
    contacts = cursor1.fetchall()
    for item in contacts:
        print(item)
    conn1.commit()
    conn1.close()


def insertcontact():
    conn1 = sqlite3.connect("Contactbook.db")
    cursor1 = conn1.cursor()
    f_name = input ("Please input the first name: ")
    l_name = input ("Please input the last name: ")
    p_num = str(input("Please input the phone number: "))
    email = input("Please input the email address: ")
    cursor1.execute("INSERT INTO contacts (first_name, last_name, phone_number, email_address) VALUES(?,?,?,?)", (f_name, l_name, p_num, email))
    conn1.commit()
    conn1.close()

def deletecontact():
    conn1 = sqlite3.connect("Contactbook.db")
    cursor1 = conn1.cursor()
    name_del = input("Please Input the name of the individual you would like to delete: ")
    cursor1.execute("DELETE from contacts WHERE first_name LIKE ?", (name_del,))
    conn1.commit()
    conn1.close()

def updatecontact():
    conn1 = sqlite3.connect("Contactbook.db")
    cursor1 = conn1.cursor()
    a = input("Which contact would you like to modify?: ")
    b = input("Which part of the contact would you like to modify?: ")
    c = input("What would you like to change the value too?: ")
    info_tuple = (c,a)
    update_query = """UPDATE contacts SET {} = ? WHERE first_name LIKE ?"""
    fomated_query = update_query.format(b)
    cursor1.execute(fomated_query, info_tuple)
    conn1.commit()
    conn1.close()

def commands():
    print("use the commands View, Insert, Update, Delete, commands to view this again and stop if you want to leave the program")
    
main()