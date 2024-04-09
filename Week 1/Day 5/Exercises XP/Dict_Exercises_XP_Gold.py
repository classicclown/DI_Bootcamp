
# #Ex.1
# birthdays = {"Ryan":"1995/01/27",
#              "Eyal":"1994/04/02",
#              "Mike":"1998/08/08",
#              "Corinne":"1997/06/02",
#              "Debbie":"2000/05/24"}

# print("Welcome to the program! You can look up the birthday of anyone.\nFirst off,please add your own name and birthday")
# user_name=input("Name: ")
# user_birthday=input("Birthday: ")
# birthdays[user_name]=user_birthday
# user = input ("Who's birthday would you like to know?\n")
# if user not in birthdays:
#     print ("Sorry, we don't have that person")
# else:
#     print (f"{user} birthday is: {birthdays[user]}") 

#Ex.4
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print (f"Here are the items and their prices:\n {items.keys()},{items.values()} ")