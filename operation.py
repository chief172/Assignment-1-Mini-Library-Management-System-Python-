# operation.py

# Data Structures
books = {}
members = []
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Romance", "Fantasy")


# Helper Functions
def find_member(member_id):
    for member in members:
        if member["id"] == member_id:
            return member
    return None

def book_exists(isbn):
    return isbn in books


# CRUD + Borrow/Return Functions
def add_book(isbn, title, author, genre, total):
    if book_exists(isbn) or genre not in genres:
        return False
    books[isbn] = {"title": title, "author": author, "genre": genre, "total": total, "available": total}
    return True

def add_member(member_id, name, email):
    if find_member(member_id):
        return False
    members.append({"id": member_id, "name": name, "email": email, "borrowed_books": []})
    return True

def search_books(keyword):
    keyword = keyword.lower()
    results = [book for book in books.values() if keyword in book["title"].lower() or keyword in book["author"].lower()]
    return results

def update_book(isbn, title=None, author=None, genre=None, total=None):
    if not book_exists(isbn):
        return False
    book = books[isbn]
    if title: book["title"] = title
    if author: book["author"] = author
    if genre and genre in genres: book["genre"] = genre
    if total:
        diff = total - book["total"]
        book["total"] = total
        book["available"] += diff
    return True

def update_member(member_id, name=None, email=None):
    member = find_member(member_id)
    if not member:
        return False
    if name: member["name"] = name
    if email: member["email"] = email
    return True

def delete_book(isbn):
    if not book_exists(isbn):
        return False
    for m in members:
        if isbn in m["borrowed_books"]:
            return False
    del books[isbn]
    return True

def delete_member(member_id):
    member = find_member(member_id)
    if not member or member["borrowed_books"]:
        return False
    members.remove(member)
    return True

def borrow_book(member_id, isbn):
    member = find_member(member_id)
    if not member or not book_exists(isbn):
        return False
    book = books[isbn]
    if len(member["borrowed_books"]) >= 3 or book["available"] <= 0:
        return False
    book["available"] -= 1
    member["borrowed_books"].append(isbn)
    return True

def return_book(member_id, isbn):
    member = find_member(member_id)
    if not member or isbn not in member["borrowed_books"]:
        return False
    member["borrowed_books"].remove(isbn)
    books[isbn]["available"] += 1
    return True
