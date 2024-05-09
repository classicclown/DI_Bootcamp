class AnagramChecker:

    def __init__(self):
        f=open("/Users/ryankopping/Documents/DI_Bootcamp/Week 4/Day 5/Project/anagram.txt",'r')
        self.wordlist=f.read()
        f.close()

    def is_valid_word(self,word):
        is_words=word.strip().split()
        cleaned_word=word.strip()
        if type(cleaned_word) is str and len(is_words)<=1 and cleaned_word.isalnum() and cleaned_word.isalpha():
            return True
        else:
            return False
        

    def is_anagram(self,word1,word2):
        list1=list(word1.lower())
        list2=list(word2.lower())
        list1.sort()
        list2.sort()
        if len(list1)==len(list2):
            if list1==list2:
                return True
        else:
            return False
        
    def get_anagrams(self,user_word):
        anagrams=[]
        words_list=self.wordlist.split()
        for words in words_list:
            if self.is_anagram(words,user_word):
                anagrams.append(words)
        return anagrams





        
        




       
        

