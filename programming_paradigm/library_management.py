
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        _is_checked_out = 0

    def Chekcout(self):
        if (self.title,self.author) in self.books:
            return (self.title, self.author)
    
    def ReturnBook(self):
        pass
        

    
class Library():
    def __init__(self):
        self._books = []
    def add_book(self):
        self._books.append(self.title,self.author)

    def check_out_book(self,title):
        for i in self._books:
            if title != i[0]:
                print(f"{i[0]} by {i[1]}")

    def return_book(selftitle):
        pass 

    def list_available_books(self):
        for i in self._books:
            print(f"{i[0]} by {i[1]}")