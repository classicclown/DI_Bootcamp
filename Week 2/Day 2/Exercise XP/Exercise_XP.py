def display_message():
    print ("We are learning functions")

display_message()

#Ex.2

def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Dune")

#Ex.3

def describe_city(city,country):
    print(f"{city} is in {country}")

describe_city("Cape Towb","South Africa")

#Ex.4
import random
def rand_number (number):
    random_num = random.randint(0,100)
    if number == random_num:
        print ("Success")
    else:
        print (f"Fail. Number 1 is {number}, number 2 is {random_num}")

rand_number(49)

#Ex.5 

def make_shirts(size="L",text="I love python"):
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirts("M")

#Ex 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians (magicians):
    for name in magicians:
        print (name)

def make_great (magicians):
    for index,value in enumerate(magicians):
        magicians[index]+=" the Great"
        

    return magicians


print(make_great(magician_names))
show_magicians(magician_names)