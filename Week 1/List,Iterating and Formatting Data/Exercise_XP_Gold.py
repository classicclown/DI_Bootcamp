#Ex.1 
strings = "sentences"
print (f"I want to concat two {strings}")

#Ex.2 
for i in range(1500,2500):
    if i%5==0 and i%7==0:
        print (i)

#ex.3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input ("Please enter your name\n")

if name in names:
    print (names.index(name))

#Ex.4
numbers = []
for i in range(1,4):
    number = int(input("Input the "+str(i)+" number"))
    numbers.append(number)
print ("The greatest number is "+str(max(numbers)))

#Ex.5
import string
alphabet = string.ascii_lowercase
for letter in alphabet:
    if letter in 'aeiou':
        print (letter+ " is a vowel")
    else:
        print (letter +" is a consonant") 

#Ex.6
words = input ("Please enter 7 words").split(" ")
letter = input ("Please enter a single character")
for word in words:
    if letter in word:
        print (words.index(word))
        break
    else:
        print ("Letter is not there") 


#Ex.7
my_list = range (1,1000001)
print (sum(my_list))

#Ex.8
input_numbers = input ("Enter numbers seperated by a comma")

numer_tuple = tuple (input_numbers.split(","))
number_list = list (input_numbers.split(","))
print(number_list, numer_tuple)

#Ex.9
import random

user_num = int(input ("Please input a number between 1 and 9\n"))
ran_num = random.randint(1,9)
game_counter =0

while True:
    if user_num==ran_num:
        print ("Winner")
        break
    else:
        print ("Wrong, try again")
        user_num =int(input())
        game_counter+=1

print ("You got it in "+str(game_counter)+" tries")
