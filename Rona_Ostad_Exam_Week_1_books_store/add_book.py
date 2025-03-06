def duplicate(isbn):
    try:
        with open("books.txt", "r") as file:
            for line in file:
                details = line.strip().split(" | ")
                if len(details) < 3:  
                    continue
                
                existing_isbn = details[2] 
                if existing_isbn == isbn:
                    return True
        return False
    except FileNotFoundError:
        return False  

def add_book():
  while True:
    title = input("Enter book title: ").strip()
    if not title.isalpha():
        print("❌ Error: The book title must be a string (letters only).")
        continue

    author = input("Enter author name: ").strip()
    if not author.isalpha():
        print("❌ Error: The author name must be a valid string (letters only).")
        continue

    isbn = input("Enter ISBN: ").strip()
    if not isbn.isdigit():
        print("❌ Error: ISBN must contain only numbers.")
        continue

    if duplicate(isbn):
        print("\n❌ Error: A book with this ISBN already exists! Please check the ISBN and try again.\n")
        continue

    genre = input("Enter book genre: ").strip()
    if not genre.isalpha():
        print("❌ Error: The book genre must be a valid string (letters only).")
        continue

    try:
        price = float(input("Enter book price: ").strip())
        if price <= 0:
            raise ValueError("Price must be a positive number.")
    except ValueError as e:
        print(f"❌ Error: {e}")
        continue

    try:
        quantity = int(input("Enter quantity in stock: ").strip())
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
    except ValueError as e:
        print(f"❌ Error: {e}")
        continue

    with open("books.txt", "a") as file:
        file.write(f"{title} | {author} | {isbn} | {genre} | {price} | {quantity}\n")

    print(f"\n✅ Book added successfully! Book ID: {isbn}\n")
    break