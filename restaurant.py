import sys
import pickle
import os

class restaurant:
    def __init__(self,s,n,p):
        self.sno=s
        self.name=n
        self.price=p
        
    def getprice(self):
        return self.price

    def getsno(self):
        return self.sno

    def modify(self):
        n=raw_input("Enter modified name : ")
        p=float(raw_input("Enter modified price : "))
        self.name=n
        self.price=p
    
    def display(self):
        s=str(self.sno)+"\t\t"+self.name+"\t\t"+str(self.price)
        print s
    
    def __str__(self):
        s="Sno : "+str(self.sno)+"\tName : "+self.name+"\tPrice : "+str(self.price)
        return s

#**********FUNCTION TO GENERATE UNIQUE SERIAL NO***********
#def generate_sno():
#    ctr=0

#******************************MAIN FUNCTION***************************
l=1
while(l==1):
    print "\n\n"
    print "**********HOMEPAGE**********"
    print "1.ADD an item to Menu"
    print "2.REMOVE an item to Menu"
    print "3.MODIFY an item to Menu"
    print "4.DISPLAY Menu"
    print "5.ORDER Food"
    print "6.EXIT"
    ch=input("Enter your choice : ")

#******************************ADDING AN ITEM******************************
    if(ch==1):
        print "ADDING Item"
        #generate_sno()
        rin=open("Menu","ab")
        lp=1
        try:
            while(lp==1):
                s=int(raw_input("Enter serial no : "))
                nam=raw_input("Enter name : ")
                pric=float(input("Enter price : "))
                r1 = restaurant(s,nam,pric)
                print "Values entered by you are :"
                print r1
                pickle.dump(r1,rin)
                lp=int(input("\nPRESS 1 to add more items : "))
        except EOFError:
            print "End Of File Reached. "
        finally:
            rin.close()

#******************************REMOVING AN ITEM******************************
    elif(ch==2):
        print "REMOVING Item"
        print "Enter the sno of item to be deleted : "
        s=int(input())
        flag=0
        f1=open("Menu","rb")
        f2=open("Temp","ab")
        try:
            while True:
                r=pickle.load(f1)
                if(s==r.getsno()):
                    flag=1
                    #DO NOT COPY
                else:
                    pickle.dump(r,f2)
        except EOFError:
            if(flag==0):
                print "Item not present"
            print "End of File Reached"
        finally:
            f1.close()
            f2.close()
                           
        os.remove("Menu")
        os.rename("Temp","Menu")
                           
#******************************MODIFYING AN ITEM******************************
    elif(ch==3):
        print "MODIFYING Item"
        print "Enter the sno of item to be modified : "
        s=int(input())
        flag=0
        f1=open("Menu","rb")
        f2=open("Temp","ab")
        try:
            while True:
                r=pickle.load(f1)
                if(s==r.getsno()):
                    flag=1
                    r.modify()
                    pickle.dump(r,f2)
                else:
                    pickle.dump(r,f2)        
        except EOFError:
            if(flag==0):
                print "Item not present"
            print "End of File Reached"
        finally:
            f1.close()
            f2.close()
                           
        os.remove("Menu")
        os.rename("Temp","Menu")
    
#******************************DISPLAY THE MENU******************************
    elif (ch==4):
        print "**********MENU**********"
        r2=restaurant(0,0,0)
        m="S NO\t\tNAME\t\tPRICE"
        print m
        rout=open("Menu","rb")
        try:
            while True:
                r2=pickle.load(rout)
                r2.display()
        except EOFError:
                rout.close()
                
#******************************ORDER FOOD******************************
    elif (ch==5):
        olp=1
        i=0
        order=[]
        while(olp==1):
            print "Please enter the serial no of food"
            o=int(input())
            order.append(o)
            i+=1
            olp=int(input("\nPress 1 to order more, any other key to generate bill : "))

        bill=open("Bill.txt","w")
        string="BILL OF FARE"
        bill.write(string)
        total=0.0
        r3=restaurant(0,0,0)
        rorder=open("Menu","rb")
        print "\n**********YOUR ORDER**********"
        while(i):
            a=order.pop(i-1)
            rorder.seek(0)
            try:
                while True:
                    r3=pickle.load(rorder)
                    if r3.getsno()==a:
                        print r3.display()
                        total+=r3.getprice()
                        break
            except EOFError:
                print "Serial no",
                print r3.getsno(),
                print " ITEM not present"
            i-=1
        rorder.close()
        print "Amount to be paid : ",
        print total
        bill.close()
        
#*********************************EXIT*******************************
    elif (ch==6):
        sys.exit(0)

    else:
        print "WRONG CHOICE"

l=input("\n\nPress 1 to conitnue to HOMEPAGE : ")
    
