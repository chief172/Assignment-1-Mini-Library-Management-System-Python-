# test.py

from operation import *

# Reset data
books.clear()
members.clear()

# 1. Add book and verify
assert add_book("200", "ML 101", "Tom", "Non-Fiction", 4) is True
assert book_exists("200") is True

# 2. Add member and verify
assert add_member("A01", "Mary", "mary@gmail.com") is True
assert find_member("A01") is not None

# 3. Borrow and fail when no copies left or limit exceeded
assert borrow_book("A01", "200") is True
assert borrow_book("A01", "200") is True
assert borrow_book("A01", "200") is True
assert borrow_book("A01", "200") is False  # 4th borrow should fail (limit or no copies)

# 4. Return all borrowed copies (need to return 3 times because member borrowed 3 copies)
assert return_book("A01", "200") is True
assert return_book("A01", "200") is True
assert return_book("A01", "200") is True

# 5. Delete book
assert delete_book("200") is True

print("✅ All tests passed successfully!")
