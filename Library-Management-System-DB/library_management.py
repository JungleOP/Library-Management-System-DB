import sqlite3

def execute_query(query):
    with sqlite3.connect('sqlitedemo.db', timeout=10) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return cursor.fetchall()

execute_query("""CREATE TABLE librarian (
    libid INTEGER PRIMARY KEY,
    fname VARCHAR(20) NOT NULL,
    lname VARCHAR(20) NOT NULL,
    email VARCHAR(20) NOT NULL,
    phone INTEGER NOT NULL
);""")



execute_query(""" INSERT INTO librarian VALUES (1, 'Haleigh','Kleopatros','becefo@game4hr.com',096265606136);""")
execute_query(""" INSERT INTO librarian VALUES (2, ' Zulfiqar','Athelstan','tgi@asifboot.com',096264170017 );""")
execute_query(""" INSERT INTO librarian VALUES (3, 'Isolda',' Karter','dufc99@btcmod.com',096265355887);""")
execute_query("""INSERT INTO librarian VALUES (4, 'Walhberct', 'Khava', 'susankr@lolaamaria.art', 96265609057);""")
execute_query(""" INSERT INTO librarian VALUES (5, 'Tuor','Helen','nashk@wpdork.com',096264898101);""")


execute_query("""CREATE TABLE member (
    member_id INTEGER PRIMARY KEY NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    member_date DATE,
    phone_number INTEGER NOT NULL,
    librarian_id INTEGER,
    FOREIGN KEY (librarian_id) REFERENCES librarian(libid)
);""")


execute_query("""INSERT INTO member VALUES (1,'Damon','Paine','6-jan-2017',08055546753,4);""")
execute_query("""INSERT INTO member VALUES (2,'Rimsha','Travis','02-Feb-2018',08055583174,3);""")
execute_query("""INSERT INTO member VALUES (3,'Nicolle','Hope','11-Dec-2019',07955519049,5);""")
execute_query("""INSERT INTO member VALUES (4,'Devon','Spencer','21-Mar-2020',07955583528,1);""")
execute_query("""INSERT INTO member VALUES (5, 'Karis', 'Fenton', '2016-04-15', 7755501498, 1);""")


execute_query("""CREATE TABLE publisher (
    publisher_id INTEGER PRIMARY KEY,
    name VARCHAR(20),
    email VARCHAR(30),
    city VARCHAR(7)
);""")

# insert data into the publisher table
execute_query("""INSERT INTO publisher VALUES(1,'Kevin matnic','kevin@gmail.com','USA');""")
execute_query("""INSERT INTO publisher VALUES (2,'James Clear','clear@gmail.com','USA');""")
execute_query("""INSERT INTO publisher VALUES (3,'Jim Kwik','kwik@hotmail.com','USA');""")
execute_query("""INSERT INTO publisher VALUES (4,'Cal Newport','cal@yahoo.com','USA');""")
execute_query("""INSERT INTO publisher VALUES (5, 'Norman Vincent Peale', 'peale@gmail.com', 'USA');""")


execute_query("""CREATE TABLE book (
    book_id INTEGER PRIMARY KEY NOT NULL,
    title VARCHAR(30),
    availability INTEGER,
    publisher_id INTEGER,
    member_id INTEGER,
    librarian_id INTEGER,
    FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id),
    FOREIGN KEY (member_id) REFERENCES member(member_id),
    FOREIGN KEY (librarian_id) REFERENCES librarian(libid)
);""")


execute_query("""INSERT INTO book VALUES (1,'Ghost In The Wires',0,1,2,2);""")
execute_query("""INSERT INTO book VALUES (2,'Atomic Habits',1,2,2,1);""")
execute_query("""INSERT INTO book VALUES (3,'Atomic Habits',1,3,1,5);""")
execute_query("""INSERT INTO book VALUES (4,'Deep Work',1,4,5,3);""")
execute_query("""INSERT INTO book VALUES (5, 'The Power Of Positive Thinking', 1, 5, 4, 4);""")


def check_book_availability(book_name):
    result = execute_query(f"SELECT availability FROM book WHERE title = '{book_name}'")
    if result:
        return True if result[0][0] else False
    else:
        return None

# get member id from user and check if book is available
try:
    member_id = int(input("Enter your member id: "))
    result = execute_query(f"SELECT member_id FROM member WHERE member_id = {member_id}")
    if result:
        print("Welcome")
        book_name = input("Enter the name of the book you are looking for: ").strip().title()
        availability = check_book_availability(book_name)
        if availability is not None:
            if availability:
                print("Book Available")
            else:
                print("Book not Available")
        else:
            print("Book not found")
    else:
        print("Access Denied!")
except ValueError:
    print("Invalid input")
