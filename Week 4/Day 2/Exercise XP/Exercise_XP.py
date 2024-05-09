class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount>1:
            return (f"{self.amount} {self.currency}s")
        else:
            return (f"{self.amount} {self.currency}")

    def __int__(self):
        return self.amount
    
    def __repr__(self):
        return (str(self))
    
    def __add__(self,other):
        if isinstance (other,int):
            return self.amount+other
        else:
            if self.currency==other.currency:
                return self.amount+other.amount
            else:
                raise TypeError (f"Cannot add between Currency type <{self.currency}> and <{other.currency}")
            
    def __iadd__(self,other):
        if isinstance (other,int):
            return self.amount+other
        elif other is not int:
            if self.currency==other.currency:
                return self.amount+other.amount
            else:
                raise TypeError (f"Cannot add between Currency type <{self.currency}> and <{other.currency}")
            
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

# result=c1+5
# print (result)
# result=c1+c2
# print (result)
# c1+=5
# print(c1)
# c1+=c2
# print(c1)
# #result=c1+c3

from func import add_nums
a=1
b=2
add_nums(a,b)

import string
import random

def rand_gen_string():
    letters=string.ascii_letters
    rand_string = "".join(random.choice(letters) for i in range (5))
    print (rand_string)

(rand_gen_string())


import datetime
#from datetime import date

def current_date():
    print (datetime.date.today())

current_date()

def until_jan ():
    day = datetime.date.today()
    hour=datetime.datetime.now().hour
    minute=datetime.datetime.now().minute
    jan = datetime.datetime(2025,1,1,8,0,0)
    until_jan=jan-(day,hour,minute)
    print(f"The time until Jan 1s,2025 is {until_jan}")

until_jan()