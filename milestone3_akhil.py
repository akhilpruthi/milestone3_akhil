from datetime import date, timedelta
from datetime import datetime
 
 
class library_management():
    book_list = []
    borrow_list = []
 
    def __init__(self, book_name=None, book_unique_number=None, book_author=None):
        if book_name is not None and book_unique_number is not None and book_author is not None:
            self.book_name = book_name
            self.book_unique_number = book_unique_number
            self.book_author = book_author
 
    def add_book(self):
        self.book_list.append({
            'book_name': self.book_name,
            'book_unique_number': self.book_unique_number,
            'book_author': self.book_author
        })
        print(":::::::::::::::::Book Successfully Added!")
 
    def display_book(self):
        if self.book_list:
            for book in self.book_list:
                print("Book Number: {}, Book Name: {}, Book Author: {}".format(
                    book['book_unique_number'], book['book_name'], book['book_author']))
        else:
            print(":::::::::::No books in the library.")
 
    def search_book(self,user_search):
        for book in self.book_list:
            result = 0
            if user_search in book['book_name']:
                print("ISBN -{}, Book Name -{},Author - {}".format(book['book_unique_number'],book['book_name'],book['book_author']))
                result += 1
            else:
                result -= 1
 
        if result < 0:
            print("Sorry this Book isn't available in the library")
 
        else:
            pass
 
    def borrow_book(self,requested_book):
        found = False
        for i, book in enumerate(self.book_list):
            if requested_book == book['book_unique_number']:
                found = True
                today = date.today()
                return_date = today + timedelta(days=15)
 
                return_date_reformatted = return_date.strftime("%Y-%m-%d")
                print("value to be popped is ::::::::::::",book)
 
                # borrowing book function
                removed_book = self.book_list.pop(i)
                removed_book['return_date'] = return_date_reformatted
                self.borrow_list.append(removed_book)
                # print("Borrowed Book Library:::::::::::",self.borrow_list)
                print(":::::::::::::::::::::ISBN -{}, Book Name -{},Author -{},Date Borrowed - {},Return Day -{}".format(book['book_unique_number'],book['book_name'],book['book_author'],today,return_date))
                break
        if not found:
            print(":::::::::::::::Sorry this Book isn't available in the library:::::::::::::")
 
 
    def return_book(self,returned_book):
        found = False
        for i, book in enumerate(self.borrow_list):
            if returned_book == book['book_unique_number']:
                found = True
                today = date.today()
                return_date_reformatted = datetime.strptime(book['return_date'], "%Y-%m-%d").date()
                book['return_date'] = return_date_reformatted
 
                if book['return_date'] > today:
                    print("You still have time left on your loan.:::::::::::")
                else:
                    fine = 2.5
                    days_overdue = (today - book['return_date']).days
                    fine_amount = fine * days_overdue
                    print("you will be fined ::::::::::::: ${}".format(fine_amount))
               
                # returning book function
                removed_book = self.borrow_list.pop(i)
                self.book_list.append(removed_book)
                # print("returned Book Library:::::::::::",self.book_list)
                print("::::::::::::::::::::ISBN -{}, Book Name -{},Author -{},orginal return date- {},Actual Return Day -{}".format(book['book_unique_number'],book['book_name'],book['book_author'],book['return_date'],today))
                break
 
        if not found:
            print("Sorry this Book isn't available in the borrowed library::::::::")
 
 
while True:
    user_input = int(input("Enter 1. To add a new book\nEnter 2. To view booklist.\nEnter 3. to search for a book\nEnter 4. to lend a book\nEnter 5. to return a book \nEnter 0 to exit.\nEnter choice: "))
 
    if user_input == 1:
        book_unique_number = input("Enter unique number of book: ")
        book_name = input("Enter the name of the book: ")
        book_author = input("Enter author's name: ")
 
        library = library_management(book_name, book_unique_number, book_author)
        library.add_book()
 
    elif user_input == 2:
        library = library_management()
        library.display_book()
 
    elif user_input == 3:
        user_search = input("Enter book name to search : ")
        library = library_management()
        library.search_book(user_search)
 
    elif user_input == 4:
        library = library_management()
        print("Avalaible books in the library:::::::::::")
        library.display_book()
        print("Enter the ISBN of book you want to borrow")
        requested_book = input("Enter book name to borrow : ")
        library.borrow_book(requested_book)
 
    elif user_input == 5:
        library = library_management()
        # library.display_book()
        print("Enter the ISBN of book you want to return")
        return_book = input("Enter BOOK ISBN to return : ")
        library.return_book(return_book)
 
    elif user_input == 0:
        print("::::::::::Exiting the program.")
        break
 
    else:
        print(":::::::::Invalid choice.")