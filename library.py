from book import Book
class Library:
    def __init__(self):
        self.books = []

    def create(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)

    def read(self, book_id):
        for i in self.books:
            if i.book_id == book_id:
                return i
        return None


    def update(self,book_id,new_book):
        found = False
        for i in self.books:
            if i.book_id == book_id:
                i.title = new_book.title
                i.author = new_book.author
                i.year = new_book.year

                found = True
                break
        if not found:
            print('Ошибка')

    def delete(self, book_id):
        found = False
        for i in self.books:
            if i.book_id == book_id:
                self.books.remove(i)
                found = True
                break
        if not found:
            print('Ошибка')

