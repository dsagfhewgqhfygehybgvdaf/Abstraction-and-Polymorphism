class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False
    def borrow(self):
        if self.is_borrowed==True:
            print("It is already borrowed")
        else:
            self.is_borrowed=True
            print("Book is borrowed")
    def return_book(self):
        if self.is_borrowed==False:
            print("It has not been borrowed")
        else:
            self.is_borrowed=False
            print("Book has been returned")
    def __str__(self):
        if self.is_borrowed:
            return self.title + " by " + self.author+ " [Borrowed]"
        else:
            return self.title+ " by " +self.author+" [Available]"
obj1=Book('Harry Potter', 'JK Rowling')
obj2=Book('Diary of a Wimpy Kid', 'Jeff Kinney')
obj3=Book('The Hunger Games','Suzanne Collins')
print(obj1)
print(obj2)
print(obj3)
while True:
    Borrow=input("Which book would you like to borrow? Please make sure your input is accurate, this system is case-sensitive.")
    if Borrow=='Harry Potter':
        obj1.borrow()
        Borrow_Again=input("Would you like to borrow more books [y/n]? Please make sure your input is accurate, this system is case-sensitive.")
        if Borrow_Again=='y':
            continue
        elif Borrow_Again=='n':
            break
    elif Borrow=='Diary of a Wimpy Kid':
        obj2.borrow()
        Borrow_Again=input("Would you like to borrow more books [y/n]? Please make sure your input is accurate, this system is case-sensitive.")
        if Borrow_Again=='y':
            continue
        elif Borrow_Again=='n':
            break
    elif Borrow=='The Hunger Games':
        obj3.borrow()
        Borrow_Again=input("Would you like to borrow more books [y/n]? Please make sure your input is accurate, this system is case-sensitive.")
        if Borrow_Again=='y':
            continue
        elif Borrow_Again=='n':
            break
    else:
        print("Book is not in library")
        Borrow_Again=input("Would you like to borrow more books [y/n]? Please make sure your input is accurate, this system is case-sensitive.")
        if Borrow_Again=='y':
            continue
        elif Borrow_Again=='n':
            break
    if obj1.is_borrowed and obj2.is_borrowed and obj3.is_borrowed:
        print("You have borrowed all the books.")
        break
while True:
    Return=input("Which book would you like to return? Please make sure your input is accurate, this system is case-sensitive.")
    if Return=='Harry Potter':
        obj1.return_book()
        Return_Again=input("Would you like to return more books [y/n]? Please make sure your input is accurate, this system is case-sensitive.")
        if Return_Again=='y':
            continue
        elif Return_Again=='n':
            break
    elif Return=='Diary of a Wimpy Kid':
        obj2.return_book()
        Return_Again=input("Would you like to return more books [y/n]? Please make sure your input is accurate, this system is case-sensitive.")
        if Return_Again=='y':
            continue
        elif Return_Again=='n':
            break
    elif Return=='The Hunger Games':
        obj3.return_book()
        Return_Again=input("Would you like to return more books [y/n]? Please make sure your input is accurate, this system is case-sensitive.")
        if Return_Again=='y':
            continue
        elif Return_Again=='n':
            break
    else:
        print("Book is not in library")
    if not obj1.is_borrowed and not obj2.is_borrowed and not obj3.is_borrowed:
            print("You have returned all the books.")
            break

print(obj1)
print(obj2)
print(obj3)
