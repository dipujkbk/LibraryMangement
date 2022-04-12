class Library:

    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvilableBooks(self):
        print("Books present in this librabry are: ")
        for book in self.books:
            print(" * "+book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else.Please wait until the book is avilable.")
            return False
        
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book ! Hope you enjoyed it.")

    

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
        



if __name__ =="__main__":
    centralLibrary = Library(["Algorthiims","Django","Clrs","Python Notes"])
    student = Student()
    while True:
        
        WelcomeMsg = '''
        ===== Welcome to Central Library =====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library

        '''
        print(WelcomeMsg)
        a = int(input("enter a choice: "))
        if a==1 :
            centralLibrary.displayAvilableBooks()
        elif a==2 :
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing the central library! Have a great day!")
            exit()
        else:
            print("Invalid Choice!")
        