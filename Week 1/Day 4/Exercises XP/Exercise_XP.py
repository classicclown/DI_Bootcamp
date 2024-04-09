#Ex.1

my_fav_numbers = {4,6,9}
my_fav_numbers.update([1,3])
my_fav_numbers.pop()
friend_fav_numbers ={2,6,8}
new_set = my_fav_numbers.union(friend_fav_numbers)
print (new_set)

#Ex.2
#No, a tuple is imutable

#Ex.3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count=0
for i in basket:
	if i=="Apples":
		apple_count +=1
print ("There are "+str(apple_count)+" apples in the basket")
basket =[]
print (basket)

#Ex.4
#A float is a number with a decimal and an int is a whole number
new_list = []
for i in range(3,11):
	new_list.append(i/2)
print (new_list)

#Ex.5
for i in range(1,21):
	print (i)
	if(i%2==0):
		print ("Index "+str(i)+" is even")

#Ex.6
name = input("Please enter your name\n")

while name != "Ryan":
	name =input("Please enter your name\n")

#Ex.7

list_of_fruits = input ("What is your favorite fruit? If there are multiple, seperate them with a space\n").split(" ")
chosen_fruit = input ("Now type the name of any fruit\n")

for fruit in list_of_fruits:
	if fruit in chosen_fruit:
		print ("You chose one of your favorites")
		break
	else:
		print ("You chose a new one. Enjoy!")

#Ex.8

toppings=[]
print ("Please enter a list of pizza toppings. When you're done, type quit")
while True:
	topping = input ()
	if topping.lower()!="quit":
		toppings.append	(topping)   
	else:
	    break
		

print (toppings)
pizza_cost = (10+len(toppings)*2.5)
print ("The total cost of your pizza is "+ str(pizza_cost)) 

#Ex. 9
ages=[]
ticket_price=0
ages = input ("Please enter all the ages of your family\n").split(" ")
ages = [int(age) for age in ages]
for i in ages:
    if 3<i<12:
        ticket_price+=10
    elif 12<i:
        ticket_price+=15
print ("The price of your ticket is "+str(ticket_price)) 

names = ["Ryan","Ben","Dave","Sam"]
for name in names[:]:
    teen_ages = int(input("Please enter the age for:\n "+name))
    if teen_ages < 16 or teen_ages > 21:
        print("Sorry, "+name+" is the wrong age")
        names.remove(name)
print("The people eligable to watch the movie are "+str(names))

#Ex.10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwich = []

for sandwich in sandwich_orders[:]:
    sandwich_orders.remove(sandwich)
    finished_sandwich.append(sandwich)
    print("I made your "+sandwich)




