class Library:
    def __init__(self,listBook):
        self.books = listBook
         
    def display(self):
        print("Available book list are below : ")
        for i in self.books:
            print("\t *"+i)

    def borrowBook(self,book):
        if book in self.books:
            print(f"You have borrowed {book}. Keep it safe. And don't forget to return it into 30 days !")
            self.books.remove(book)
            return True
        else:
            print("The book u typed has already borowed by someone. When it will available we will notify you!")
            return False
    def returnBook(self,book1):
        self.books.append(book1)
        print("Thanks for reading this book ! Hope you are enjoyed it!")

class student:
    def requestBook(self):
        self.book=input("Enter the name of the book you want to borrow :")
        return self.book
    def returnBook(self):
        self.book=input("Enter the name of the book you want to return :")
        return self.book

Management=Library(["Python","C","C++","Java","C#","DSA Python"])
Student=student()
while (True):
    welcomeMSG='''=======Welocme to the center library=======
    1. Show the list of the book.
    2. Borrow boook 
    3. Return book
    4.Exit the library
    '''
    print(welcomeMSG)
    a=int(input("Enter a choice = "))
    if a == 1:
        Management.display()
    elif a == 2:
         Management.borrowBook(Student.requestBook())
    elif a == 3:
        Management.returnBook(Student.returnBook())
    elif a == 4:
        print("Thanks for choosing the library ")
        exit()
    else:
        print("Invalid choice")

  