import os
import pathlib
from termcolor import colored
from classes.Board import Pawn, Knight, Bishop, Rook, Queen, King, Piece
from classes.Board import Board
from classes.Board import piece_type_dict 

currpath = pathlib.Path(__file__).parent.resolve()

# Runner for loading board via user input
def load_board():
    boards = os.listdir(str(currpath) + '\\\\boards')
    os.system('cls')

    while(True):
        print('Enter index of board to load:\n')
        for board, index in zip(boards, range(1, len(boards) + 1)):
            print('\t{}. {}'.format(index , board[:board.index('.')]))
        user_input = input('\n')
        try:
            index = int(user_input) - 1
            if index < 0:
                raise Exception()
            loaded_board = Board(boards[index])
            os.system('cls')
            return loaded_board
        except:
            os.system('cls')
            print(colored("Did not recognize input \"{}\", please select an index from 1 to {}\n".format(user_input, len(boards)), 'red'))
            continue

# Defining this globally so we don't have to take up more
# memory every time a pawn is queened

queening_map = {
    'queen' : 5, 'rook' : 4, 'bishop' : 3, 'knight' : 2
}

def queening_process(color : str):
    while(True):
        user_input = input("\nQueening detected... please enter what type of piece you would like to turn your pawn into:\n\n")
        user_input = user_input.lower()
        try:
            queened_piece_index = queening_map[user_input]
            if color == 'b':
                queened_piece_index *= -1
            queened_piece = piece_type_dict[queened_piece_index]
            return queened_piece
        except:
            print(colored("\n{} IS AN INVALID PIECE, ENTER TO TRY AGAIN...".format(user_input), 'red'))
            input()
            continue

def main():

    chessboard = load_board()
    while(True):
        os.system('cls')
        chessboard.display_board()
        user_input = input('\nPlease enter your move:\n\n')

        if len(user_input) == 1:
            # DEV TOOLS
            if user_input == 'm':
                user_input = input("\nWhich spot's piece would you like to get the valid moves for?\n")
                print(chessboard.get_spot(user_input).piece.get_valid_moves(chessboard, user_input))
                input("Enter to continue...")
        else:
            try:
                target = user_input[:2]
                destination = user_input[3:]
                target_piece = chessboard.get_spot(target).piece
                valid_moves = target_piece.get_valid_moves(chessboard, target)
                if destination in valid_moves:
                    # Check for queening:
                    if isinstance(target_piece, Pawn) and (destination[1] == '8' or destination[1] == '1'):
                        queened_piece = queening_process(target_piece.color)
                        chessboard.get_spot(destination).piece = queened_piece
                        queened_piece.has_moved = True
                    else: 
                        chessboard.get_spot(destination).piece = target_piece
                        target_piece.has_moved = True
                    # Set origin spot to be empty now that its piece moved away
                    chessboard.get_spot(target).piece = Piece()
                else:
                    print(colored("\n{} IS AN INVALID MOVE, ENTER TO TRY AGAIN...".format(user_input), 'red'))
                    input()
                    continue
            except:
                print(colored("\nINVALID INPUT {}, ENTER TO TRY AGAIN...".format(user_input), 'red'))
                input()
                continue
            
if __name__ == "__main__":
    main()