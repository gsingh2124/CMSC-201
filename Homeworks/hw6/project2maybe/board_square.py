'''
File:           board_square.py
Author:         Gurjinder Singh
Date:           11/6/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    practice with classes?

'''
class UrPiece:
    def __init__(self, color, symbol):
        self.color = color
        self.position = None
        self.complete = False
        self.symbol = symbol

    def can_move(self, num_moves):
        if self.position != None:#make sure piece is on the board
            if self.position == BoardSquare.position:#make sure the position of your piece is on the board
                if BoardSquare.enterance == True:#if you are at the enterance
                    if BoardSquare.piece.position != None:#and the position of the board piece is valid
                        if BoardSquare.forbidden != self.position: #if you are not on a forbidden piece
                            return True
                    if BoardSquare.position != None:
                        return False
                elif BoardSquare.enterance == False:
                    return False
            if BoardSquare.exit == _exit:#if out of the board
                if color == "White":#if out of the board, and the next position you can go to is white, you can move
                    if BoardSquare.next_white == None:
                        return True
                    if BoardSquare.next_black != None:#False if its black
                        return False
                else:
                    if color == "Black":#if out of the board, and the next position you can go to is black, you can move
                        if BoardSquare.next_white != None:#if that position is white, False
                            return False
                        if BoardSquare.next_black == None:
                            return True
            else:
                if self.position == BoardSquare.next_white and self.color == "White": #if your position is equal to the position of the next white, and you are white, you can move
                    return True
                if self.position == BoardSquare.next_black and self.color == "Black": #if your position is equal to the position of the next black, and you are black, you can move
                    return True
            if BoardSquare.piece.position == BoardSquare.exit:
                if BoardSquare.position == BoardSquare.exit.position:#if out of the board, and the exit position is next, can move
                    return True
                if BoardSquare.position != BoardSquare.exit.position:#if out of the board and cant move to next position, false
                    return False
            elif BoardSquare.piece.position == BoardSquare.forbidden:#if the position of the piece on the board is forbitten, canot move
                return False
            if BoardSquare.piece.position == BoardSquare.rosette:#if the Position of the picece is rosette
                if BoardSquare.enterance == False:# and if the enterance is falce, canot move
                    return False
                elif BoardSquare.enterance == True:# if it is the enterance, can move
                    return True




class BoardSquare:
    def __init__(self, x, y, entrance=False, _exit=False, rosette=False, forbidden=False):
        self.piece = None
        self.position = (x, y)
        self.next_white = None
        self.next_black = None
        self.exit = _exit
        self.entrance = entrance
        self.rosette = rosette
        self.forbidden = forbidden

    def load_from_json(self, json_string):
        import json
        loaded_position = json.loads(json_string)
        self.piece = None
        self.position = loaded_position['position']
        self.next_white = loaded_position['next_white']
        self.next_black = loaded_position['next_black']
        self.exit = loaded_position['exit']
        self.entrance = loaded_position['entrance']
        self.rosette = loaded_position['rosette']
        self.forbidden = loaded_position['forbidden']

    def jsonify(self):
        next_white = self.next_white.position if self.next_white else None
        next_black = self.next_black.position if self.next_black else None
        return {'position': self.position, 'next_white': next_white, 'next_black': next_black, 'exit': self.exit, 'entrance': self.entrance, 'rosette': self.rosette, 'forbidden': self.forbidden}
