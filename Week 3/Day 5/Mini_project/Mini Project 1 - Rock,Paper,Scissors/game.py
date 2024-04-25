import random

class Game:

    def get_user_item(self):
        user_input=input("Select an item: (r)ock, (p)aper or (s)cissors: ")
        while user_input not in ['r','s','p']:
            user_input=input("Select an item: (r)ock, (p)aper or (s)cissors ")
        else:
            if user_input=='r':
                return 'rock'
            elif user_input=='p':
                return 'paper'
            else:
                return 'scissors'
        
    def get_computer_item():
        options=['rock','paper','scissors']
        comp_choice =random.choice(options)
        return comp_choice
    
    def get_game_result(self,user_item,comp_item):
        result=""
        if user_item=='rock' and comp_item=='scissors' or user_item=='paper' and comp_item=='rock' or user_item=='scissors' and comp_item=='paper':
            result="Win"
        elif user_item==comp_item:
            result="Tie"
        else:
            result="Loss"
        return result
    
    def play(self):
        user_input=self.get_user_item(self)
        comp_input=self.get_computer_item()
        game=self.get_game_result(self,user_input,comp_input)
        print(f"You selected {user_input} and the computer chose {comp_input}. Result: {game}")
        if game=='Win':
            return 'Win'
        elif game=='Tie':
            return 'Tie'
        else:
            return 'Loss'






     


