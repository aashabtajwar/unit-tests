import pytest
import sqlite3
from src.db import create_table, create_connection, create_cursor, create_table_two, insert_row, read_row
from unittest import mock


# @pytest.fixture
# def setUp()

def test_create_connection(mocker):
    mock_connection = mocker.MagicMock()
    mocker.patch.object(sqlite3, 'connect', mock_connection)
    mock_connection.return_value = 'connection'
    ret = create_connection()
    assert ret == 'connection'

    
def test_create_cursor(mocker):
    mock_connect = mocker.MagicMock()
    mocker.patch('sqlite3.connect', mock_connect)
    mock_connect.cursor.return_value = 'cursor'
    re = create_cursor(mock_connect)
    assert re == 'cursor'

def test_create_table(mocker):
    mock_connection = mocker.MagicMock()
    mocker.patch('sqlite3.connect', return_value = mock_connection)
    mock_connection.cursor().execute.return_value = None 
    r = create_table()
    query = '''
        CREATE TABLE IF NOT EXISTS BOOKS (
            id INT PRIMARY KEY NOT NULL,
            title VARCHAR NOT NULL,
            author VARCHAR NOT NULL,
            description VARCHAR, 
            content TEXT NOT NULL
        )
    '''
    mock_connection.cursor().execute.assert_called_with(query)
    assert r == None



def test_create_table_two(mocker):
    mock_connection = mocker.MagicMock()
    mocker.patch('sqlite3.connect', return_value = mock_connection)
    mock_cursor = mock_connection.cursor.return_value
    r = create_table_two(mock_cursor)
    
    query = '''
        CREATE TABLE IF NOT EXISTS BOOKS (
            id INT PRIMARY KEY NOT NULL,
            title VARCHAR NOT NULL,
            author VARCHAR NOT NULL,
            description VARCHAR, 
            content TEXT NOT NULL
        )
    '''
    mock_cursor.execute.assert_called_with(query)

def test_insert_row(mocker):
    mock_connection = mocker.MagicMock()
    mocker.patch('sqlite3.connect', return_value = mock_connection)
    mock_cursor = mock_connection.cursor.reutrn_value
    title = 'harry'
    author = 'rowling'
    description = 'a boy in a train'
    content = 'it starts with a boy stuck in a basement'
    r = insert_row(mock_cursor, title, author, description, content)
    query = f'''
        INSERT INTO Books (title, author, description, content)
        VALUES ("{title}", "{author}", "{description}", "{content}")
    '''
    mock_cursor.execute.assert_called_with(query)


def test_read_row(mocker):
    mock_connection = mocker.MagicMock()
    mocker.patch('sqlite3.connect', return_value = mock_connection)
    mock_cursor = mock_connection.cursor.return_value 
    mock_cursor.fetchone.return_value = ('harry', 'rowling', 'stone story', 'story content')
    id_val = '1'
    r = read_row(mock_cursor, id_val)
    query = f'SELECT * FROM Books WHERE id = {id_val}'
    mock_cursor.execute.assert_called_with(query)

    assert r == ('harry', 'rowling', 'stone story', 'story content')

    # mock_connection.cursor().execute.assert_called_with(query)
    # mock_cursor.execute.assert_called_with(query)

# def test_create_table_two(mocker):
#     # mock_connect = mocker.MagicMock()
#     mock_cursor = mocker.MagicMock()
#     mocker.patch('sqlite3.connect', return_value = mock_connect)
#     mocker.patch('sqlite3.connect.cursor', return_value = mock_cursor)
#     # mock_connect.cursor().execute.return_value = None
#     mock_cursor.execute.return_value = "Cursor_Object"
#     # r = create_table_two(mock_connect.cursor)
#     r = create_table_two(mock_cursor)
#     query = '''
#         CREATE TABLE IF NOT EXISTS BOOKS (
#             id INT PRIMARY KEY NOT NULL,
#             title VARCHAR NOT NULL,
#             author VARCHAR NOT NULL,
#             description VARCHAR, 
#             content TEXT NOT NULL
#         )
#     '''
#     mock_cursor.execute.assert_called_with(query)
#     assert r == "Cursor_Object"
