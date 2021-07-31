import sqlite3
from sqlite3.dbapi2 import Cursor


conn = sqlite3.connect("Contactbook.db")

cursor = conn.cursor()

#cursor.execute("""CREATE TABLE contacts (
#    first_name text,
#    last_name text,
#    phone_number text
#)""")

#many_contacts = [
#                    ('Wes', 'Brown','2342563657'),
#                    ('James','sheen','0987654321'),
#                    ('Sam','Car','56734254434')
#                    ]                
#cursor.executemany("INSERT INTO contacts VALUES (?,?,?)", many_contacts)

cursor.execute("SELECT * FROM contacts")

print(cursor.fetchall())


conn.commit()


conn.close()