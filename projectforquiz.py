class Book1:

    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

class Book2:

    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

class Book3:

    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

ob1 = Book1("Alice In Wonderland", "Nick Michael", False)
ob2 = Book2("The Farlands", "Susan Tritty", True)
ob3 = Book3("The Boy Who Drew The Universe", "Nate McWatkinss", False)

question = input("Do you want to borrow a book or bring it back? (borrow/bring): ")
question1 = int(input("Which book do you want to borrow or give back? (1/2/3): "))
question2 = int(input("Which book do you want to borrow(1, 2, 3): "))

if question == "bring":
    if question1 == 1:
        if ob1.is_borrowed == True:
            print("Thank you!")
            ob1.is_borrowed == False
    if question1 == 2:
            if ob2.is_borrowed == True:
                print("Thank you!")
                ob2.is_borrowed == False
    if question1 == 3:
            if ob3.is_borrowed == True:
                print("Thank you!")
                ob3.is_borrowed == False

if question == "borrow":
    if question2 == 1:
      if ob1.is_borrowed == False:
        print("You borrowed the book, do not forget to bring it!")
        ob1.is_borrowed == True
    else:
        print("This book is borrowed, please try anoter one.")

    if question2 == 2:
      if ob2.is_borrowed == False:
        print("You borrowed the book, do not forget to bring it!")
        ob1.is_borrowed == True
    else:
        print("This book is borrowed, please try anoter one.")

    if question2 == 3:
      if ob3.is_borrowed == False:
        print("You borrowed the book, do not forget to bring it!")
        ob3.is_borrowed == True
    else:
        print("This book is borrowed, please try anoter one.")