import random
def get_words_from_file():
    words = []
    with open('/Users/ryankopping/Documents/DI_Bootcamp/Week 4/Day 4/Exercise XP/words.txt') as f:
        text = f.readlines()
        for word in text:
            words.append(word.lower().strip())
        return words

def get_random_sentence(length):
    word_list=get_words_from_file()
    sentence=''
    for i in range(length):
        word=random.choice(word_list)
        sentence+=word+' '
    return sentence



if __name__=='__main__':
    print('This program makes random sentences')
    while True:
        try:
            length = int(input('How long do you want the sentence to be?\n'))
            break
        except:
            print('Not a number!')
    print(get_random_sentence(length))


#Exercise 2

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

def jsonread():
    data = json.loads(sampleJson)
    print(data['company']['employee']['payable']['salary'])
    data['company']['employee']['birth_date']='1990/02/02'

    with open ('jsonfile.json','w')as f:
        json.dump(data,f)


jsonread()