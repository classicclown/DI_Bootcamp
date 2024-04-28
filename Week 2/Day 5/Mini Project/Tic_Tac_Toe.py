#board = [[" "," "," "],[" "," "," "],[" "," "," "]]

def display_board(board):
    

    row1 = ("*" * 17)
    row2 = ("*   " + " | ".join(board[0]) + "   *")
    row3 = ("*  ---|---|---  *")
    row4 = ("*   " + " | ".join(board[1]) + "   *")
    row6 = ("*   " + " | ".join(board[2]) + "   *")
    print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row3}\n{row6}\n{row1}")
    return (board)
            
def player_input(player):
    player_column = int(input (f"Player {player},choose a column (1-3)"))
    player_row = int (input(f"Player {player}Choose a row (1-3)"))
    if(board[player_row-1][player_column-1]!=" "):
        print("Sorry, that cell is taken already. Try again")
        player_input(player)
    else:
        board[player_row-1][player_column-1]=player

def check_win(board):
    win=False 
    #Check if there is a winner in a row
    for row in range(len(board)):
         if board[row][0]==board[row][1]==board[row][2]!=" ":
             win = True
             break
         elif board[0][row] == board[1][row] == board[2][row]!=" ":
             win=True
         elif board[0][0]==board[1][1]==board[2][2]!=" " or board[0][2]==board[1][1]==board[2][0]!=" ":
            win=True
    return win
    

if __name__=="__main__":
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    player = "X"
    num_turns=1
    print ("Welcome to Tic Tac Toe!")
    display_board(board)
    print ("Player X goes first")
    player_input(player)
    while check_win(board) != True and num_turns<9:
        display_board(board)
        if player == "X":
            player = "O"
        else:
            player ="X"
        player_input(player)
        num_turns+=1
    if check_win(board)==True:
        display_board(board)
        print (f"Congrats, player {player} won")
                
    else:
        display_board(board)
        print("Unlucky, it was a tie.")

    
               


