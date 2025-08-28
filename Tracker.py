# importinng important libs
import csv
import os
from datetime import datetime
#class 
class ExpenseTracker:
    def __init__(self, filename="file.csv"):
        self.filename = filename

    def addnew(self,amount,category,date,note): #appends a list of values to the file
        lis=[amount,category,date,note] 
        file_exists = os.path.isfile(self.filename) #checks if the file exists 
        with open(self.filename, "a", newline="") as f: #opens the file with append mode named as f
                writer = csv.writer(f)#writing the values
                if not file_exists: 
                    writer.writerow(["Amount", "Category", "Date", "Note"]) #writes the name
                writer.writerow(lis) 

    def showexp(self):
        counter=0
        with open(self.filename, "r", newline="") as f:
            read=csv.reader(f)
            next(read)
            for row in read:
                 counter+=1
                 print("#########################")
                 print(f"data number.{counter}")
                 print("#########################")
                 print(f"amount={row[0]}")
                 print(f"category={row[1]}")
                 print(f"date={row[2]}")
                 print(f"note={row[3]}\n")

    def totalsp(self):
         with open(self.filename, "r", newline="") as f:
            read=csv.reader(f)
            total=0
            for row in read:
                if row[0].isdigit(): # this skips the header
                    total+=int(row[0]) #calculates the tota;
            print(f"the total expense of all time is Rs. {total}")

    def monthlysp(self,year,month):
        with open(self.filename, "r", newline="") as f:
            read=csv.reader(f)
            total=0
            for row in read:
                if not row or row[0] == "Amount": #skips empty and header rows
                    continue
                try:
                    d = datetime.strptime(row[2], "%Y-%m-%d").date()#conversion into date time format
                    if d.year == year and d.month == month:
                        total += int(row[0])
                except Exception:
                    pass
            print(f"total expense of {year}-{month:02d} is Rs.{total} ")
    def flt_ctg(self,category): #filtering by category
        self.category=category
        counter=0
        with open(self.filename,"r",newline="") as f:
            read=csv.reader(f)
            next(read)
            for row in read:
                if row[1]==self.category:
                    counter+=1
                    print("#########################################")
                    print(f"data number.{counter}")
                    print("#########################################")
                    print(f"amount= {row[0]}")
                    print(f"category= {row[1]}")
                    print(f"date= {row[2]}")
                    print(f"note= {row[3]}\n")

