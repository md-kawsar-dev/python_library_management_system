import save_all_books
def delete_book(all_books):
    title = input("Enter the title of the book you want to delete: ")
    for book in all_books:
        if book["title"].lower() == title.lower():
            all_books.remove(book)
            # Save the updated list of books
            save_all_books.save_all_books(all_books)
            print("Book deleted successfully!")
            return all_books