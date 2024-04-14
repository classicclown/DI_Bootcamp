# String: Programming is cool!
# Character: o
# 3

def count_occurance (phrase,letter):
    count=0
    for char in phrase:
        if char == letter:
            count +=1
    print(count)

    
count_occurance("This is a great example","y")

