from anagram_checker import AnagramChecker

def menu():
        print ("Welcome to the anagram checker.\nDo you want to check a word (check) or quit(q)?")
        user_choice=input()
        if user_choice.lower()=='check':
            user_choice=input("What word do you want to check?\n")
        elif user_choice.lower()!='q' and user_choice.lower()!='check':
              print("Invalid input")
              user_choice=input("Do you want to check a word(check) or quit(q)?\n")
        return user_choice.strip()

if __name__=="__main__":
        user_word = menu()
        new_check = AnagramChecker()
        while user_word!='q':
              if new_check.is_valid_word(user_word):
                    anagrams=new_check.get_anagrams(user_word)
                    print("You word: "+user_word)
                    print("Anagrams: "+str(anagrams))
                    user_word=menu()
        else:
              print("Thanks for using the anagram checker")
            

    




