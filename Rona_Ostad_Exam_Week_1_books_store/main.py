from add_book import add_book
from view_books import view_books
from search_book import search_book
from remove_book import remove_book

def main():
    while True:
        view_books()
        print("\n📚 Book Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("\n📕 Exiting the program. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice! Please enter a number between 1-5.")

#program start here
if __name__ == "__main__":
    main()
