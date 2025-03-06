def view_books():
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        if not books:
            print("\n📖 No books found in the store.\n")
            return

        print("\n📚 Book List:")
        print("=" * 73)
        print(f"{'Title':<16}{'Author':<16}{'ISBN':<10}{'Genre':<16}{'Price':<10}{'Qty':<5}")
        print("=" * 73)

        for book in books:
            book_details = book.strip().split(" | ")
            
            if len(book_details) == 6:
                print(f"{book_details[0]:<16}{book_details[1]:<16}{book_details[2]:<10}{book_details[3]:<16}{book_details[4]:<10}{book_details[5]:<5}")
            else:
                book.strip()

        print("=" * 73)

    except FileNotFoundError:
        print("\n❌ Error: The file 'books.txt' does not exist. Add some books first.\n")

