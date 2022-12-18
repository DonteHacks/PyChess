import csv
import pandas as pd
from  classes.Piece import Pawn, Knight, Bishop, Rook, Queen, King, Piece
from tabulate import tabulate
import boards
import pathlib

currpath = pathlib.Path(__file__).parent.resolve()

# Define file and rank names
file_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rank_names = ['8', '7', '6', '5', '4', '3', '2', '1']

piece_type_dict = {
   -1 : Pawn('b', '\u265F'), -2 : Knight('b', '\u265E'), -3 : Bishop('b', '\u265D'),
   -4 : Rook('b', '\u265C'), -5 : Queen('b', '\u265B'),  -6 : King('b', '\u265A'),

    0 : Piece(),

    1 : Pawn('w', '\u2659'),  2 : Knight('w', '\u2658'),  3 : Bishop('w', '\u2657'),
    4 : Rook('w', '\u2656'),  5 : Queen('w', '\u2655'),   6 : King('w', '\u2654')
}

# SPOT CLASS
class Spot():
    
    # Instance Variables
    file : str = '' # a - h
    rank : str = '' # 1 - 8
    piece : Piece = None

    # Constructor
    def __init__(self, coords, piece=None):
        self.file = file_names[coords[0]]
        self.rank = rank_names[coords[1]]
        self.piece = piece

    # toString
    def __str__(self):
        return str(self.piece)

# BOARD CLASS
class Board():

    # Instance Variables
    spots_df = None

    # Constructor
    # Creates empty board, but if filename is provided, initializes pieces
    def __init__(self, board_filename=''):
        self.spots_df = pd.DataFrame([[Spot((x,y)) for x in range(0,8)] for y in range(0,8)], index=rank_names, columns=file_names) 

        if board_filename != '':
            # TODO: Implement loading logic here
            # print('Trying to open ' + curr_file_path + '/../board/' + board_filename)
            with open(str(currpath) + '\\\\..\\\\boards\\\\' + board_filename, 'r') as file:
                reader = csv.reader(file, delimiter=',')
                for row, rank in zip(reader, rank_names):
                    for element, file, x in zip(row, file_names, range(0,8)):
                        # print("Element: {} / File: {} / Row: {} / Rank: {} / X {}".format(element, file, row, rank, x))
                        # print(self.spots_df[file][str(rank)].piece)
                        self.spots_df[file][rank].piece : Piece = piece_type_dict[int(element)]

    # spot input is something like 'a8' or 'h5'
    def get_spot(self, spot : str) -> Spot:
        return self.spots_df[spot[0]][spot[1]]

    # Prints spots dataframe in a pretty way using tabulate
    def display_board(self):
        print(tabulate(self.spots_df, headers='keys', tablefmt='grid', stralign='center'))