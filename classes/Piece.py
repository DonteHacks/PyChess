# Define file and rank names
file_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rank_names = ['8', '7', '6', '5', '4', '3', '2', '1']

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

    pass

class Bishop(Piece):

    def __init__(self, color='', character='', has_moved=False):
        super().__init__(color, character, has_moved)

    pass

class Rook(Piece):

    def __init__(self, color='', character='', has_moved=False):
        super().__init__(color, character, has_moved)

    pass

class Queen(Piece):

    def __init__(self, color='', character='', has_moved=False):
        super().__init__(color, character, has_moved)

    pass

class King(Piece):

    def __init__(self, color='', character='', has_moved=False):
        super().__init__(color, character, has_moved)

    def get_shadow_moves(self, spot : str):
        shadow_moves = [get_spot_up(spot), get_spot_down(spot), get_spot_left(spot), get_spot_right(spot), get_spot_left_up(spot), get_spot_right_up(spot), get_spot_left_down(spot), get_spot_right_down(spot)]
        output = list(filter(lambda move: move is not None, shadow_moves))
        return output