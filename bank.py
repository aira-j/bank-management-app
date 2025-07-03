#welcoming user
print("welcome to the Bank Management App")

# defining class
class BankAccount:
    def __init__(self, name, accountno, password):
        self.name=name
        self.accountno=accountno
        self.password=password
        self.balance=0
        self.transaction_history=[] 
                        
# depositing money function
    def Deposit(self):
        try:
            d=int(input("how much amount you want to enter: "))
            if d<=0:
                print("enter a valid amount")
                return
            
            self.balance+=d
            self.transaction_history.append(f"added Rs.{d} successfully")
        except ValueError:
            print("enter a valid amount")

# withdrawing money function    
    def Withdraw(self):
        try:
            w=int(input("enter amount you want to withdraw: "))
            if w<=0:
                print("enter a positive amount")
                return
            elif w>self.balance:
                print("sufficient balance not present")
                return
            else:
                self.transaction_history.append(f"withdrawn Rs.{w} successfully")
                print("money withdrawn successfully")
        except ValueError:
            print("enter a valid amount")

#asking user credentials
name=input("Enter your name: ")
accountno=input("Enter your accountno: ")
password=input("Enter a password: ")

myaccount=BankAccount(name, accountno, password)

#menu
while True:
    print("What do you want to do?: \n"
        "1. Deposit money \n"
        "2. Withdraw money \n"
        "3. Check balance \n"
        "4. View transaction history \n"
        "5.Exit")
    try:
        option=int(input("choose from 1/2/3/4/5"))
        choice=[1,2,3,4,5]
        if option in choice:
            if option==1:
                myaccount.Deposit()
                print()

            elif option==2:
                myaccount.Withdraw()
                print()

            elif option==3:
                print("your balance is", myaccount.balance)
                print()

            elif option==4:
                print("your transaction history is:")
                sno=1
                for i in myaccount.transaction_history:
                    print(sno, ".", i)
                    sno+=1
                print()
                
            elif option==5:
                break

        else:
            print("You can choose only from 1/2/3/4")
            continue
    except ValueError:
        print("enter a valid value")
        continue
        

          


                

