import sqlite3
from tkinter import *
connection = sqlite3.connect('sqlitedemo.db', timeout=10)
def check_book_availability():
    member_id = member_id_entry.get()
    cursor = connection.execute('select member_id from member;')
    member_ids = [row[0] for row in cursor.fetchall()]
    if int(member_id) not in member_ids:
        message_label.config(text='Invalid member ID')
        return
    book_name = book_name_entry.get().lower().title().strip()
    cursor = connection.execute('select title, availability from book;')
    books = {row[0]: row[1] for row in cursor.fetchall()}
    if book_name not in books:
        message_label.config(text='Book not found')
    elif books[book_name] == 1:
        message_label.config(text='Book available')
    else:
        message_label.config(text='Book not available')
root = Tk()
root.title('Book Availability Checker')
member_id_label = Label(root, text='Member ID:')
member_id_label.grid(row=0, column=0)
member_id_entry = Entry(root)
member_id_entry.grid(row=0, column=1)
book_name_label = Label(root, text='Book name:')
book_name_label.grid(row=1, column=0)
book_name_entry = Entry(root)
book_name_entry.grid(row=1, column=1)
check_button = Button(root, text='Check availability', command=check_book_availability)
check_button.grid(row=2, column=0, columnspan=2)
message_label = Label(root, text='')
message_label.grid(row=3, column=0, columnspan=2)
root.mainloop()
connection.close()
