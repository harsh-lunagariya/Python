class Library:
    books = {
        101: {"title": "Python Basics", "author": "Naveen", "status": "Available"},
        102: {"title": "Data Structures", "author": "Alice", "status": "Borrowed"},
    }
    def add_book(self,book_id,title,author,status="Available"):
        self.books[book_id] = {"title":title,"author":author,"status":status}
        
    def display_books(self):
        for i in self.books:
            print(self.books[i])

class Books:
    def __init__(self,id,title,author,status="Available"):
        self.book_id = id
        self.title = title
        self.author = author
        self.status = status

class User:
    def __init__(self,id,name,age):
        self.user_id = id
        self.user_name = name
        self.age = age


l1 = Library()
l1.add_book(103,"Kings Road","Bob")
l1.display_books()
