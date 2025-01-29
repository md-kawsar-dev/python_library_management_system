
def save_all_books(all_books):
    with open("all_books.csv", "w") as file:
        file.write("title,author,isbn,year,price,quantity\n")
        for book in all_books:
            file.write(f'{book["title"]},{book["author"]},{book["isbn"]},{book["year"]},{book["price"]},{book["quantity"]}\n')
    
