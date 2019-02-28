nano 01-Basics-ClassesandObjects04.py # create the file

# create a bank account class that has two attributes: owner, balance
# and two methods: deposit, withdraw
# As an added requirement, withdrawals may not exceed the available balance.
class Account(object):
    def __init__(self, owner="Test", balance=0):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return "Account owner: %s, Account balance: %d" %(str(self.owner), int(self.balance))
    def deposit(self, amounttodeposit):
        self.balance = self.balance + amounttodeposit
        print("%s, %d is successfully deposited to you account, your new balance is: %d." %(self.owner, int(amounttodeposit), int(self.balance)))    
    def withdraw(self, amounttowithdraw):
        if(self.balance>=amounttowithdraw):
            self.balance = self.balance - amounttowithdraw
            print("%s, %d is successfully withdrawn you account, your new balance is: %d." %(self.owner, int(amounttowithdraw), int(self.balance)))    
        else:
            print("%s, your balance is %d, you can't withdraw %d." %(self.owner, int(self.balance), int(amounttowithdraw)))
objAccount = Account("Naeem", 100)
print(objAccount)
objAccount.deposit(500)
objAccount.deposit(750)
objAccount.withdraw(1000)
objAccount.withdraw(500)
objAccount.withdraw(300) 

# now execute the file 
python 01-Basics-ClassesandObjects04.py
