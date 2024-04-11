# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
word = input ("Please enter a word\n")
dict1 = {}
for index,letter in enumerate(word):
    if letter in dict1.keys():
        dict1[letter]+=[index]
    else:
        dict1[letter]=[index]

print(dict1)

#Ex.2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"}

afford=[]
wallet=300
items_purchase = {key:int(value.replace("$","").replace(",","")) for key,value in items_purchase.items()}
for key,value in items_purchase.items():
    if int(value)<(wallet):
        afford.append(key)

if len(afford)==0:
    print ("Nothing")
    print(sorted(afford))
else:
    print (sorted(afford))