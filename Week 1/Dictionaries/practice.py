def calculation (a,b):
    result = {}
    result["addition"] = (a+b)
    result ["subtraction"]=(a-b)
    result ["multiplication"] = (a*b)
    result ["division"]=(a/b) if b!=0 else ("Undefined")
    result["mod"]=(a%b) if b!=0 else ("Undefined")
    return result

print (calculation(4,0))

''''
Question 1: Currency Converter Function
Problem Statement:
Write a Python function named convert_currency that takes two 
arguments: an amount (float or integer) and a currency code (string). The function should convert the amount from US dollars to the specified currency and 
return the converted amount. Use a predefined dictionary within the function to store conversion rates for at least three currencies (e.g., EUR, GBP, JPY). 
If the currency code is not in the dictionary, the function should print an error message and return None'
'''

def convert_currency (amount, currency):
    currency_list = {"Eur":1.2, "GBP":0.9,"JPY":0.5}
    if currency not in currency_list:
        return "None"
    else:
        return currency_list[currency]*amount
    
print (convert_currency(400,"Zar"))


''''
Question 2: Filter and Transform List Function
Problem Statement:
Write a function named filter_and_square that accepts a list of numbers. 
The function should filter out all negative numbers and numbers greater than 10, square the remaining numbers, and return the modified list. 
The function should also count how many items were removed and print this count.

def filter_and_square (numbers):
    removed =0
    index=0
    for num in numbers[:]:
        if 0>num>10:
            numbers.remove(num)
            removed+=1
        else:
            numbers[index]=num**2
            index+=1
    return (f"Here is the modified list.{numbers}There were {removed} remocved numbers")

print (filter_and_square([1,4,6,15])) '''

'''
Question 9: Group Anagrams from a List of Words
Problem Statement:
Given a list of words, write a Python function named group_anagrams that groups anagrams together. 
Each group of anagrams should be in a separate list, and the list containing these groups should be returned. 
Words are considered anagrams of each other if they can be rearranged to form the other word. Ignore case sensitivity for anagram comparisons.
# Example usage
words = ["bat", "tab", "listen", "silent", "it", "ti"]
print(group_anagrams(words))
# Output: [['bat', 'tab'], ['listen', 'silent'], ['it', 'ti']]'''

def group_anagrams (list1):
    anagram = []
    for word1 in list1:
        for word2 in list1:
            if word1.sort() == word2.sort():
                anagram.append(word1,word2)
    

print (group_anagrams(["bat", "tab", "listen", "silent", "it", "ti"]))




    



