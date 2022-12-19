import csv
import pandas as pd
from tabulate import tabulate
import pathlib

currpath = pathlib.Path(__file__).parent.resolve()

# Define file and rank names
file_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rank_names = ['8', '7', '6', '5', '4', '3', '2', '1']

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
    def get_spot(self, spot : str):
        return self.spots_df[spot[0]][spot[1]]

    # Prints spots dataframe in a pretty way using tabulate
    def display_board(self):
        print(tabulate(self.spots_df, headers='keys', tablefmt='grid', stralign='center'))

    def __str__(self):
        return str(self.spots_df)

def get_spot_up(spot : str):
    if spot[1] != '8': return spot[0] + rank_names[rank_names.index(spot[1]) - 1] 
    pass
def get_spot_down(spot : str):
    if spot[1] != '1': return spot[0] + rank_names[rank_names.index(spot[1]) + 1] 
    pass
def get_spot_left(spot : str):
    if spot[0] != 'a': return file_names[file_names.index(spot[0]) - 1] + spot[1]
    pass
def get_spot_right(spot : str):
    if spot[0] != 'h': return file_names[file_names.index(spot[0]) + 1] + spot[1]
    pass
def get_spot_left_up(spot : str):
    if spot[0] != 'a' and spot[1] != '8': return file_names[file_names.index(spot[0]) - 1] + rank_names[rank_names.index(spot[1]) - 1] 
    pass
def get_spot_right_up(spot : str):
    if spot[0] != 'h' and spot[1] != '8': return file_names[file_names.index(spot[0]) + 1] + rank_names[rank_names.index(spot[1]) - 1]
    pass
def get_spot_left_down(spot : str):
    if spot[0] != 'a' and spot[1] != '1': return file_names[file_names.index(spot[0]) - 1] + rank_names[rank_names.index(spot[1]) + 1]
    pass
def get_spot_right_down(spot : str):
    if spot[0] != 'h' and spot[1] != '1': return file_names[file_names.index(spot[0]) + 1] + rank_names[rank_names.index(spot[1]) + 1]
    pass

class Piece():

    color = ''
    character = ''
    has_moved = False
    
    def __init__(self, color='', character='', has_moved=False):
        self.has_moved = has_moved
        self.color = color
        self.character = character
        pass

    def __str__(self):
        return self.character

class Pawn(Piece):

    def __init__(self, color='', character='', has_moved=False):
        super().__init__(color, character, has_moved)

    pass

class Knight(Piece):

    def __init__(self, color='', character='', has_moved=False):
        super().__init__(color, character, has_moved)

    # 'ddru' returns spot down, down, right, up from spot
    def get_spot_from_path(self, path : str, spot : str):
        curr_spot = spot
        function_map = {
                            'l' : get_spot_left,
                            'r' : get_spot_right,
                            'u' : get_spot_up,
                            'd' : get_spot_down
        }
        for letter in path:
            curr_spot = function_map[letter](curr_spot)
            if curr_spot == None:
                return None
        return curr_spot
    
    def get_valid_moves(self, board : Board, spot : str):
        valid_moves = []
        paths = ['ull', 'dll', 'urr', 'drr', 'luu', 'ruu', 'ldd', 'rdd']
        for path in paths:
            target_spot = self.get_spot_from_path(path, spot)
            if target_spot == None:
                continue
            target_color = board.get_spot(target_spot).piece.color
            if target_color == '' or target_color != self.color:
                valid_moves.append(target_spot)
        return valid_moves


class Bishop(Piece):

    def __init__(self, color='', character='', has_moved=False):
        super().__init__(color, character, has_moved)

    def get_valid_diag(self, board : Board, direction : str, spot : str):
        function_map = {
                            'left_up' : get_spot_left_up,
                            'right_up' : get_spot_right_up,
                            'left_down' : get_spot_left_down,
                            'right_down' : get_spot_right_down
        
        }
        output = []
        next_spot = function_map[direction](spot)
        while next_spot != None:
            next_color = board.get_spot(next_spot).piece.color
            if next_color == '':
                output.append(next_spot)
                next_spot = function_map[direction](next_spot)
            elif next_color != self.color:
                output.append(next_spot)
                break
            elif next_color == self.color:
                break
        return output

    def get_valid_moves(self, spot : str):
        valid_moves = []
        valid_moves.extend(self.get_valid_diag('left_up', spot))
        valid_moves.extend(self.get_valid_diag('right_up', spot))
        valid_moves.extend(self.get_valid_diag('left_down', spot))
        valid_moves.extend(self.get_valid_diag('right_down', spot))
        return valid_moves

class Rook(Piece):

    def __init__(self, color='', character='', has_moved=False):
        super().__init__(color, character, has_moved)

    def get_valid_branch(self, board : Board, direction : str, spot : str):
        function_map = {
                            'left' : get_spot_left,
                            'right' : get_spot_right,
                            'up' : get_spot_up,
                            'down' : get_spot_down
        
        }
        output = []
        next_spot = function_map[direction](spot)
        while next_spot != None:
            next_color = board.get_spot(next_spot).piece.color
            if next_color == '':
                output.append(next_spot)
                next_spot = function_map[direction](next_spot)
            elif next_color != self.color:
                output.append(next_spot)
                break
            elif next_color == self.color:
                break
        return output
        

    def get_valid_moves(self, board : Board, spot : str):
        valid_moves = []
        valid_moves.extend(self.get_valid_branch(board, 'left', spot))
        valid_moves.extend(self.get_valid_branch(board, 'right', spot))
        valid_moves.extend(self.get_valid_branch(board, 'up', spot))
        valid_moves.extend(self.get_valid_branch(board, 'down', spot))
        return valid_moves

class Queen(Piece):

    def __init__(self, color='', character='', has_moved=False):
        super().__init__(color, character, has_moved)

    def get_valid_moves(self, spot : str):
        valid_moves : list = Rook.get_valid_moves(spot)
        valid_moves.extend(Bishop.get_valid_moves(spot))
        return valid_moves

    pass

class King(Piece):

    def __init__(self, color='', character='', has_moved=False):
        super().__init__(color, character, has_moved)

    def get_valid_moves(self, board : Board, spot : str):
        all_directions = [get_spot_up(spot), get_spot_down(spot), get_spot_left(spot), get_spot_right(spot), get_spot_left_up(spot), get_spot_right_up(spot), get_spot_left_down(spot), get_spot_right_down(spot)]
        shadow_moves = list(filter(lambda move: move is not None, all_directions))
        # Move validation
        valid_moves = []
        for move in shadow_moves:
            move_color = board.get_spot(move).piece.color
            if move_color == '':
                valid_moves.append(move)
            elif move_color != self.color:
                valid_moves.append(move)
        return valid_moves

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