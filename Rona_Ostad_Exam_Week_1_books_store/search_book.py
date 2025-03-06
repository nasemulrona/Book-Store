def search_book():
    search_isbn = input("Enter ISBN to search: ").strip()

    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        found_books = []  

        for book in books:
            book_details = book.strip().split(" | ")

            if len(book_details) >= 6:  
                title, author, isbn, genre, price, qty = book_details

                if isbn == search_isbn:  
                    found_books.append(book_details)  

        if not found_books:
            print("\n❌ No book found with this ISBN.\n")
        else:
            print("\n🔎 Search Result:")
            print("=" * 73)
            print(f"{'Title':<16}{'Author':<16}{'ISBN':<10}{'Genre':<16}{'Price':<10}{'Qty':<5}")
            print("=" * 73)
            for book in found_books:
                print(f"{book[0]:<16}{book[1]:<16}{book[2]:<10}{book[3]:<16}{book[4]:<10}{book[5]:<5}")
            print("=" * 73)

    except FileNotFoundError:
        print("\n⚠️ No books found! The file does not exist.\n")
