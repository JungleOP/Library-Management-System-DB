import sqlite3
connection = sqlite3.connect('sqlitedemo.db', timeout=10)
#-----------------------------------------------------------------------------------------
# for Table Librarian
connection.execute("""create table librarian(
    libid int primary key,
    fname varchar2(20) not null,
    lname varchar(20) not null,
    email varchar(20) not null,
    phone int not null
    );""")
connection.execute(""" insert into librarian values (1, 'Haleigh','Kleopatros','becefo@game4hr.com',096265606136);""")
connection.execute(""" insert into librarian values (2, ' Zulfiqar','Athelstan','tgi@asifboot.com',096264170017 );""")
connection.execute(""" insert into librarian values (5, 'Tuor','Helen','nashk@wpdork.com',096264898101);""")
connection.execute(""" insert into librarian values (3, 'Isolda',' Karter','dufc99@btcmod.com',096265355887);""")
connection.execute(""" insert into librarian values (4, 'Walhberct','Khava','susankr@lolaamaria.art',096265609057);""")
cursor = connection.execute("Select * from librarian;")
# print(cursor.fetchall())
connection.commit()
#-----------------------------------------------------------------------------------------
# for Table Member
connection.execute("""Create table member (
    member_id number (3) not null primary key,
    first_name varchar2(30),
    last_name varchar2(30),
    member_date date,
    phone_number number (15) not null,
    librarian_id number (3),
    foreign key (librarian_id) references librarian(librarian_id)
);
""")
connection.execute("""insert into member values (1,'Damon','Paine','6-jan-2017',08055546753,4);""")
connection.execute("""insert into member values (2,'Rimsha','Travis','02-Feb-2018',08055583174,3);""")
connection.execute("""insert into member values (3,'Nicolle','Hope','11-Dec-2019',07955519049,5);""")
connection.execute("""insert into member values (4,'Devon','Spencer','21-Mar-2020',07955583528,1);""")
connection.execute("""insert into member values (5,'Karis','Fenton','15-Apr-2016',07755501498,1);""")
cursor = connection.execute('select * from member;')
# print(cursor.fetchall())
connection.commit()
#-----------------------------------------------------------------------------------------
# for Table Publisher
connection.execute("""create table publisher(
    ID number(2) primary key,
    Name varchar2(20),
    PublisherEmail varchar2(30),
    City varchar2(7)
    );""")
connection.execute("""insert into publisher values(1,'Kevin matnic','kevin@gmail.com','USA');""")
connection.execute("""insert into publisher values (2,'James Clear','clear@gmail.com','USA');""")
connection.execute("""insert into publisher values (3,'Jim Kwik','kwik@hotmail.com','USA');""")
connection.execute("""insert into publisher values (4,'Cal Newport','cal@yahoo.com','USA');""")
connection.execute("""insert into publisher values (5,'Norman Vincent Peale','peale@gmail.com','USA');""")
cursor = connection.execute('select * from publisher;')
# print(cursor.fetchall())
connection.commit()
#-----------------------------------------------------
#for talbe Book
connection.execute("""create table book (
    book_id number (3) not null primary key,
    title varchar2(30),
    availability number (1),
    publisher_id number (3),
    member_id number (3),
    librarian_id number (3),
    foreign key (publisher_id) references publisher(publisher_id),
    foreign key (member_id) references member(member_id),
    foreign key (librarian_id) references librarian(librarian_id)
);

""")
connection.execute("""insert into book values (1,'Ghost In The Wires',0,1,2,2);""")
connection.execute("""insert into book values (2,'Atomic Habits',1,2,2,1);""")
connection.execute("""insert into book values (3,'Atomic Habits',1,3,1,5);""")
connection.execute("""insert into book values (4,'Deep Work',1,4,5,3);""")
connection.execute("""insert into book values (5,'The Power Of Positive Thinking',1,5,4,4);""")
cursor = connection.execute('select * from book;')
print(cursor.fetchall())
connection.commit()
#--------------------------------------------------
#member input checking if the book is available or not
#1- validating member_id
#2- checking book
try:
    member_id = int(input("Enter your member id: "))
    cursor = connection.execute('select member_id from member;')
    lst = [] # for id checking
    dict = {} # for books
    lst.append(cursor.fetchall()[member_id-1][0])
    if member_id in lst:
        print("Welcome")
        book_name = input("Enter the name of the book you are looking for:  ").lower().title().strip() # to handle user issues
        lst2 = []  # for books
        lst3 = []
        dict = {}
        c = connection.execute('select title from book;')
        x =  connection.execute('select availability from book;')
        lst2.append(c.fetchall())
        lst3.append(x.fetchall())
        for i in range(len(lst2)):
            for j in range(len(lst2[i])):
                dict[lst2[i][j][0]] = True
        for i in range(len(lst3)):
            for j in range(len(lst3[i])):
                dict[lst2[i][j][0]] = lst3[i][j][0]

        if dict[book_name]==1:
            print("Book Available")
        elif dict[book_name]==0:
            print("Book not Available")
except :
    print("Access Denied! ")
