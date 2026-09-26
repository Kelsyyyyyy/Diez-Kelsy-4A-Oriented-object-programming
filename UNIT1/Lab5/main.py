
from books import book
from users import user
from library import library


#instance
book1 = book ("001","Python for dummies", "Kelsy", "Villareal")
book2 = book ("002","OOP fundamentals", "Grecia",  "E.A")
user1 = user ("001", "Pepe")

library1 = library()
library1.add_book(book1)
library1.add_book(book2)
library1.add_users(user1)

library1.show_books()

user2 = user ("002","Maria")
library1.add_users(user2)

print("\n===USERS===")
library1.show_users()

print ("\n===Borrowed Books===")
library1.borrow_book("001","001")
library1.borrow_book("002","002")

print("\n Trying to borrow a book that has alreay been borrwed...")
library1.borrow_book("001","002")

print("\n===Returning Books===")
library1.return_book("001","001")
