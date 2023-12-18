class Book:
    def __init__(self, title, author, availability_status=True):
        self.title = title
        self.author = author
        self.availability_status = availability_status

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Availability: {self.availability_status}")

    def update_availability(self, new_status):
        self.availability_status = new_status


class User:
    def __init__(self, id_no, name):
        self.id_no = id_no
        self.name = name
        self.books_borrowed = []

    def display_user_details(self):
        print(f"ID Number: {self.id_no}, Name: {self.name}, Books Borrowed: {', '.join([book.title for book in self.books_borrowed])}")

    def borrow_book(self, book):
        if book.availability_status:
            self.books_borrowed.append(book)
            book.update_availability(False)
            print(f"Book '{book.title}' borrowed successfully by {self.name}.")
        else:
            print(f"Book '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.update_availability(True)
            print(f"Book '{book.title}' returned successfully by {self.name}.")
        else:
            print(f"You have not borrowed the book '{book.title}'.")
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book_to_library(self, title, author):
        new_book = Book(title, author, True)
        self.books.append(new_book)
        print(f"Book '{title}' added to the library.")

    def register_user(self, id_no, name):
        new_user = User(id_no, name)
        self.users.append(new_user)
        print(f"User '{name}' registered with ID number: {id_no}.")
    def handle_borrow_transaction(user_name, id_no, book_title, return_date):
        print("Working on it")
    
    def handle_return_transaction(user_name, id_no):
        print("Working on it")
    def view_book_details(self, book_title):
        book = next((book for book in self.books if book.title == book_title), None)
        if book:
            print(f"Title: {book.title}, Author: {book.author}, Availability: {book.availability_status}")
        else:
            print(f"Book '{book_title}' is not available in the library.")

    def check_borrowed_books(self, user_name):
        user = next((user for user in self.users if user.name == user_name), None)
        if user:
            if user.books_borrowed:
                print(f"{user_name} has borrowed the following books: {', '.join([book.title for book in user.books_borrowed])}")
            else:
                print(f"{user_name} currently has no books borrowed.")
        else:
            print(f"User '{user_name}' is not registered in the library.")


# Sample usage with interactive interface
if __name__ == "__main__":
    library = Library()

    while True:
        print("\nMenu:")
        print("1. Add a book to the library")
        print("2. Register as a new user")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View book details")
        print("6. Check borrowed books")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            library.add_book_to_library(title, author)

        elif choice == "2":
            user_name = input("Enter your name: ")
            id_no = input("Enter your ID: ")
            library.register_user(id_no, user_name)

        elif choice == "3":
            user_name = input("Enter your name: ")
            id_no = input("Enter your ID: ")
            book_title = input("Enter the title of the book you want to borrow: ")
            return_date = input("Enter the return date (YYYY-MM-DD): ")
            library.handle_borrow_transaction(user_name, id_no, book_title, return_date)

        elif choice == "4":
            user_name = input("Enter your name: ")
            id_no = input("Enter your ID: ")
            library.handle_return_transaction(user_name, id_no)

        elif choice == "5":
            book_title = input("Enter the title of the book for which you want to view details: ")
            library.view_book_details(book_title)

        elif choice == "6":
            user_name = input("Enter your name: ")
            library.check_borrowed_books(user_name)

        elif choice == "7":
            print("Exiting the library management system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")