class Text:

    def __init__(self,text):
        self.text=text

    def freq_check(self):
        split_text=self.text.lower().split()
        freq_dict={}
        for word in split_text:
            if word in freq_dict.keys():
                freq_dict[word]+=1
            else:
                freq_dict[word]=1

        # for key,value in freq_dict.items():
        #     print (f'{key}: {value}')
        return freq_dict

    def most_common (self):
        freq_dict=self.freq_check()
        most_common = max(freq_dict, key=lambda x: freq_dict[x])
        print (f'The most common word is: {most_common}')

    def unique(self):
        unique_dict=self.freq_check()
        unique_list=[]
        for key,value in unique_dict.items():
            if value==1:
                unique_list.append(key)
            else:
                continue
        return (f"The unique words are: {unique_list}")

    @classmethod
    def read_file (cls, filename):
        with open (filename,'r') as f:
            text = f.read()
        return cls(text)
        


# text = Text.read_file('/Users/ryankopping/Documents/DI_Bootcamp/Week 4/Day 4/Exercise XP/the_stranger.txt')
# text.most_common()
# print(text.unique())

import string
from stop_words import get_stop_words
class TextModification(Text):

    def __init__(self,text):
        super().__init__(text)
        
    def no_punctuation (self):
        trans_table = str.maketrans('','', string.punctuation)
        no_punc=self.text.lower().translate(trans_table)
        return (no_punc)
    
    def no_stop_words(self):
        no_stopwords = [word for word in self.text.split() if word not in get_stop_words('english')]
        return no_stopwords

    def no_special_char (self):
        trans_table = str.maketrans('','', string.punctuation)
        no_special=self.text.translate(trans_table)
        return (no_special)




text=TextModification('This? is a test. in english!')

print(text.no_special_char())
print(text.no_punctuation())


                

        


# text = Text("A good book would sometimes cost as much as a good house.")
# text.freq_check()
# (text.most_common())
# print(text.unique())