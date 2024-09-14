class Library:
    def __init__(self):
        self.books = []

    def insert_book(self, title, desc, author, text):
        book = {
            'title' : title,
            'desc' : desc,
            'author': author,
            'text': text
        }
        self.books.append(book)
        return f'Inserted book with title: {book["title"]}'
    
    def get_book(self, id):
        if 0 <= id < len(self.books):
            return self.books[id]
        else:
            return 'Invalid Index'
        
    def remove_book(self, id):
        if 0 <= id < len(self.books):
            book = self.books.pop(id)
            return f'Removed Book {book}'
        else:
            return 'Invalid Index'



