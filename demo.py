# demo.py

from operation import *

print("\n--- DEMO: Mini Library Management System ---")

print(add_book("101", "harry potter", "J.K Rowling", "Fiction", 3))
print(add_book("102", "Diary of the Wimpy Kid", "Jeff Kinney", "Non-Fiction", 10))
print(add_member("M001", "Alice", "alice@gmail.com"))
print(add_member("M002", "Bob", "bob@gmail.com"))

print(borrow_book("M001", "101"))
print(borrow_book("M002", "102"))
print(return_book("M001", "101"))
print(delete_book("101"))

print("\nSearch results for 'Di':")
for b in search_books("Di"):
    print(b)
