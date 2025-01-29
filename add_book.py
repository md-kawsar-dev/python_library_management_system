from save_all_books import save_all_books
# title,author,isbn,year,price,quantity
def add_book(all_books):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = int(input("Enter the ISBN of the book: "))
    year = int(input("Enter the year of publication: "))
    price = float(input("Enter the price of the book: "))
    quantity = int(input("Enter the quantity of the book: "))
    book = {"title": title, "author": author, "isbn": isbn, "year": year, "price": price, "quantity": quantity}
    all_books.append(book)
    save_all_books(all_books)
    print("Book added successfully!")
    return all_books