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


from datetime import datetime
from datetime import date

def until_jan ():
    now=datetime.now()
    target=datetime(2025,1,1,1,1,1,1)
    print(f"The time until Jan 1st,2025 is {target-now}")

until_jan()

def birthday(year,month,day):
    start=datetime(year,month,day,1,1,1)
    now=datetime.now()
    minutes_lived=(now-start).total_seconds()//60
    print (f"Minutes lived: {minutes_lived}")

#birthday(1995,1,27)

from faker import Faker

def add_new_users():
    fake=Faker()
    users=[]
    name=fake.name()
    address=fake.address()
    language_code=fake.language_code()
    new_user = {'name':name,'address':address,'language':language_code}
    users.append(new_user)
    print(users)
    

add_new_users()


