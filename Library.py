class Book:
    def __init__(self, title, author, year, price, stoplist=False):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist
    
    def get_info(self):
        print("Author: "+self.author+", Title: "+self.title+", Year: "+str(self.year)+", Price: "+str(self.price)+", Stoplist: "+str(self.stoplist))
        
    def find_most_expensive(books):
        if not books:
            return None
        most_exp = books[0]
        for book in books:
            if book.price > most_exp.price:
                most_exp = book
        return most_exp
    
    def set_stoplist(self, stoplist):
        self.stoplist = stoplist

    def censor(self, author_name, stoplist):
        if self.author == author_name:
            self.stoplist = stoplist