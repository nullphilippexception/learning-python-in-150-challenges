import sqlite3
# connect to db
with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

# create table
cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
    id integer PRIMARY KEY,
    first_name text,
    surname text,
    phone_number text);""")

# insert values into table
cursor.execute("""INSERT INTO Names(id,first_name,surname,phone_number)
                VALUES("1", "Simon", "Howels", "01223 349752")""")
cursor.execute("""INSERT INTO Names(id,first_name,surname,phone_number)
                VALUES("2", "Karen", "Phillips", "01954 295773")""")
cursor.execute("""INSERT INTO Names(id,first_name,surname,phone_number)
                VALUES("3", "Darren", "Smith", "01583 749012")""")
cursor.execute("""INSERT INTO Names(id,first_name,surname,phone_number)
                VALUES("4", "Anne", "Jones", "01323 567322")""")
cursor.execute("""INSERT INTO Names(id,first_name,surname,phone_number)
                VALUES("5", "Mark", "Smith", "01223 855534")""")
db.commit()
