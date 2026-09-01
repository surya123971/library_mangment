from datetime import datetime, timedelta

from book import Book
from member import Member
from file_handler import save_data, load_data


class Library:

    def __init__(self):

        self.books = {}
        self.members = {}
        self.history = []

        self.load_data()

    # -----------------------------
    # Load Data
    # -----------------------------

    def load_data(self):

        data = load_data()

        for book_id, book in data["books"].items():

            self.books[book_id] = Book(
                book["book_id"],
                book["title"],
                book["author"],
                book["category"],
                book["available"]
            )

        for member_id, member in data["members"].items():

            new_member = Member(
                member["member_id"],
                member["name"],
                member["phone"]
            )

            new_member.borrowed_books = member["borrowed_books"]

            self.members[member_id] = new_member

        self.history = data["history"]

    # -----------------------------
    # Save Data
    # -----------------------------

    def save(self):

        books = {}

        for book_id, book in self.books.items():
            books[book_id] = book.to_dict()

        members = {}

        for member_id, member in self.members.items():
            members[member_id] = member.to_dict()

        save_data(
            books,
            members,
            self.history
        )

    # -----------------------------
    # Add Book
    # -----------------------------

    def add_book(self, book_id, title, author, category):

        if book_id in self.books:
            return False, "Book ID already exists."

        if not book_id or not title or not author or not category:
            return False, "All fields are required."

        book = Book(
            book_id,
            title,
            author,
            category
        )

        self.books[book_id] = book

        self.save()

        return True, "Book added successfully."

    # -----------------------------
    # Add Member
    # -----------------------------

    def add_member(self, member_id, name, phone):

        if member_id in self.members:
            return False, "Member ID already exists."

        if not member_id or not name or not phone:
            return False, "All fields are required."

        member = Member(
            member_id,
            name,
            phone
        )

        self.members[member_id] = member

        self.save()

        return True, "Member registered successfully."

    # -----------------------------
    # Search Books
    # -----------------------------

    def search_books(self, keyword):

        results = []

        keyword = keyword.lower()

        for book in self.books.values():

            if (
                keyword in book.title.lower()
                or keyword in book.author.lower()
                or keyword in book.category.lower()
            ):

                results.append(book)

        return results

    # -----------------------------
    # Issue Book
    # -----------------------------

    def issue_book(self, book_id, member_id):

        if book_id not in self.books:
            return False, "Book not found."

        if member_id not in self.members:
            return False, "Member not found."

        book = self.books[book_id]
        member = self.members[member_id]

        if not book.available:
            return False, "Book is already issued."

        if len(member.borrowed_books) >= 3:
            return False, "Member can borrow maximum 3 books."

        issue_date = datetime.now()
        due_date = issue_date + timedelta(days=14)

        borrowed_book = {
            "book_id": book_id,
            "issue_date": issue_date.strftime("%Y-%m-%d"),
            "due_date": due_date.strftime("%Y-%m-%d")
        }

        member.borrowed_books.append(borrowed_book)

        book.available = False

        self.save()

        return True, (
            "Book issued successfully. "
            f"Due date: {due_date.strftime('%d-%m-%Y')}"
        )

    # -----------------------------
    # Return Book
    # -----------------------------

    def return_book(self, book_id, member_id):

        if book_id not in self.books:
            return False, "Book not found."

        if member_id not in self.members:
            return False, "Member not found."

        member = self.members[member_id]

        borrowed = None

        for item in member.borrowed_books:

            if item["book_id"] == book_id:
                borrowed = item
                break

        if borrowed is None:
            return False, "This member has not borrowed this book."

        return_date = datetime.now()

        due_date = datetime.strptime(
            borrowed["due_date"],
            "%Y-%m-%d"
        )

        late_days = (
            return_date.date() - due_date.date()
        ).days

        if late_days > 0:
            fine = late_days * 5
        else:
            fine = 0

        member.borrowed_books.remove(borrowed)

        self.books[book_id].available = True

        history_record = {
            "member_id": member_id,
            "book_id": book_id,
            "issue_date": borrowed["issue_date"],
            "due_date": borrowed["due_date"],
            "return_date": return_date.strftime("%Y-%m-%d"),
            "fine": fine
        }

        self.history.append(history_record)

        self.save()

        return True, (
            f"Book returned successfully. "
            f"Fine: Rs. {fine}"
        )

    # -----------------------------
    # Get Member Borrowed Books
    # -----------------------------

    def get_borrowed_books(self, member_id):

        if member_id not in self.members:
            return []

        return self.members[member_id].borrowed_books