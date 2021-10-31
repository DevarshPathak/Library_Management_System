import mysql.connector as m
db=m.connect(host="localhost",user="root",passwd="9191",database="library")
c=db.cursor()
c.execute("create table if not exists member(Mem_code varchar(20) primary key,Mem_name varchar(20),Mobile varchar(22),DOM date,Address varchar(50))")


def insert_member():
    try:
        mcode=input("Enter member code : ")
        mname=input("Enter member name : ")
        mob=input("Mobile Number : ")
        dom=input("Date of Membership in format(YYYY-MM-DD) : ")
        add=input("Enter Address : ")
        q="insert into member values('"+mcode+"','"+mname+"','"+mob+"','"+dom+"','"+add+"')"
        c.execute(q,)
        print("****Data Inserted****")
        db.commit()
        
    except:
        print("LOL")


def delete_member():
    try:
        mcode=input("Enter member code that you want to delete : ")
        c.execute("delete from member where Mem_code='"+mcode+"'")
        print("Successfully Deleted")
        db.commit()
    except:
        print("ERROR")

def search_member():
    try:
        press=int(input("Enter 1 to search by mobile no.\nEnter 2 to search by name.\n"))
        if press==1:
            mob=input("Enter Mobile number : ")
            m="%"+mob+"%"
            q="select * from member where mobile like '"+m+"'"
            c.execute(q)
            n=1
            for i in c:
                print("Data",n,":",i)
        elif press==2:
            name=input("Enter name : ")
            n="%"+name+"%"
            q="select * from member where mem_name like '"+n+"'"
            c.execute(q)
            n=1
            for i in c:
                print("Data",n,":",i)
                n=n+1
        else:
            print("Enter correct input")
            search_member()
    except:
        print("ERROR")
            
def display_all():
    try:
        c.execute("select * from member")
        n=1
        for i in c:
            print("Data",n,":",i)
            n=n+1
    except:
        print("Error")
