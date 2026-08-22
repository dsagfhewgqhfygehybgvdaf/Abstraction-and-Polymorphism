class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        is_borrowed=False
    def borrow(self):
        a=input("Would you like to borrow this book?y/n")
        while True:
            if a=='y':
                print("Book borrowed")
                is_borrowed=True
                break
            elif a=='n':
                print("Book not borrowed")
                break
            else:
                print("Please try again")
    def return_book(self):
        b=input("Would you like to return this book?y/n")
        while True:
            if b=='y':
                print("Book returned")
                is_borrowed=False
                break
            elif b=='n':
                print("Book kept")
                break
            else:
                print("Please try again")
obj1=book('Harry Potter', "J.K Rowling")
obj2=book('Diary of a Wimpy Kid',"Jeff Kinney")
obj3=book('Charlie and the Chocolate Factory',"Roald Dahl")
print(obj1.title)
print(obj1.author)
obj1.borrow()
obj1.return_book()
print(obj2.title)
print(obj2.author)
obj2.borrow()
obj2.return_book()
print(obj3.title)
print(obj3.author)
obj3.borrow()
obj3.return_book()    