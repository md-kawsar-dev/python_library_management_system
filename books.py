import add_book
import view_all_books
import delete_book
all_books =[]
while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Delete Book")
    print("4. Update Book")
    menu = input("Enter your choice: ")
    if menu == "0":
        print("Thank you for using Library Management System")
        break
    elif menu == "1":
        all_books = add_book.add_book(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        all_books = delete_book.delete_book(all_books)
    elif menu == "4":
        print("Update Book")
    else:
        print("Invalid Choice! Please choose between 0-4")