class Book():

    def __init__(self, title, author, isbn, available=True):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=available
        

    def issue_book (self):
        if self.available:
            self.available=False
            print(f"Book {self.title} has been taken out")
        else:
            print (f"{self.title} has already been taken out")

    def return_book (self):
        if self.available == False:
            self.available==True
            print (f"{self.title} has been returned")
        else:
            print (f"{self.titlte} was already returned")

    def __str__(self):
        print (f"Title: {self.title}\nAuthor: {self.author}\nIs Available: {self.available}")

class Library:


    def __init__(self):
        self.books=[]
        pass

    def add_book (self,book):
        self.books.append(book)

    def find_books_by_title(self,title):
        list_of_books=[]
        for books in self.books:
            if books.title == title:
                list_of_books.append(books)
        return list_of_books
    
    def find_books_by_author (self, author):
        list_of_books=[]
        for books in self.books:
            if books.author == author:
                list_of_books.append(books)
        return list_of_books
    
    def list_available (self, title):
        list_of_books=[]
        for books in self.books:
            if books.available == True:
                list_of_books.append(books)
        return list_of_books
        
    def list_all_books (self):
        return (book for book in self.books)

lib = Library()
lib.add_book(Book("1984","George",1291929))
lib.add_book(Book("Run","George",113123))
lib.add_book(Book("Happy","David Yang",929383782))

lib.books

