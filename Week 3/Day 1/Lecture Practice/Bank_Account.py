class Bank_Account():

    def __init__(self,owner,balance):
        self.name = owner
        self.balance=balance
        print (f"Account for {self.name} created successfully")
        
    def deposit (self,amount):
            self.balance +=amount
            print (f"The account balance is now {self.balance}")

    def withdraw(self,amount):
            if self.balance>amount:
                self.balance-=amount
                print(f"The account balance is now {self.balance}")
            else:
                print("You do not have sufficient funds.")
                withdraw_all=input("Would you like to withdraw what is left in the account?(Y/N) If you select N, it will cancel the transaction.").lower()
                if withdraw_all=="y":
                    self.balance-=self.balance
                    print(f"Your balance is now {self.balance}")
                else:
                    print ("Transaction cancelled")
        
    def transfer (self,other_account, amount):
            if self.balance > amount:
                self.balance -= amount
                other_account.balance += amount
                print ("Funds have been transferred")
            else:
                print ("Inssuficient funds to do the transfer. Transaction aborted")

    def get_balance(self):
            return self.balance

first_account = Bank_Account("Alice",500)
first_account.deposit(500)
first_account.withdraw(2000)
second_account =Bank_Account("Bob",500)
first_account.transfer(second_account,300)
print (f" The balance of {first_account.name} is {first_account.get_balance()}")
print (f" The balance of {second_account.name} is {second_account.get_balance()}")