def add_book(self):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    book = {
        'title': title,
        'author': author,
        'is_borrowed': False
    }
    self.books.append(book)
    print(f"'{title}' by {author} added successfully!\n")

def view_books(self):
    if not self.books:
        print("No books in the library yet.\n")
        return
    print("📚 All Available Books:")
    for idx, book in enumerate(self.books, 1):
        status = "Borrowed" if book['is_borrowed'] else "Available"
        print(f"{idx}. {book['title']} by {book['author']} - {status}")
    print()

def search_book(self):
    query = input("Enter book title or author to search: ").strip().lower()
    found = False
    for book in self.books:
        if query in book['title'].lower() or query in book['author'].lower():
            status = "Borrowed" if book['is_borrowed'] else "Available"
            print(f"Found: {book['title']} by {book['author']} - {status}")
            found = True
    if not found:
        print("Book not found.\n")
    else:
        print()

def borrow_book(self):
    title = input("Enter the title of the book to borrow: ").strip().lower()
    for book in self.books:
        if book['title'].lower() == title:
            if book['is_borrowed']:
                print("Sorry, this book is already borrowed.\n")
            else:
                book['is_borrowed'] = True
                print(f"You borrowed '{book['title']}' successfully!\n")
            return
    print("Book not found.\n")

def return_book(self):
    title = input("Enter the title of the book to return: ").strip().lower()
    for book in self.books:
        if book['title'].lower() == title:
            if book['is_borrowed']:
                book['is_borrowed'] = False
                print(f"You returned '{book['title']}' successfully!\n")
            else:
                print("This book wasn't borrowed.\n")
            return
    print("Book not found.\n")

def menu(self):
    while True:
        print("====== Library Menu ======")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            self.add_book()
        elif choice == '2':
            self.view_books()
        elif choice == '3':
            self.search_book()
        elif choice == '4':
            self.borrow_book()
        elif choice == '5':
            self.return_book()
        elif choice == '6':
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")
 
if name == "main": my_library = Library() my_library.menu()
class Library: def init(self): self.books = []
