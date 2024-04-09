#Ex.1 
import math
user_input = input("Please enter list of numbers seperated by a comma\n").split(",")
for num in user_input:
    Q = round(math.sqrt ((2*50*int(num))/30),0)
    print (Q)

#Ex.2
list1 =   [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
for i in list1:
    print (i)

print (list1.sort())
print (sum(list1))
new_list = list1[0],list1[-1]
print(new_list)
big_list=[]
for i in list1:
    if i > 50:
        big_list.append(i)
print (big_list)
small_list=[]
for i in list1:
    if i < 10:
        small_list.append(i)
print (small_list)
 
#Ex.3

interesting = '''Python was created by Guido van Rossum, and first released on February 20, 1991. While you may know the python as a large snake, the name of the Python programming language comes from an old BBC television comedy sketch series called Monty Python's Flying Circus.'''

print (len(interesting))
num_sentence = interesting.split(". ")
print ("The string contains "+str(len(num_sentence))+" sentences")
num_words = interesting.split()
print ("The string contains "+str(len(num_words))+" words")
unique_num_words = set(num_words)
print (("The string contains "+str(len(unique_num_words))+" unique words"))

#Ex.4
text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
words = text.split(" ")
frequency = {}

for word in words:
    frequency[word] = frequency.get(word,0)+1 

for word,freq in frequency.items():
    print(word, freq)


    