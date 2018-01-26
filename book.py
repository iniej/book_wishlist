class Book:

    ''' Represents one book in a user's list of books'''

    NO_ID = -1

    def __init__(self, title, author,  read=False, id=NO_ID, read_date='', rating=''):
        '''Default book is unread, and has no ID'''
        self.title = title
        self.author = author
        self.read = read
        self.id=id
        self.read_date=read_date
        self.rating = rating


    def set_id(self, id):
        self.id = id


    def __str__(self):
        read_str = 'no'
        if self.read:
            read_str = 'yes'
            today = datetime.datetime.now()
            today = str(toda.month)+'/'+str(today.day)+'/'+str(today.year)
        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        template = 'id: {} Title: {} Author: {} Read: {} Rating: {}'
        return template.format(id_str, self.title, self.author, read_str, self.rating)


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read and self.id==other.id and self.read_date== other.read_date and self.rating== other.rating

    # def _rate_(self, other):
        # return self.title == other.title and self.rating == other.rating
