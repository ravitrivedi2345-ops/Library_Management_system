from utilis import library

def view_books() -> None:
    if not library:
        print("No books are present in the library")
    else:
        print("\n--- List of Books ---")
        for idx, book in enumerate(library, 1):
            print(f"{idx}. {book}")
