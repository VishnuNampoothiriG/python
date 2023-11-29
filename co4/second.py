class bank:
    def __init__(self,accno,name,accty,bal):
        self.accno=accno
        self.name=name
        self.accty=accty
        self.bal=0
    def deposit(self,dep):
        self.bal=self.bal+dep
        return self.bal
    def withdraw(self,wit):
        self.bal=self.bal-wit
        return self.bal
    def showamount(self):
        print("account holder name:",self.name)
        print("account number:",self.accno)
        print("account type:",self.accty)
        print("balance amount:",self.bal)
accno=int(input("enter your account number:"))
name=input("enter your name:")
accty=input("enter your account type:")
obj=bank(accno,name,accty,bal=0)
obj.showamount()
while(True):
    print("\n MENU")
    print("\n1.DEPOSIT")
    print("\n2.WITHDRAW")
    print("\n3.CHECK BALANCE/DETAILS")
    c=int(input("enter your choice:"))
    if c==1:
        d=int(input("enter the amount you want to deposit:"))
        print("your balance is:",obj.deposit(d))
    elif c==2:
        w=int(input("enter the amount you want to withdraw:"))
        if w>obj.bal:
            print("insufficient balance")
        else:
            print("your balance is:",obj.withdraw(w))

    elif c==3:
        obj.showamount()
    else:
        print("enter a valid choice:")
            
            
            
        
