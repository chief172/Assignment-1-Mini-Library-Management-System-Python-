

# Data Structures
books = {}  # ISBN → {"title": ..., "author": ..., "genre": ..., "total": ..., "available": ...}
members = []  # list of dicts: {"id": ..., "name": ..., "email": ..., "borrowed_books": [...]}
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Romance", "Fantasy")



def find_member(member_id):
    for member in members:
        if member["id"] == member_id:
            return member
    return None

def book_exists(isbn):
    return isbn in books



def add_book():
    isbn = input("Enter ISBN: ")
    if book_exists(isbn):
        print("Book with this ISBN already exists.")
        return
    title = input("Enter title: ")
    author = input("Enter author: ")
    genre = input(f"Enter genre {genres}: ")
    if genre not in genres:
        print("Invalid genre.")
        return
    try:
        total = int(input("Enter total copies: "))
    except ValueError:
        print("Invalid number.")
        return
    books[isbn] = {"title": title, "author": author, "genre": genre, "total": total, "available": total}
    print(f" Book '{title}' added successfully!")


def add_member():
    member_id = (input("Enter member ID: "))
    if find_member(member_id):
        print("Member ID already exists.")
        return
    name = input("Enter name: ")
    email = input("Enter email: ")
    members.append({"id": member_id, "name": name, "email": email, "borrowed_books": []})
    print(f"Member '{name}' added successfully!")


def search_books():
    keyword = input("Enter keyword (title/author): ").lower()
    results = [book for book in books.values() if keyword in book["title"].lower() or keyword in book["author"].lower()]
    if not results:
        print("No books found.")
    else:
        print("\nSearch Results:")
        for book in results:
            print(f" - {book['title']} by {book['author']} ({book['genre']}) | Available: {book['available']}")


def update_book():
    isbn = input("Enter ISBN of book to update: ")
    if not book_exists(isbn):
        print("Book not found.")
        return
    title = input("Enter new title (leave blank to keep same): ")
    author = input("Enter new author (leave blank to keep same): ")
    genre = input(f"Enter new genre {genres} (leave blank to keep same): ")
    total = input("Enter new total copies (leave blank to keep same): ")

    book = books[isbn]
    if title: book["title"] = title
    if author: book["author"] = author
    if genre and genre in genres: book["genre"] = genre
    if total.isdigit():
        diff = int(total) - book["total"]
        book["total"] = int(total)
        book["available"] += diff
    print(f"Book '{isbn}' updated successfully.")


def update_member():
    member_id = input("Enter member ID to update: ")
    member = find_member(member_id)
    if not member:
        print("Member not found.")
        return
    name = input("Enter new name (leave blank to keep same): ")
    email = input("Enter new email (leave blank to keep same): ")
    if name: member["name"] = name
    if email: member["email"] = email
    print(f"Member '{member_id}' updated successfully.")


def delete_book():
    isbn = input("Enter ISBN to delete: ")
    if not book_exists(isbn):
        print(" Book not found.")
        return
    for m in members:
        if isbn in m["borrowed_books"]:
            print("Cannot delete — book currently borrowed.")
            return
    del books[isbn]
    print(f"Book '{isbn}' deleted successfully.")


def delete_member():
    member_id = input("Enter member ID to delete: ")
    member = find_member(member_id)
    if not member:
        print(" Member not found.")
        return
    if member["borrowed_books"]:
        print(" Cannot delete — member has borrowed books.")
        return
    members.remove(member)
    print(f"Member '{member_id}' deleted successfully.")


def borrow_book():
    member_id = input("Enter member ID: ")
    member = find_member(member_id)
    if not member:
        print("Member not found.")
        return
    isbn = input("Enter ISBN: ")
    if not book_exists(isbn):
        print("Book not found.")
        return
    book = books[isbn]
    if len(member["borrowed_books"]) >= 3:
        print("Cannot borrow more than 3 books.")
        return
    if book["available"] <= 0:
        print("No copies available.")
        return
    book["available"] -= 1
    member["borrowed_books"].append(isbn)
    print(f" '{book['title']}' borrowed successfully by {member['name']}.")


def return_book():
    member_id = input("Enter member ID: ")
    member = find_member(member_id)
    if not member:
        print("Member not found.")
        return
    isbn = int(input("Enter ISBN: "))
    if isbn not in member["borrowed_books"]:
        print("This member did not borrow this book.")
        return
    member["borrowed_books"].remove(isbn)
    books[isbn]["available"] += 1
    print(f" '{books[isbn]['title']}' returned successfully.")



def main():
    while True:
        print("\n Library Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Update Member")
        print("6. Delete Book")
        print("7. Delete Member")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. Exit")

        choice = input("Choose an option (1-10): ")

        if choice == "1": add_book()
        elif choice == "2": add_member()
        elif choice == "3": search_books()
        elif choice == "4": update_book()
        elif choice == "5": update_member()
        elif choice == "6": delete_book()
        elif choice == "7": delete_member()
        elif choice == "8": borrow_book()
        elif choice == "9": return_book()
        elif choice == "10":
            print(" Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
