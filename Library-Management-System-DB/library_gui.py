import sqlite3
from tkinter import *

# Connect to the database
connection = sqlite3.connect('sqlitedemo.db', timeout=10)

# Define the function to check book availability
def check_book_availability():
    # Get the member ID from the entry widget
    member_id = member_id_entry.get()

    # Check if the member ID exists in the database
    cursor = connection.execute('select member_id from member;')
    member_ids = [row[0] for row in cursor.fetchall()]
    if int(member_id) not in member_ids:
        message_label.config(text='Invalid member ID')
        return

    # Get the book name from the entry widget
    book_name = book_name_entry.get().lower().title().strip()

    # Check if the book is available
    cursor = connection.execute('select title, availability from book;')
    books = {row[0]: row[1] for row in cursor.fetchall()}
    if book_name not in books:
        message_label.config(text='Book not found')
    elif books[book_name] == 1:
        message_label.config(text='Book available')
    else:
        message_label.config(text='Book not available')

# Create the GUI window
root = Tk()
root.title('Book Availability Checker')

# Create the member ID label and entry widget
member_id_label = Label(root, text='Member ID:')
member_id_label.grid(row=0, column=0)
member_id_entry = Entry(root)
member_id_entry.grid(row=0, column=1)

# Create the book name label and entry widget
book_name_label = Label(root, text='Book name:')
book_name_label.grid(row=1, column=0)
book_name_entry = Entry(root)
book_name_entry.grid(row=1, column=1)

# Create the check availability button
check_button = Button(root, text='Check availability', command=check_book_availability)
check_button.grid(row=2, column=0, columnspan=2)

# Create the message label
message_label = Label(root, text='')
message_label.grid(row=3, column=0, columnspan=2)

# Run the GUI main loop
root.mainloop()

# Close the database connection
connection.close()
