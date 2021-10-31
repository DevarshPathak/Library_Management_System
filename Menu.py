import Member as m
import Issue as i
import Book as b

def Membermenu():
    while True:
        print("\n****Member Record Management****")
        print("\n1. Add Member Record")
        print("\n2. Delete Member")
        print("\n3. Search Member")
        print("\n4. Display all Member Records")
        print("\n5. Exit")
        n=int(input("Enter Option : "))
        if n==1:
            m.insert_member()
        elif n==2:
            m.delete_member()
        elif n==3:
            m.search_member()
        elif n==4:
            m.display_all()
        elif n==5:
            print("EXIT")
            return
        else:
            print("Incorrect Input")
            Membermenu()

def Bookmenu():
    while True:
        print("\n****Book Management System****")
        print("\n1. Add Book Record")
        print("\n2. Delete Book Record")
        print("\n3. Search Book")
        print("\n4. Edit Book Record")
        print("\n5. Display all Book Records")
        print("\n6. Exit")
        n=int(input("Enter Option : "))
        if n==1:
            b.insert_book()
        elif n==2:
            b.delete_book()
        elif n==3:
            b.search_book()
        elif n==4:
            b.edit_book()
        elif n==5:
            b.display()
        elif n==6:
            print("EXIT")
            return
        else:
            print("Incorrect Input")
            Bookmenu()

def Issuereturnmenu():
    while True:
        print("\n****Issue Return Management****")
        print("\n1. Issue Book")
        print("\n2. Return Book")
        print("\n3. Display all issued Records")
        print("\n4. Exit")
        n=int(input("Enter Option : "))
        if n==1:
            i.issue_book()
        elif n==2:
            i.return_book()
        elif n==3:
            i.issued_details()
        elif n==4:
            print("EXIT")
            return
        else:
            print("Incorrect Input")
            Issuereturnmenu()

    
              
