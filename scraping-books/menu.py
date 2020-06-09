import logging
from app import books

USER_CHOICE = '''Enter one of the following:
-'b' to look for 5 star books
-'c' to look at the cheapest books
-'n' to just get the next available book on the catalogue
-'q' to exit'

Enter your choice: '''

logger = logging.getLogger('scraping-menu')

def print_best_books():
    logger.info(f'Find best books by rating...')
    best_books = sorted(books,key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info(f'Find best books by price...')
    cheapest_books = sorted(books,key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)

books_generator = (x for x in books)

def get_next_book():
    logger.info(f'Getting next book from generator of all books...')
    print(next(books_generator))


user_choices={
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b','c','n'):
            user_choices[user_input]()
        else:
            print("Please enter a valid comment. ")
        user_input = input(USER_CHOICE)
    logger.debug('Terminating program...')

menu()
