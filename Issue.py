import mysql.connector as m
from datetime import date
db=m.connect(host="localhost",user="root",passwd="9191",database="library")
c=db.cursor()
c.execute("create table if not exists issue(Mem_code varchar(20),bookcode varchar(20),issue_date date,return_date date,foreign key(mem_code) references member(mem_code),foreign key(bookcode) references bookrecord(bookcode))")


def issue_book():
    try:
        mcode=input("Enter the member code : ")
        bcode=input("Enter the book code of the book you want to issue : ")
        issued=str(date.today())
        q="insert into issue(Mem_code,bookcode,issue_date) values('"+mcode+"','"+bcode+"','"+issued+"')"
        c.execute(q)
        db.commit()
        print("Book Issued")
    except:
        print("Error")

def return_book():
    try:
        mcode=input("Enter member code : ")
        bcode=input("Enter the book code of the book for return : ")
        rd=str(date.today())
        q="update issue set return_date='"+rd+"' where Mem_code='"+mcode+"' and bookcode='"+bcode+"'"
        c.execute(q)
        db.commit()
        print("Book Returned")
    except:
        print("Error")

def issued_details():
    try:
        q="select m.Mem_code,b.bookcode,issue_date,return_date from Member m,Bookrecord b,issue i where m.Mem_code=i.Mem_code and b.bookcode=i.bookcode"
        c.execute(q)
        n=1
        for i in c:
            print("Data",n,":",i)
            n+=1
    except:
        print("Error")
