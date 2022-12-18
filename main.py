import os
import pathlib
from termcolor import colored
from classes.Board import Board
from classes.Piece import Piece

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
                print(chessboard.get_spot(user_input).piece.get_shadow_moves(user_input))
                input("Enter to continue...")
        else:
            try:
                target = user_input[:2]
                destination = user_input[3:]
                target_piece = chessboard.get_spot(target).piece
                destination_piece = chessboard.get_spot(destination).piece
                shadow_moves = target_piece.get_shadow_moves(target)
                if destination in shadow_moves:
                    if target_piece.color == destination_piece.color:
                        print(colored("\nYOU CAN'T CAPTURE YOUR OWN PIECE, ENTER TO TRY AGAIN...".format(user_input), 'red'))
                        input()
                        continue
                    else:
                        chessboard.get_spot(destination).piece = target_piece
                        chessboard.get_spot(target).piece = Piece()
                        target_piece.has_moved = True
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