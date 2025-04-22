import random
import string
from datetime import datetime, timedelta

# Constants
NUM_BOOKS = 1000
NUM_USERS = 500
MAX_BORROW_PER_USER = 5

# Book and User storage
books = []
users = []
borrow_records = []

# Book class
class Book:
    def __init__(self, id, title, author, copies):
        self.id = id
        self.title = title
        self.author = author
        self.copies = copies

# User class
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

# Borrow record
class BorrowRecord:
    def __init__(self, user_id, book_id, date_borrowed):
        self.user_id = user_id
        self.book_id = book_id
        self.date_borrowed = date_borrowed

# Helpers
def random_string(length=5):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def create_books(n):
    for i in range(n):
        books.append(Book(i + 1, f"Book {random_string()}", f"Author {random.choice(string.ascii_uppercase)}", random.randint(1, 5)))

def create_users(n):
    for i in range(n):
        users.append(User(i + 1, f"User {random_string()}"))

def borrow_books():
    for user in users:
        num_to_borrow = random.randint(1, MAX_BORROW_PER_USER)
        borrowed = 0
        while borrowed < num_to_borrow:
            book = random.choice(books)
            if book.copies > 0:
                book.copies -= 1
                borrow_date = datetime.now() - timedelta(days=random.randint(1, 30))
                user.borrowed_books.append(book.id)
                borrow_records.append(BorrowRecord(user.id, book.id, borrow_date))
                borrowed += 1

# Main logic
create_books(NUM_BOOKS)
create_users(NUM_USERS)
borrow_books()

# Output some data
summary = {
    "total_books": len(books),
    "total_users": len(users),
    "total_borrowed": len(borrow_records),
    "sample_users": [(user.id, user.name, len(user.borrowed_books)) for user in users[:5]],
    "sample_books": [(book.id, book.title, book.author, book.copies) for book in books[:5]]
}
summary
