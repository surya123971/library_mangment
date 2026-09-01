import streamlit as st

from library import Library


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="wide"
)


# -----------------------------
# Create Library Object
# -----------------------------

if "library" not in st.session_state:
    st.session_state.library = Library()

library = st.session_state.library


# -----------------------------
# Title
# -----------------------------

st.title("📚 Library Management System")
st.write("Library Automation and Membership System")


# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("Menu")

menu = st.sidebar.radio(
    "Select an option",
    [
        "Dashboard",
        "Add Book",
        "Register Member",
        "Search Books",
        "Issue Book",
        "Return Book",
        "Borrowed Books",
        "Borrowing History"
    ]
)


# ==========================================================
# DASHBOARD
# ==========================================================

if menu == "Dashboard":

    st.header("📊 Dashboard")

    total_books = len(library.books)
    available_books = sum(
        1 for book in library.books.values()
        if book.available
    )
    issued_books = total_books - available_books
    total_members = len(library.members)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Books", total_books)

    with col2:
        st.metric("Available Books", available_books)

    with col3:
        st.metric("Issued Books", issued_books)

    with col4:
        st.metric("Members", total_members)

    st.divider()

    st.subheader("📚 Library Overview")

    if library.books:

        for book in library.books.values():

            status = "Available" if book.available else "Issued"

            st.write(
                f"**{book.title}** — "
                f"{book.author} — "
                f"{book.category} — "
                f"{status}"
            )

    else:
        st.info("No books registered yet.")


# ==========================================================
# ADD BOOK
# ==========================================================

elif menu == "Add Book":

    st.header("📚 Register New Book")

    book_id = st.text_input("Book ID")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    category = st.text_input("Category")

    if st.button("Add Book"):

        success, message = library.add_book(
            book_id,
            title,
            author,
            category
        )

        if success:
            st.success(message)
        else:
            st.error(message)


# ==========================================================
# REGISTER MEMBER
# ==========================================================

elif menu == "Register Member":

    st.header("👤 Register New Member")

    member_id = st.text_input("Member ID")
    name = st.text_input("Member Name")
    phone = st.text_input("Phone Number")

    if st.button("Register Member"):

        success, message = library.add_member(
            member_id,
            name,
            phone
        )

        if success:
            st.success(message)
        else:
            st.error(message)


# ==========================================================
# SEARCH BOOKS
# ==========================================================

elif menu == "Search Books":

    st.header("🔍 Search Books")

    keyword = st.text_input(
        "Enter title, author or category"
    )

    if st.button("Search"):

        if not keyword:
            st.warning("Please enter a search value.")

        else:

            results = library.search_books(keyword)

            if results:

                for book in results:

                    status = (
                        "Available"
                        if book.available
                        else "Issued"
                    )

                    st.write(
                        f"### 📖 {book.title}"
                    )

                    st.write(
                        f"**Book ID:** {book.book_id}"
                    )

                    st.write(
                        f"**Author:** {book.author}"
                    )

                    st.write(
                        f"**Category:** {book.category}"
                    )

                    st.write(
                        f"**Status:** {status}"
                    )

                    st.divider()

            else:
                st.warning("No books found.")


# ==========================================================
# ISSUE BOOK
# ==========================================================

elif menu == "Issue Book":

    st.header("📖 Issue Book")

    if not library.books:
        st.warning("No books available.")

    elif not library.members:
        st.warning("No members registered.")

    else:

        available_books = {
            book_id: book
            for book_id, book in library.books.items()
            if book.available
        }

        if not available_books:

            st.warning("All books are currently issued.")

        else:

            book_id = st.selectbox(
                "Select Book",
                list(available_books.keys()),
                format_func=lambda x:
                f"{x} - {available_books[x].title}"
            )

            member_id = st.selectbox(
                "Select Member",
                list(library.members.keys()),
                format_func=lambda x:
                f"{x} - {library.members[x].name}"
            )

            if st.button("Issue Book"):

                success, message = library.issue_book(
                    book_id,
                    member_id
                )

                if success:
                    st.success(message)
                else:
                    st.error(message)


# ==========================================================
# RETURN BOOK
# ==========================================================

elif menu == "Return Book":

    st.header("↩️ Return Book")

    if not library.members:

        st.warning("No members registered.")

    else:

        member_id = st.selectbox(
            "Select Member",
            list(library.members.keys()),
            format_func=lambda x:
            f"{x} - {library.members[x].name}"
        )

        borrowed_books = library.get_borrowed_books(
            member_id
        )

        if not borrowed_books:

            st.info(
                "This member has no borrowed books."
            )

        else:

            book_ids = [
                item["book_id"]
                for item in borrowed_books
            ]

            book_id = st.selectbox(
                "Select Book",
                book_ids,
                format_func=lambda x:
                f"{x} - {library.books[x].title}"
            )

            if st.button("Return Book"):

                success, message = library.return_book(
                    book_id,
                    member_id
                )

                if success:
                    st.success(message)
                else:
                    st.error(message)


# ==========================================================
# BORROWED BOOKS
# ==========================================================

elif menu == "Borrowed Books":

    st.header("📋 Borrowed Books")

    if not library.members:

        st.info("No members registered.")

    else:

        member_id = st.selectbox(
            "Select Member",
            list(library.members.keys()),
            format_func=lambda x:
            f"{x} - {library.members[x].name}"
        )

        borrowed_books = library.get_borrowed_books(
            member_id
        )

        if borrowed_books:

            for item in borrowed_books:

                book_id = item["book_id"]

                st.write(
                    f"**Book:** {library.books[book_id].title}"
                )

                st.write(
                    f"**Issue Date:** {item['issue_date']}"
                )

                st.write(
                    f"**Due Date:** {item['due_date']}"
                )

                st.divider()

        else:

            st.info("No borrowed books.")


# ==========================================================
# BORROWING HISTORY
# ==========================================================

elif menu == "Borrowing History":

    st.header("📜 Borrowing History")

    if library.history:

        for record in reversed(library.history):

            book_id = record["book_id"]
            member_id = record["member_id"]

            book_title = library.books[book_id].title
            member_name = library.members[member_id].name

            st.write(
                f"### 📖 {book_title}"
            )

            st.write(
                f"**Member:** {member_name}"
            )

            st.write(
                f"**Issue Date:** {record['issue_date']}"
            )

            st.write(
                f"**Due Date:** {record['due_date']}"
            )

            st.write(
                f"**Return Date:** {record['return_date']}"
            )

            st.write(
                f"**Fine:** Rs. {record['fine']}"
            )

            st.divider()

    else:

        st.info("No borrowing history available.")