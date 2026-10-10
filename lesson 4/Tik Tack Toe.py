import random
from colorama import init, Fore, style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + style.RESET_ALL
        else:
            return Fore.GREEN + cell + style.RESET_ALL
        print(''+colored(board[0])+'|'+colored(board[1])+'|'+colored(board[2]))
        print(Fore.PURPLE + '--+----+--' + style.RESET_ALL)
        print(''+colored(board[3])+'|'+colored(board[4])+'|'+colored(board[5]))
        print(Fore.Pink + '--+----+--' + style.RESET_ALL)
        print(''+colored(board[6])+'|'+colored(board[7])+'|'+colored(board[8])) 
        print()
        
def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.YELLOW + "Choose your symbol (X/O): ").upper()
    if symbol == 'X':
            return ('X','O')
    else:
        return ('O','X')
    
def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or board[move-1].isdigit():
        try:
            move = int(input(Fore.CYAN + "Enter your move (1-9): ")) - 1
            if move not in range(1, 10) or board[move - 1].isdigit():
                print(Fore.RED + "Invalid move. Please try again.")
        except ValueError:
            print(Fore.RED + "Please enter a number between 1 and 9.")
        board[move - 1] = symbol  
        
 