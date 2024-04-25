class Book:
    book_id = 1
    def __init__(self,title,author,year):
        self.title = title
        self.year = year
        self.author = author
        self.book_id = Book.book_id
        Book.book_id += 1