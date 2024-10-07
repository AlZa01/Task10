import Library
book1 = Library.Book("The Lightning Thief", "Rick Riordan", 2005, 9.99)
book2 = Library.Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997, 10.99)
book3 = Library.Book("The Sea of Monsters", "Rick Riordan", 2006, 10.99)
book4 = Library.Book("The Lord of the Rings", "J.R.R. Tolkien", 1954, 15.99)
book5 = Library.Book("Pride and Prejudice", "Jane Austen", 1813, 8.99)
book6 = Library.Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, 12.99, stoplist=True)

books = [book1, book2, book3, book4, book5, book6]

print("\n#get_info method")
for book in books:
    book.get_info()
    
print("\n#find_most_expensive method")
most_expensive_book = Library.Book.find_most_expensive(books)
if most_expensive_book:
    print("Most expensive book: "+most_expensive_book.title+" by "+most_expensive_book.author+", Price: "+str(most_expensive_book.price))
    
print("\n#set_stoplist method for the book2 (Harry Potter and the Sorcerer's Stone)")    
book2.set_stoplist(True)
book2.get_info()

print("\n#censor method for the book1 (The Lightning Thief by Rick Riordan)")
Library.Book.censor(book1, "Rick Riordan", True)
book1.get_info()
print("\n")