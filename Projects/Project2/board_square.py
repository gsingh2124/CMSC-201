'''
File:           board_square.py
Author:         Gurjinder Singh
Date:           11/15/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Can move do be hitting different tho... Contains board square and piece objects while dictating movability

'''
WHITE = "White"
BLACK = "Black"
global WhiteStarts
global BlackStarts
global WhiteEnds
global BlackEnds
class UrPiece:
    WhiteStarts = []
    BlackStarts = []
    WhiteEnds = []
    BlackEnds = []
    def __init__(self, color, symbol):
        self.color = color
        self.position = None
        self.complete = False
        self.symbol = symbol
    def can_move(self, num_moves):
        # Start Check 1, includes check 3, and rule 5
        if self.position != None:
            if self.color == WHITE:
                if num_moves == 1:
                    if self.position.next_white.piece == None:
                        return True
                    elif self.position.next_white.piece == BLACK:
                        if self.position.next_white.rosette == True:
                            return False
                        elif self.position.next_white.rosette == False:
                            return True
                    else:
                        return False
                if num_moves == 2:
                    if self.position.next_white.next_white.piece == None:
                        return True
                    elif self.position.next_white.next_white.piece == BLACK:
                        if self.position.next_white.next_white.rosette == True:
                            return False
                        elif self.position.next_white.next_white.rosette == False:
                            return True
                    else:
                        return False
                if num_moves == 3:
                    if self.position.next_white.next_white.next_white.piece == None:
                        return True
                    elif self.position.next_white.next_white.next_white.piece == BLACK:
                        if self.position.next_white.next_white.next_white.rosette == True:
                            return False
                        elif self.position.next_white.next_white.next_white.rosette == False:
                            return True
                    else:
                        return False
                if num_moves == 4:
                    if self.position.next_white.next_white.next_white.next_white.piece == None:
                        return True
                    elif self.position.next_white.next_white.next_white.next_white.piece == BLACK:
                        if self.position.next_white.next_white.next_white.next_white.rosette == True:
                            return False
                        elif self.position.next_white.next_white.next_white.next_white.rosette == False:
                            return True
                    else:
                        return False
                if num_moves == 0:

                    return False
            elif self.color == BLACK:
                if num_moves == 1:
                    if self.position.next_black.piece == None:
                        return True
                    elif self.position.next_black.piece == WHITE:
                        if self.position.next_black.rosette == True:
                            return False
                        elif self.position.next_black.rosette == False:
                            return True
                    else:
                        return False
                if num_moves == 2:
                    if self.position.next_black.next_black.piece == None:
                        return True
                    elif self.position.next_black.next_black.piece == WHITE:
                        if self.position.next_black.next_black.rosette == True:
                            return False
                        elif self.position.next_black.next_black.rosette == False:
                            return True
                    else:
                        return False
                if num_moves == 3:
                    if self.position.next_black.next_black.next_black.piece == None:
                        return True
                    elif self.position.next_black.next_black.next_black.piece == WHITE:
                        if self.position.next_black.next_black.next_black.rosette == True:
                            return False
                        elif self.position.next_black.next_black.next_black.rosette == False:
                            return True
                    else:
                        return False
                if num_moves == 4:
                    if self.position.next_black.next_black.next_black.next_black.piece == None:
                        return True
                    elif self.position.next_black.next_black.next_black.next_black.piece == WHITE:
                        if self.position.next_black.next_black.next_black.next_black.rosette == True:
                            return False
                        elif self.position.next_black.next_black.next_black.next_black.rosette == False:
                            return True
                    else:
                        return False
                if num_moves == 0:
                    return False
        # End Check 1
        # Start Check 2, includes check 3
        elif self.position == None:
            if self.color == WHITE:
                if num_moves == 0 or self.complete:
                    return False
                elif num_moves == 1 and not self.complete:
                    if self.WhiteStarts[0].piece == None:#check if any objects of White Starts is empty (should be only 1 start)
                        return True
                    else:
                        return False
                elif num_moves == 2 and not self.complete:
                    if self.WhiteStarts[0].piece.next_white == None:
                        return True
                    else:
                        return False
                elif num_moves == 3 and not self.complete:
                    if self.WhiteStarts[0].piece.next_white.next_white == None:
                        return True
                    else:
                        return False
                elif num_moves == 4 and not self.complete:
                    if self.WhiteStarts[0].piece.next_white.next_white.next_white == None:
                        return True
                    else:
                        return False
            elif self.color == BLACK:
                if num_moves == 0 or self.complete:
                    return False
                elif num_moves == 1 and not self.complete:
                    if self.BlackStarts[0].piece == None:#check if any objects of Black Starts is empty (should be only 1 start)
                        return True
                    else:
                        return False
                elif num_moves == 2 and not self.complete:
                    if self.BlackStarts[0].piece.next_black == None:
                        return True
                    else:
                        return False
                elif num_moves == 3 and not self.complete:
                    if self.BlackStarts[0].piece.next_black.next_black == None:
                        return True
                    else:
                        return False
                elif num_moves == 4 and not self.complete:
                    if self.BlackStarts[0].piece.next_black.next_black.next_black == None:
                        return True
                    else:
                        return False
                # End Check 2
        #Start check 4
        elif self.position.next_black._exit or self.position.next_white._exit:
            if num_moves == 1:
                return True
            else:
                return False
        elif self.position.next_black.next_black._exit or self.position.next_white.next_white._exit:
            if num_moves == 2:
                return True
            else:
                return False
        elif self.position.next_black.next_black.next_black._exit or self.position.next_white.next_white.next_white._exit:
            if num_moves == 3:
                return True
            else:
                return False
        elif self.position.next_black.next_black.next_black.next_black._exit or self.position.next_white.next_white.next_white.next_white._exit:
            if num_moves == 4:
                return True
            else:
                return False
        #End check 4
        else:
            print("No possible moves with current roll")
            return False


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
