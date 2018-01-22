#Main program
#test push
import ui, datastore
from book import Book



def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        rate_book()

    elif choice == '6':
        '''added by iniej'''
        sort_list()

    elif choice == '7':
        search_list()



    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)


def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()
    if datastore.set_read(book_id, True):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')

def new_book():
    '''Get info from user, add new book'''
    new_book = ui.get_new_book_info()
    datastore.add_book(new_book)
    ui.message('Book added: ' + str(new_book))

def sort_list():

    '''sort the books'''
    allBooks = datastore.get_books()
    sortBooksByTitle = sorted(allBooks, key = lambda book: book.title)
    sortbooksByAuthor = sorted(allBooks, key = lambda book: book.author)
    sortBy = int(input('Enter 1 to sort by title and 2 to sort by auther: '))
    while True:
        if(sortBy == 1):
            ui.show_list(sortBooksByTitle)
            break
        elif(sortBy == 2):
            ui.show_list(sortbooksByAuthor)
            break
        else:
            print('The entry was incorrect.')
            sortBy = int(input('Enter the correct options: '))


def search_list():
    '''Search for a book'''
    #search = str(input('Enter a title '))
    all_search = datastore.get_books()

    for book in all_search:
        if(search == book.title):
            ui.show_list(book)
        else:
            notFound = ('book not found.')
            ui.show_list(notFound)





def rate_book():
    rate_book = ui.rate_a_book()
    datastore.add_rate(rate_book)
    ui.message('Rating added: ' + str(rate_book))


def quit():
    '''Perform shutdown tasks'''
    datastore.shutdown()
    ui.message('Bye!')


def main():



    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
