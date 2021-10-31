import Member
import Book
import Issue
import Menu as m

while True:
    print("\n\n\t\t****LIBRARY MANAGEMENT SYSTEM****\n\n\t\t")
    print("1. Member Department")
    print("2. Book Department")
    print("3. Issue/Return Department")
    print("4. Exit")
    n=int(input("Enter Your choice : "))
    if n==1:
        m.Membermenu()
    elif n==2:
        m.Bookmenu()
    elif n==3:
        m.Issuereturnmenu()
    elif n==4:
        break
    else:
        print("Invalid Input")
        x=input("Press any key to continue")
