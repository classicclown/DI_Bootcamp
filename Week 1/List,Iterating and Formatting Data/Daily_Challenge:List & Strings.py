number = int(input ("Input a number you want the multiples of"))
length = int(input ("How many multiples do you want?"))
i = 1
while i <= length:
    print(i*number)
    i+=1

user_string = input("Please enter a string\n")
no_dupes=""
for letter in user_string:
    if letter not in no_dupes:
        no_dupes += letter
    else:
        continue
print (no_dupes)