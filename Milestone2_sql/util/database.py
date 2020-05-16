from typing import List, Dict, Union

from .database_connection import DatabaseConnection

Book = Dict(str,Union(str,int))]


def create_book_table() -> None:
    with DatabaseConnection('database.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)')


def add_book(name: str,author: str) -> None:
    with DatabaseConnection('database.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO books VALUES(?, ?, 0)',(name,author))



def get_all_books() -> List[Book]:
    with DatabaseConnection('database.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books =[{'name' : row[0], 'author': row[1], 'read':row[2]} for row in cursor.fetchall()]   #[(name,author,read),(name,author,read),]
    return books


def mark_book_as_read(name) -> None:
    with DatabaseConnection('database.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name = ?',(name,))


def delete_book(name:str) -> None:
    with DatabaseConnection('database.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE from books WHERE name = ?',(name,))
