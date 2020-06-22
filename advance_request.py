import json
import os
from datetime import date
import precon


class advanceRequestForm:
    def __init__(self):
        self.date = "NONE"
        self.applicantName="NONE"
        self.Designation="NONE"
        self.purpose="NONE"
        self.aquireFrom="NONE"
        self.aquireFrom3="NONE"
        self.headOfExp="NONE"
        self.amount="NONE"
        self.finSancNum="NONE"
        self.budgetAval="NONE"
        self.accountholder = "NONE"
        self.IFSCcode = "NONE"
        self.accountNumber = "NONE"
        self.BankName = "NONE"
        self.declaration=False
        self.approved=False
    def takeInput(self):
        self.curdate = str(date.today())
        print('Please enter all the fields:')
        self.applicantName=input('Name of the applicant :')
        if precon.prevadv(self.applicantName)==False:
            print("You cant request advance until your previous advances have been settled.")
            return 
        self.Designation=input('Designation :')
        self.purpose=input('Enter the purpose of advance : ')
        print("Advance required from :")
        print("1.Institute Budget")
        print("2.Department Budget")
        print("3.Other")
        self.aquireFrom=input("select a number from above three : ")
        if int(self.aquireFrom) == 3:
            self.aquireFrom3=input("You selected option 3 so specify the name of other budjet : ")
        self.amount = input("enter amount of advance : ")
        self.finSancNum = input("enter financial sanction number : ")
        self.banktakeInput()
        print("Declaration:\n1) The Advance is required to facilitate an activity or event in ehich various petty expenditures are involved and they are required to be paid in cash")
        print("2) I declare that the amount of advance will be used for Institute work only.")
        print("3) I will settle the Advance within 15 days")
        temp=input("do you agree:(y/n)")
        if temp=="y":
            self.declaration=True
        
    def banktakeInput(self):
        print("BANK DETAILS :-")
        self.accountholder = input("enter account holder name : ")
        self.IFSCcode = input("enter IFSC code : ")
        self.accountNumber = input("enter account number : ")
        self.BankName = input("enter Bank name : ")


def run():
    x = advanceRequestForm()
    x.takeInput()
    if x.declaration==True :
        jsonStr = json.dumps(x.__dict__, indent=4)
        filepath = "requests/"+x.applicantName+".json"
        fout = open(filepath, "w")
        fout.write(jsonStr)
    else :
        print('You have not agreed for the declaration so your request will not be processed')
    return x

# x=run()
