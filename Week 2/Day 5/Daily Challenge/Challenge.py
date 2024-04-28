#Challenge 1

def sorted_list(sequence):
    split_list = sequence.split(",")
    split_list.sort()
    print (split_list)

sorted_list("without,hello,bag,world")

#Challenge 2

def longest_word (sentence):
    max_length = max(sentence.split(),key=len)
    print (max_length)

longest_word("A thing of beauty is a joy forever.")
