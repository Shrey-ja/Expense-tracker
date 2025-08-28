from datetime import datetime
from Tracker import ExpenseTracker
#this takes the user input so we don't have to validate the input each time
def gtin(input_message,cast_fun=str,condition=lambda x:True,er_msg="Invalid try again"):
    '''inpm takes the input message, cast_fun takes the data type you want your data to be
    condition parameter takes a condition and then error message desplays the error message'''
    while True:
        try:
            value=cast_fun(input(input_message))
            if not condition(value):
                print(er_msg)
                continue
            return value
        except ValueError:
            print("INVALID..!! Try again!")
            pass
#this is so the user can exit the program
def endloop():
    a=gtin("Do you want to do something else? y for yes and n for no (y/n)>>",str,er_msg="enter a value from 1-6 only")
    return a
#just to make the category selection easier
def CoE(category):
        if category==1:
            return "FOOD"
        elif category==2:
            return "TRAVEL"
        elif category==3:
            return "STUDIES"
        elif category==4:
            return "MEDICAL"
        elif category==5:
            return "PERSONAL"
        elif category==6:
            return "OTHERS"
def ptm():
    print("1.Food")
    print("2.Travel")
    print("3.Studies")
    print("4.Medical")
    print("5.Personal")
    print("6.Others")

l=ExpenseTracker()

ans ="y"
while ans!= "n": 
    #menu
    print("choose your num\n""1. add\n""2.Show expense\n""3.TOTAL\n""4.Monthly spent\n""5.search by cetegory\n""6.exit\n")
    a=gtin("your Choic number 1-6 only=>",int,lambda x:x<=6 and x>0,"invalid value try a num between 1-6")
    # try:
    #     a=int(input("your choice.. =")) #selection for the menu
    # except ValueError:
    #      print("enter 1-5 only") #error handling incase user inputs incorrect value
    #      continue
    if a==1 :
            amount=gtin("Enter spent Amount=>",cast_fun=int,er_msg="it should be a number only") #using the gtin function
            ptm()
            cat=gtin("Enter Category=>",cast_fun=int,condition=lambda x:x>0 and x<6,er_msg="it should be a number only 1-6")
            c=CoE(category=cat)
            valid_date= gtin("Enter date (YYYY-MM-DD): ",cast_fun=lambda x: datetime.strptime(x,"%Y-%m-%d").date(),er_msg="Invalid date format! Please use YYYY-MM-DD.")
            note=input("enter a note if you want, else type none-")
            l.addnew(amount,c,valid_date,note) #adding the new entries to the csv file
            ans=endloop()
    elif a==2:
        l.showexp()
        ans=endloop()
    elif a==3:
            l.totalsp()
            ans=endloop()
    elif a==4:
        try:    
            year=int(input("enter the year="))
            month=int(input("enter the month(01-12)="))
            l.monthlysp(year,month)
            ans=endloop()
        except Exception:
            continue
    elif a==5:
        #menu
        print("******************************\n")
        ptm()
        cate_n=gtin("enter a valid category",int,condition=lambda x: 1 <= x <= 6,er_msg="invalid category(1-6 only)")
        cate=CoE(cate_n)
        l.flt_ctg(cate)
        ans=endloop()
    elif a==6:
         break
    else:
         print("try again")
print("Thank you for using :3")#end


