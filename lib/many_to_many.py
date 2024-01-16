# import ipdb

class Author:

    all = []
    
    def __init__(self, name):

        self.name = name

        Author.all.append(self)
    
    def contracts(self):
        
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):

        total = 0

        for contract in self.contracts():
            total += contract.royalties
        
        return total

class Book:

    all = []
    
    def __init__(self, title):

        self.title = title

        Book.all.append(self)
    
    def contracts(self):

        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):

        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:

    all = []
    
    def __init__(self, author, book, date, royalties):
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):

        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Needs to be an instance of Author.")

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):

        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("Needs to be an instance of Book")
    
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):

        if isinstance(date, str):
            self._date = date
        else:
            raise Exception("Needs to be a string")
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):

        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception("Needs to be an integer")
    
    def contracts_by_date(date):
        
        return [contract for contract in Contract.all if date == contract.date]


# book = Book("Title")
# author = Author("Name")
# date = '01/01/2001'
# royalties = 40000
# contract = Contract(author, book, date, royalties)

# print(contract.author)
# print(contract.date)
# print(author.date)
# print(author.royalties)

# ipdb.set_trace()