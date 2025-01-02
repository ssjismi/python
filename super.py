class Publisher:
    def __init__(self, name):
        self.name = name
    def display_publisher(self):
        return f"Publisher: {self.name}" 
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author
    def display_book(self):
        return f"Title: {self.title}\nAuthor: {self.author}"
class Python(Book):
    def __init__(self, name, title, author, price,no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages
    def display_info(self):
        publisher_info = self.display_publisher()
        book_info = self.display_book()
        return f"{publisher_info}\n{book_info}\nPrice:${self.price}\nNumber of Pages: {self.no_of_pages}" 

python_book = Python("O'Reilly Media", "Learning Python", "Mark Lutz", 39.99, 1600) 
 
print(python_book.display_info())
