class Atm:


    def __init__(self):
        self.pin=""
        self.balance=0
        print("welcome")

        self.menu()



    def menu(self):
         

             print("""
                  what ypu want  to do?
                  1. Enter 1 to create pin
                  2. Enter 2 to deposit
                  3. Enter 3 to withdraw
                  4. Enter 4 to check balance
                  5. Enter 5 to exit
                                      """)    
             user_ch=input("enter the choice")

             if user_ch=="1":
                self.create_pin()


             elif user_ch=="2":
                self.deposit()

             elif user_ch=="3":
                self.withdraw()

             elif user_ch=="4":
                self.check_balance()

             else:
                print("bye")
                breakpoint
            





    def create_pin(self):
        self.pin=input("enter your pin")
        print("created pin succesfully")




    def deposit(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter the amount"))
            self.balance +=amount
            print("amount credited")

        else:
            print("invalid pin")





    def withdraw(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter amount"))
            if amount<self.balance:
                self.balance -=amount

            else:
                print("insufficient funds")

        else:
            print("invalid pin")





    def check_balance(self):
        temp=input("enter your pin")
        if temp==self.pin:
            print(self.balance)

        else:
            print("invalid pin") 


                                                 

obj1=Atm()




