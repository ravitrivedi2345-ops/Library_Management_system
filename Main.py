from add_book import add_books
from issue_book import issue_book
from return_book import return_book
from view_book import view_books


def main():
    while True:
        print("\nWelcome to the Library System")
        print("1. View Books")
        print("2. Add Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_books()
        elif choice == '2':
            add_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()