from game import Game

def get_user_menu_choice():
    user_input=input("\tMenu\n\t(g): Play a new game\n\t(x): Show the score and quit\n")
    while user_input not in ('gx'):
        user_input=("Not a valid input,try again\n")
    return user_input

def print_results(results):
    print (f'These are your results:')
    for result,score in results.items():
        print(f'{result} : {score}')
    print("Thank you for playing!")


if __name__== "__main__":
    user_choice=get_user_menu_choice()
    total_score={'Win':0,"Tie":0,"Loss":0}
    game=Game()
    while user_choice != 'x':
        new_game=game.play()
        if new_game=='Win':
            total_score['Win']+=1
        elif new_game=='Tie':
            total_score['Tie']+=1
        else:
            total_score['Loss']+=1
        user_choice=get_user_menu_choice()
    else:
        print_results(total_score)

    