'''
File:           royal_game_of_ur.py
Author:         Gurjinder Singh
Date:           11/15/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    the dreaded game of ur...fun but not fun to try and make, heres my attempt
                cmsc201 retake next semester here I come

'''

from sys import argv
from random import choice
from board_square import BoardSquare, UrPiece


class RoyalGameOfUr:
    STARTING_PIECES = 7

    def __init__(self, board_file_name):
        self.players = {}
        self.board = None
        self.load_board(board_file_name)
        self.num_pieces = 0

    def load_board(self, board_file_name):
        import json
        try:
            with open(board_file_name) as (board_file):
                board_json = json.loads(board_file.read())
                self.num_pieces = self.STARTING_PIECES
                self.board = []
                for x, row in enumerate(board_json):
                    self.board.append([])
                    for y, square in enumerate(row):
                        self.board[x].append(BoardSquare(x, y, entrance=(square['entrance']), _exit=(square['exit']), rosette=(square['rosette']), forbidden=(square['forbidden'])))

                else:
                    for i in range(len(self.board)):
                        for j in range(len(self.board[i])):
                            if board_json[i][j]['next_white']:
                                x, y = board_json[i][j]['next_white']
                                self.board[i][j].next_white = self.board[x][y]
                            if board_json[i][j]['next_black']:
                                x, y = board_json[i][j]['next_black']
                                self.board[i][j].next_black = self.board[x][y]

        except OSError:
            print('The file was unable to be opened. ')

    def draw_block(self, output, i, j, square):
        """
        Helper function for the display_board method
        :param output: the 2d output list of strings
        :param i: grid position row = i
        :param j: grid position col = j
        :param square: square information, should be a BoardSquare object
        """
        MAX_X = 8
        MAX_Y = 5
        for y in range(MAX_Y):
            for x in range(MAX_X):
                if x == 0 or y == 0 or x == MAX_X - 1 or y == MAX_Y - 1:
                    output[MAX_Y * i + y][MAX_X * j + x] = '+'
                if square.rosette and (y, x) in [(1, 1), (1, MAX_X - 2), (MAX_Y - 2, 1), (MAX_Y - 2, MAX_X - 2)]:
                    output[MAX_Y * i + y][MAX_X * j + x] = '*'
                if square.piece:
                    # print(square.piece.symbol)
                    output[MAX_Y * i + 2][MAX_X * j + 3: MAX_X * j + 5] = square.piece.symbol

    def display_board(self):
        """
        Draws the board contained in the self.board object

        """
        if self.board:
            output = [[' ' for _ in range(8 * len(self.board[i // 5]))] for i in range(5 * len(self.board))]
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if not self.board[i][j].forbidden:
                        self.draw_block(output, i, j, self.board[i][j])

            print('\n'.join(''.join(output[i]) for i in range(5 * len(self.board))))

    def get_moves(self, player, num_moves):# Returns a list of possible moves based on the player and its roll
        get_moves = []
        for piece in player:
            if piece.can_move(num_moves):#uses can_move to determine if the move is possible
                get_moves.append(piece)
            return get_moves

    def continue_playing(self, players):
        for player in players:
            if all((piece.complete for piece in players[player])):#if all the pieces of the opposing player are complete
                return False
            return True #if there is a piece that hasent finished yet

    def make_move(self, the_piece, roll):
        if the_piece.position:#if the piece is on the board, move it to its desired position
            x, y = the_piece.position.position
            self.board[x][y].piece.position = None
            self.board[x][y].piece = None
            position = self.board[x][y]
        else:#if the piece isnt on the board, enter it on the board with num_moves-1
            roll -= 1
            if the_piece.color == "White":
                position = UrPiece.WhiteStarts[0]
            else:
                position = UrPiece.BlackStarts[0]
        for i in range(roll):
            if the_piece.color == "White":#ups the position once
                position = position.next_white
            else:
                if the_piece.color == "Black":#ups the position once
                    position = position.next_black
                if position: #if there is a piece on that position, take their piece
                    x, y = position.position
                    the_piece.position = self.board[x][y]
                    self.board[x][y].piece = the_piece
                    if self.board[x][y].piece:
                        print(str(self.board[x][y].piece.symbol) + " has been knocked off")
                        self.board[x][y].piece.position = None#reset square to none
                        self.board[x][y].piece = None
                else:#if the piece reaches the end
                    the_piece.position = None
                    the_piece.complete = True
                    print(str(the_piece.symbol) + " has made it to the end.")
                return position#returns the move

    def get_players(self):#Get the player names, as well as create the symbols and numbers for the number of starting pieces
        #White
        player_name = input("What is your name? ")
        self.players[player_name] = [UrPiece("White", "W{}".format(i + 1)) for i in range(self.STARTING_PIECES)]
        print(player_name + " you will play as white.")
        #Black
        player_name = input("What is your name? ")
        self.players[player_name] = [UrPiece("Black", "B{}".format(i + 1)) for i in range(self.STARTING_PIECES)]
        print(player_name + " you will play as white.")

    def take_turn(self, player, roll):
        get_moves = self.get_moves(player, roll)#gets possible moves for the player
        for i, move in enumerate(get_moves):#account for each possible move per piece
            if not move.position:
                print(str(i + 1) + str(move.symbol) + " currently off the board")
            else:
                print(str(i + 1) + str(move.symbol) +  move.position.position)
        else:
            for piece in player:#Asks for the players moves until all the pieces are acounted for
                if piece.complete:#checks if the current piece is completed
                    print(str(piece.symbol) + " made it off the board.")
                if len(range(get_moves)) > 0 and roll:
                    move = int(input("Which move do you wish to make? "))
                    if move not in range(1 + len(get_moves) + 1):
                        move = int(input("Selection error, please choose another "))
                    else:
                        endpos = self.make_move(get_moves[(move - 1)], roll)
                        if endpos and endpos.rosette:
                            return True
                        else:
                            print("No moves are possible with the current dice roll. ")
                        return False

    def roll_d4_dice(self, n=4):
        """
        :param n: the number of tetrahedral d4 to roll, each with one dot on
        :return: the result of the four rolls.
        """
        dots = 0
        for _ in range(n):
            dots += choice([0, 1])
        else:
            return dots

    def play_game(self):
        turn = 0
        self.get_players()
        players = list(self.players.keys())
        player = self.players[players[turn]]
        if self.board == False:
            print("Cannot load from given board-file name")
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].entrance == "White":#add the starts to the list in ur piece
                        UrPiece.WhiteStarts.append(self.board[i][j])
                else:
                    if self.board[i][j].entrance == "Black":
                            UrPiece.BlackStarts.append(self.board[i][j])
                if self.board[i][j].exit == "White":#add the ends to the list in ur piece
                    UrPiece.WhiteEnds.append(self.board[i][j])
                elif self.board[i][j].exit == "Black":
                    UrPiece.BlackEnds.append(self.board[i][j])
            else:
                while self.continue_playing(self.players):#Continue playing used for rosette
                    self.display_board()
                    player = self.players[players[turn]]
                    roll = self.roll_d4_dice()
                    print("You rolled " + str(roll))
                    if self.take_turn(player, roll):
                        self.display_board()
                        print("You have landed on a rosette, go again. ")
                        roll = self.roll_d4_dice()
                    else:
                        turn = (turn + 1) % 2

                print(players[((turn + 1) % 2)] + " wins.")

if __name__ == '__main__':
    file_name = input('What is the file name of the board json? ') if len(argv) < 2 else argv[1]
    rgu = RoyalGameOfUr(file_name)
    rgu.play_game()