
class library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_users(self, user):
        self.users.append(user)

    def show_books(self):
        for book in self.books:
            print(book.show_books())

    def show_users(self):
        for user in self.users:
            print(user.show_user_info())

    def borrow_book(self, id_user, id_book):
     
        user_found = None
        for user in self.users:
            if user.id == id_user:
                user_found = user
                break
        
      
        book_found = None
        for book in self.books:
            if book.id == id_book:
                book_found = book
                break
        
      
        if user_found == None:
            print("User doesnt exist")
            return False
        
       
        if book_found == None:
            print("Book doesnt exist")
            return False
        
       
        if book_found.available == False:
            print("The book is not available")
            return False
        
      
        book_found.available = False
        book_found.borrowed_by = id_user
        print("The book has been borrowed succesfully")
        return True

    def return_book(self, id_user, id_book):
       
        user_found = None
        for user in self.users:
            if user.id == id_user:
                user_found = user
                break
        
      
        book_found = None
        for book in self.books:
            if book.id == id_book:
                book_found = book
                break
        
        
        if user_found == None:
            print("User doesnt exist")
            return False
        
       
        if book_found == None:
            print("Book doesnt exist")
            return False
        
       
        if book_found.available == True:
            print("The book is not borrowed")
            return False
        
      
        if book_found.borrowed_by != id_user:
            print("This user hasnt have the book")
            return False
        
        
        book_found.available = True
        book_found.borrowed_by = None
        print("The book has been returned succesfulyy")
        return True
  
    

    