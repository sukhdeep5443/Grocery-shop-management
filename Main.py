import mysql.connector as mc
con=mc.connect(host="localhost",user="root",password="tiger",database="grocery")
cur=con.cursor()

import random as ran

import admin.create as cre
import admin.delete as dele
import admin.modify as modi
import customer.read as r

#admin
r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Grocery Shop.txt")
ki=input("Enter your choice (Administrator/Customer) : ")
if ki=="Administrator":
    query="select * from admin"
    cur.execute(query)
    eb=cur.fetchall()
    ko=input("Enter Your User_Name : ")
    kp=int(input("Enter Your Password : "))
    for i in eb:
        if i[0]==ko and i[1]==kp:
            while True:
                r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Adminsitrator.txt")
                ch=int(input("Enter Your Choice : "))
                if ch==1:
                    cre.create(input("Enter category of product : "),
                    input("Enter product name : "),
                    int(input("Enter ID of Product : ")),
                    int(input("Enter quantity of product : ")),
                    int(input("Enter cost of product : ")),
                    int(input("Enter Discount : ")),
                    int(input("Enter selling price of product : ")))
                    print("Your product is created....")
                                  
                elif ch==2:
                    dele.delete(input("Enter category of product : "),
                    int(input("Enter ID of Product to be deleted : ")))
                    print("Your product is deleted....")
    
                elif ch==3:
                    modi.modifyquantity(input("Enter category of product : "),
                    int(input("Enter New Quantity of Product : ")),
                    int(input("Enter ID of Product : ")))
                    print("Your Stock Quantity Of product is modified....")
                elif ch==4:
                    query="select * from workers"
                    cur.execute(query)
                    e=cur.fetchall()
                    print("| Worker_Name                       ","| Age ","| Phone Number ","| Date_Of_Joining ","| Salary ","| Address                    |")


                    for i in e:
                        print("|",i[0]," "*(33-len(i[0])),"|",
                        i[1]," "*(3-len(str(i[1]))),"|",
                        i[2]," "*(12-len(str(i[2]))),"|",
                        i[3]," "*(15-len(str(i[3]))),"|",
                        i[4]," "*(6-len(str(i[4]))),"|",
                        i[5]," "*(25-len(i[5])),"|")
                    
                elif ch==5:
                    query="select * from customer"
                    cur.execute(query)
                    e=cur.fetchall()

                    for i in e:
                        print(i)
                ui=input("Wanna go back to home page (Yes/No) : ")
                if ui=="No":
                    break
            break
    else:
        print("INCORRECT USER_NAME / PASSWORD !!!!!!")
    #elif ch==6:
        #query="select * from bakery_and_bread where Stock_Quantity
            
    
elif ki=="Customer":
    a1=input("Enter your Name : ")
    b1=int(input("Enter your Phone Number : "))
    c1=input("Enter Current Date : ")

#Customer   
    l=[]
    while True:
         r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Varities.txt")
         ch=int(input("Enter your choice : "))
         if ch==1:
             while True:
                 r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Bakery and Bread.txt")
                 x=input("Enter Name of your required product : ")
                 b=int(input("Enter Quantity : "))
               
                 query="select * from bakery_and_bread where Product_Name='{}'".format(x)
                 cur.execute(query)
                 e2=cur.fetchone()
               
                 e1=list(e2)
                 e1[2]=b
                 e1[3]=e1[3]*b
                 e1[4]=e1[4]*b
                 e1[5]=e1[5]*b
                 l.append(e1)
                 query="update bakery_and_bread set Stock_Quantity={} where Product_Name='{}'".format(e2[2]-b,x)
                 cur.execute(query)
                 con.commit()
                 ag=input("Wanna enter More from This Category, State Yes Or No : ")
                 if ag=="No":
                      break
                  
                       
         elif ch==2:
                  
             while True:
                 r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Bathroom Essentials.txt")
                 x=input("Enter Name of your required product : ")
                 b=int(input("Enter Quantity : "))
                 query="select * from bathroom_essentials where Product_Name='{}'".format(x)
                 cur.execute(query)
                 e2=cur.fetchone()    
                 e1=list(e2)
                 e1[2]=b
                 e1[3]=e1[3]*b
                 e1[4]=e1[4]*b
                 e1[5]=e1[5]*b
                 l.append(e1)
                 query="update bathroom_essentials set Stock_Quantity={} where Product_Name='{}'".format(e2[2]-b,x)
                 cur.execute(query)
                 con.commit()
                 ag=input("Wanna enter More from This Category, State Yes Or No : ")
                 if ag=="No":
                     break
         elif ch==3:
        
              while True:
                 r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Cereals and Rice.txt")
                 x=input("Enter Name of your required product : ")
                 b=int(input("Enter Quantity : "))
                 query="select * from cereals_and_rice where Product_Name='{}'".format(x)
                 cur.execute(query)
                 e2=cur.fetchone()
                 e1=list(e2)
                 e1[2]=b
                 e1[3]=e1[3]*b
                 e1[4]=e1[4]*b
                 e1[5]=e1[5]*b
                 l.append(e1)
                 query="update cereals_and_rice set Stock_Quantity={} where Product_Name='{}'".format(e2[2]-b,x)
                 cur.execute(query)
                 con.commit()
                 ag=input("Wanna enter More from This Category, State Yes Or No : ")
                 if ag=="No":
                     break

         elif ch==4:
              
              while True:
                  r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Chips and Biscuits.txt")
                  x=input("Enter Name of your required product : ")
                  b=int(input("Enter Quantity : "))
                  query="select * from chips_and_biscuits where Product_Name='{}'".format(x)
                  cur.execute(query)
                  e2=cur.fetchone()
                  e1=list(e2)
                  e1[2]=b
                  e1[3]=e1[3]*b
                  e1[4]=e1[4]*b
                  e1[5]=e1[5]*b
                  l.append(e1)
                  query="update chips_and_biscuits set Stock_Quantity={} where Product_Name='{}'".format(e2[2]-b,x)
                  cur.execute(query)
                  con.commit()
                  ag=input("Wanna enter More from This Category, State Yes Or No : ")
                  if ag=="No":
                      break

         elif ch==5:
              
              while True:
                 r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Dairy, Cheese, and Eggs.txt")
                 x=input("Enter Name of your required product : ")
                 b=int(input("Enter Quantity : "))
                 query="select * from diary_cheese_and_eggs where Product_Name='{}'".format(x)
                 cur.execute(query)
                 e2=cur.fetchone()
                 e1=list(e2)
                 e1[2]=b
                 e1[3]=e1[3]*b
                 e1[4]=e1[4]*b
                 e1[5]=e1[5]*b
                 l.append(e1)
                 query="update diary_cheese_and_eggs set Stock_Quantity={} where Product_Name='{}'".format(e2[2]-b,x)
                 cur.execute(query)
                 con.commit()
                 ag=input("Wanna enter More from This Category, State Yes Or No : ")
                 if ag=="No":
                     break

         elif ch==6:
              
              while True:
                 r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Drinks.txt")
                 x=input("Enter Name of your required product : ")
                 b=int(input("Enter Quantity : "))
                 query="select * from drinks where Product_Name='{}'".format(x)
                 cur.execute(query)
                 e2=cur.fetchone()
                 e1=list(e2)
                 e1[2]=b
                 e1[3]=e1[3]*b
                 e1[4]=e1[4]*b
                 e1[5]=e1[5]*b
                 l.append(e1)
                 query="update drinks set Stock_Quantity={} where Product_Name='{}'".format(e2[2]-b,x)
                 cur.execute(query)
                 con.commit()
                 ag=input("Wanna enter More from This Category, State Yes Or No : ")
                 if ag=="No":
                     break

         elif ch==7:
              
              while True:
                 r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Dry Fruits.txt")
                 x=input("Enter Name of your required product : ")
                 b=int(input("Enter Quantity : "))
                 query="select * from dry_fruits where Product_Name='{}'".format(x)
                 cur.execute(query)
                 e2=cur.fetchone()
                 e1=list(e2)
                 e1[2]=b
                 e1[3]=e1[3]*b
                 e1[4]=e1[4]*b
                 e1[5]=e1[5]*b
                 l.append(e1)
                 query="update dry_fruits set Stock_Quantity={} where Product_Name='{}'".format(e2[2]-b,x)
                 cur.execute(query)
                 con.commit()
                 ag=input("Wanna enter More from This Category, State Yes Or No : ")
                 if ag=="No":
                     break
         elif ch==8:
              
              while True:
                 r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Household Essentials.txt")
                 x=input("Enter Name of your required product : ")
                 b=int(input("Enter Quantity : "))
                 query="select * from household_essentials where Product_Name='{}'".format(x)
                 cur.execute(query)
                 e2=cur.fetchone()    
                 e1=list(e2)
                 e1[2]=b
                 e1[3]=e1[3]*b
                 e1[4]=e1[4]*b
                 e1[5]=e1[5]*b
                 l.append(e1)
                 query="update household_essentials set Stock_Quantity={} where Product_Name='{}'".format(e2[2]-b,x)
                 cur.execute(query)
                 con.commit()
                 ag=input("Wanna enter More from This Category, State Yes Or No : ")
                 if ag=="No":
                     break

         elif ch==9:
              
              while True:
                 r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Ice Creams and Chocolates.txt")
                 x=input("Enter Name of your required product : ")
                 b=int(input("Enter Quantity : "))

                 query="select * from icecreams_and_chocolates where Product_Name='{}'".format(x)
                 cur.execute(query)
                 e2=cur.fetchone()

                 e1=list(e2)
                 e1[2]=b
                 e1[3]=e1[3]*b
                 e1[4]=e1[4]*b
                 e1[5]=e1[5]*b
                 l.append(e1)
                 query="update icecreams_and_chocolates set Stock_Quantity={} where Product_Name='{}'".format(e2[2]-b,x)
                 cur.execute(query)
                 con.commit()
                 ag=input("Wanna enter More from This Category, State Yes Or No : ")
                 if ag=="No":
                     break

         elif ch==10:
              
              while True:
                 r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Meat and Seafood.txt")
                 x=input("Enter Name of your required product : ")
                 b=int(input("Enter Quantity : "))
                 query="select * from meat_and_seafood where Product_Name='{}'".format(x)
                 cur.execute(query)
                 e2=cur.fetchone()
                 e1=list(e2)
                 e1[2]=b
                 e1[3]=e1[3]*b
                 e1[4]=e1[4]*b
                 e1[5]=e1[5]*b
                 l.append(e1)
                 query="update meat_and_seafood set Stock_Quantity={} where Product_Name='{}'".format(e2[2]-b,x)
                 cur.execute(query)
                 con.commit()
                 ag=input("Wanna enter More from This Category, State Yes Or No : ")
                 if ag=="No":
                     break

         elif ch==11:
              
              while True:
                 r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Oils, Sauces and Condiments.txt")
                 x=input("Enter Name of your required product : ")
                 b=int(input("Enter Quantity : "))
                 query="select * from oils_sauces_and_condiments where Product_Name='{}'".format(x)
                 cur.execute(query)
                 e2=cur.fetchone()
                 e1=list(e2)
                 e1[2]=b
                 e1[3]=e1[3]*b
                 e1[4]=e1[4]*b
                 e1[5]=e1[5]*b
                 l.append(e1)
                 query="update oils_sauces_and_condiments set Stock_Quantity={} where Product_Name='{}'".format(e2[2]-b,x)
                 cur.execute(query)
                 con.commit()
                 ag=input("Wanna enter More from This Category, State Yes Or No : ")
                 if ag=="No":
                     break

         elif ch==12:
              
              while True:
                 r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Vegetables and fruits.txt")
                 x=input("Enter Name of your required product : ")
                 b=int(input("Enter Quantity : "))
                 query="select * from vegetables_and_fruits where Product_Name='{}'".format(x)
                 cur.execute(query)
                 e2=cur.fetchone()
                 e1=list(e2)
                 e1[2]=b
                 e1[3]=e1[3]*b
                 e1[4]=e1[4]*b
                 e1[5]=e1[5]*b
                 l.append(e1)
                 query="update vegetables_and_fruits set Stock_Quantity={} where Product_Name='{}'".format(e2[2]-b,x)
                 cur.execute(query)
                 con.commit()
                 ag=input("Wanna enter More from This Category, State Yes Or No : ")
                 if ag=="No":
                     break
    
         w=input("Wanna Go Back To Home Page???.............(Yes/No)..")
         if w=="No":
             break

    s=0
    di=0
    for i in l:
        s+=i[5]
        di+=i[4]

    print("Your Subtotal is : ",s)

    ax=input("Enter Mode of Payment (Cash/Credit Card/Debit Card) : ")

    if ax=="Cash":
         ab=int(input("Enter amount You give : "))

    x1=input("Enter Rating [Worst,Satisfactory,Good,Best,Excellent] : ")

    r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Invoice1.txt")

    ai=ran.randrange(10000,99999)

    print("INVOICE NO. : ",ai)

    print("| Product_Name                       ","| Quantity ","| Marked Price ","| Special Discount ","| Selling Price  |")


    for i in l:
         print("|",i[0]," "*(34-len(i[0])),"|",
         i[2]," "*(8-len(str(i[2]))),"|",
         i[3]," "*(12-len(str(i[3]))),"|",
         i[4]," "*(16-len(str(i[4]))),"|",
         i[5]," "*(13-len(str(i[5]))),"|")

    print("Mode of Payment : ",ax)
    if ax=="Cash":
         print("SUBTOTAL : ",s)
         print("You gave : ",ab)
    
         print("Change you Received : ",ab-s)
    elif ax=="Credit Card" or ax=="Debit Card":
         print("SUBTOTAL : ",s)
         print("You gave : ",s)

    print("You Saved : ",di)

    z=len(l)

    print("Total no. of products purchased : ",z)
    r.readfile("C:\\Users\\Sabby\\Desktop\\Python Project\\Invoice2.txt")

    #Adding customer details to database
    query="insert into customer values('{}',{},'{}',{},{},'{}',{},'{}')".format(a1,b1,c1,ai,z,ax,s,x1)
    cur.execute(query)
    con.commit()
