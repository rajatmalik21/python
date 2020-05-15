from Milestone2.utils import database2

USER_CHOICE = """
Enter:
-'a' to add a new book
-'l' to list all books
-'r' to mark a book as read
-'d' to delete a book
-'q' to quit

Your Choice: """

def menu():
    database2.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input!='q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_book()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Command unknown. Please try again")
        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input("Enter the name of the book: ")
    author = input("Enter the author of the book: ")

    database2.add_book(name,author)


def list_book():
    books = database2.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read : {read}")



def prompt_read_book():
    name = input("Enter the name of the book you finished reading: ")
    database2.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the name of the book you want to delete: ")
    database2.delete_book(name)

menu()
