import sqlite3 

def create_connection():
    return sqlite3.connect('database.sql')

def create_cursor(conn):
    return conn.cursor()

def create_table():
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()
    query = '''
        CREATE TABLE IF NOT EXISTS BOOKS (
            id INT PRIMARY KEY NOT NULL,
            title VARCHAR NOT NULL,
            author VARCHAR NOT NULL,
            description VARCHAR, 
            content TEXT NOT NULL
        )
    '''
    cur.execute(query)

def insert_row(cur, title, author, description, content):
    query = f'''
        INSERT INTO Books (title, author, description, content)
        VALUES ("{title}", "{author}", "{description}", "{content}")
    '''
    return cur.execute(query)


def read_row(cur,id):
    query = f'SELECT * FROM Books WHERE id = {id}'
    cur.execute(query)
    return cur.fetchone()

def create_table_two(cur):
    query = '''
        CREATE TABLE IF NOT EXISTS BOOKS (
            id INT PRIMARY KEY NOT NULL,
            title VARCHAR NOT NULL,
            author VARCHAR NOT NULL,
            description VARCHAR, 
            content TEXT NOT NULL
        )
    '''
    return cur.execute(query)