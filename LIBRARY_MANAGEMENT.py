import os
class Mine_Library:

    def add_book(self):
        self.title = str(input("Enter Title of your Book:"))
        self.author = str(input("Enter Author of your Book:"))
        self.ISBN = int(input("Enter Book_Number of your Book:"))

        with open("book.txt","a") as f:
            f.write(f"Title: {self.title} Author: {self.author} ISBN: {self.ISBN}\n")
        self.book_borrowed=False
        
    def view_books(self):
        print("\n<<All boobks of library>>\n")
        with open("book.txt","r") as f:
            print("List of all books in library:")
            read=f.read()
            print(read)

    def borrow_books(self):
        self.borrow = int(input("Enter the number of the book you want to borrow:"))
        f=open("library_data.txt","r")
        for line in f:
            if f"ISBN: {self.borrow}" in line:
                self.book_borrowed=True
            
        print("You have borrowed the book sucessfully.")
    
    def return_books(self):
        # self.retur = int(input("Enter the number of the book you want to return:"))
        # f=open("library_data.txt","r")
        # for line in f:
        #     if f"ISBN: {self.retur}" in line:
        #         self.book_borrowed=False
        print("You have returned the book sucessfully.")

    def save_record(self):
        os.remove("library_data.txt")
        with open("book.txt","r") as f:
            p=0
            while(p==0):
                n=f.readline()
                if n=="":
                    p=1
                else:
                    with open("library_data.txt","a") as s:
                        t=s.write(f"{n} borrowed:{self.book_borrowed}\n")
        print("Data saved sucessfully")
    
    def load_record(self):
        print("\n<<Your library data>>\n")
        with open("library_data.txt","r") as f:
            print(f.read())


manage=Mine_Library()
while(True):
    print("\n__LIBRARY__\n")
    print("1.Add a book")
    print("2.View all books")
    print("3.Borrow a book")
    print("4.Return a book")
    print("5.Save record")
    print("6.Load record")
    print("7.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        manage.add_book()
    elif choice==2:
        manage.view_books()
    elif choice==3:
        manage.borrow_books()
    elif choice==4:
        manage.return_books()
    elif choice==5:
        manage.save_record()
    elif choice==6:
        manage.load_record()
    elif choice==7:
        print("<<<LIBRARY IS CLOSED>>>")
        break
    else:
        print("Invalid choice. Please choose a valid option.")


    
