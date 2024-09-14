import pytest 
from src.my_library import Library

@pytest.fixture(scope='module') # to run only once
def library():
    print('lib...')
    return Library()


def test_insert_book(library):
    title = 'title'
    desc = 'desc'
    author = 'author'
    text = 'text'
    r = library.insert_book(title, desc, author, text)
    expected = f'Inserted book with title: {title}'
    assert r == expected

def test_get_book(library):
    book = {
            'title': 'title',
            'desc' : 'desc',
            'author' : 'author',
            'text' : 'text'
    }
    _ = library.insert_book(book['title'], book['desc'], book['author'], book['text'])
    r = library.get_book(0)
    assert r == book

def test_delete_book(library):

    book = {
            'title': 'title',
            'desc' : 'desc',
            'author' : 'author',
            'text' : 'text'
    }
    
    _ = library.insert_book(book['title'], book['desc'], book['author'], book['text'])
    r = library.remove_book(0)
    assert r == f'Removed Book {book}'
