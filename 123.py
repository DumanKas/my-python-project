class Data:
    def __init__(self):
        self.data = []

    def add_book(self,key,name_book,author):
        book = {
            'key':key,
            'name_book':name_book,
            'author':author
        }
        self.data.append(book)


    def remove_book(self,key):
        for i in self.data:
            if i['key']== key:
                self.data.remove(i)
                return True
        return False


    def get_book(self,key):
        for i in self.data:
            if i['key'] == key:
                return i
        return None

a = Data()
a.add_book(8,'Duman','Dumann')
a.add_book(4,'asd','asdsa')
a.add_book(2,'asdasd','aasss')
print(a.get_book(2))