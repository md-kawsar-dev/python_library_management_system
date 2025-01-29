
def view_all_books(all_books):
    if len(all_books) == 0:
        print("No books available!")
        return None
    print("All Books")
    print("Title\tAuthor\tISBN\tYear\tPrice\tQuantity")
    for book in all_books:
        print(f'{book["title"]}\t{book["author"]}\t{book["isbn"]}\t{book["year"]}\t{book["price"]}\t{book["quantity"]}')
    return all_books