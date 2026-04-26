from utilis import library

def return_book() -> None:
    book = input("Enter book name to be returned: ")
    library.append(book)
    print(f"'{book}' has been returned")
