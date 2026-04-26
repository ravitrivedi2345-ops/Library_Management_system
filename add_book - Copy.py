from utilis import library

def add_books() -> None:
    book = input("Enter book name to be added: ")
    library.append(book)
    print(f"'{book}' has been added")
