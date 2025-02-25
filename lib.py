library = []

def add_book():
    """Add a new book to the library."""
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = int(input("Enter year of publication: "))
    isbn = input("Enter ISBN: ")
    available = True

    book = {"Title": title, "Author": author, "Year": year, "ISBN": isbn, "Available": available}
    library.append(book)
    print(f'Book "{title}" added successfully!')

def view_books():
    """Display all books in the library."""
    if not library:
        print("No books in the library.")
        return
    
    for book in library:
        status = "Available" if book["Available"] else "Borrowed"
        print(f'{book["Title"]} by {book["Author"]} ({book["Year"]}) | ISBN: {book["ISBN"]} | Status: {status}')
    print()

def update_book(isbn):
    """Update the information of a book given its ISBN."""
    for book in library:
        if book["ISBN"] == isbn:
            book["Title"] = input("Enter new title: ")
            book["Author"] = input("Enter new author: ")
            book["Year"] = int(input("Enter new year of publication: "))
            print("Book updated successfully!")
            return
    print("Book not found!")

def delete_book(isbn):
    """Remove a book from the library using its ISBN."""
    for book in library:
        if book["ISBN"] == isbn:
            library.remove(book)
            print(f'Book "{book["Title"]}" deleted successfully!')
            return
    print("Book not found!")

def search_book(title):
    """Searches for a book by its exact title."""
    found_books = [book for book in library if book["Title"].lower() == title.lower()]
    
    if found_books:
        for book in found_books:
            status = "Available" if book["Available"] else "Borrowed"
            print(f'{book["Title"]} by {book["Author"]} ({book["Year"]}) | ISBN: {book["ISBN"]} | Status: {status}')
    else:
        print("No book found with that title.")

def borrow_book(isbn):
    """Mark a book as borrowed if available."""
    for book in library:
        if book["ISBN"] == isbn:
            if book["Available"]:
                book["Available"] = False
                print(f'You borrowed "{book["Title"]}".')
            else:
                print("Book is already borrowed.")
            return
    print("Book not found!")

def return_book(isbn):
    """Mark a book as returned."""
    for book in library:
        if book["ISBN"] == isbn:
            if not book["Available"]:
                book["Available"] = True
                print(f'You returned "{book["Title"]}".')
            else:
                print("Booknot found.")
            return
        
def actions():
    """Actions to be performed in the library."""
    while True:
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")
        
        choice = input("Choose an option (1-8): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            isbn = input("Enter ISBN of book to update: ")
            update_book(isbn)
        elif choice == "4":
            isbn = input("Enter ISBN of book to delete: ")
            delete_book(isbn)
        elif choice == "5":
            title = input("Enter book title to search: ")
            search_book(title)
        elif choice == "6":
            isbn = input("Enter ISBN of book to borrow: ")
            borrow_book(isbn)
        elif choice == "7":
            isbn = input("Enter ISBN of book to return: ")
            return_book(isbn)
        elif choice == "8":
            print("Quit!")
            break
        else:
            print("Please enter a number between 1 and 8.")

actions()