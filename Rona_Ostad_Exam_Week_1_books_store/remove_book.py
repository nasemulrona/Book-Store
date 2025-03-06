def remove_book():
    remove_isbn = input("Enter ISBN of the book to remove: ").strip()

    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        updated_books = []
        book_found = False

        for book in books:
            book_details = book.strip().split(" | ") 
    
            if len(book_details) > 2:
                isbn = book_details[2]  

                if isbn == remove_isbn:
                    book_found = True 
                    continue  
            
            updated_books.append(book)  

        if not book_found:
            print("\n❌ No book found with this ISBN.\n")
            return

        
        with open("books.txt", "w") as file:
            for book in updated_books:
                file.write(book)

        print("\n✅ Book removed successfully!\n")

    except FileNotFoundError:
        print("\n⚠️ No books found! The file does not exist.\n")
