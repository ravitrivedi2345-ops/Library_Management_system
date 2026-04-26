from utilis import library
def issue_book() -> None:
    book = input("Enter book name to be issued: ")
    if book in library:
        library.remove(book)
        print(f"'{book}' has been issued")
    else:
        print("Book not found")
