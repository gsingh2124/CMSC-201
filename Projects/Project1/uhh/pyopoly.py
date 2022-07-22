'''
File:           pyopoly.py
Author:         Gurjinder Singh
Date:           10/30/202
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    monopoly but not monopoly... for legal reasons

'''

from sys import argv
from random import randint, seed
from board_methods import load_map, display_board
# possibly a lot more code here.
# this code can be anywhere from right under the imports to right # above if __name__ == '__main__':
#if len(argv) >= 2:
#   seed(argv[1])


Position = ["     "]*32#current player positions, signified by their symbol

map = []

p1 = '' #Player 1 name
p1s = '' #Player 1 Symbol
p2 = '' #Player 2 name
p2s = '' #Player 2 Symbol

PlayersList = [""]*2

PositionBlank = "     "

Board_file_name = "proj1_board1.csv"

EXIT_STATEMENT = "EXIT"

def play_game(starting_money, pass_go_money, board_file):
    user_inputp1 = ''
    user_inputp2 = ''
    userTurn = 1
    userProperty = ''
    p1Position = 0
    p2Position = 0
    running = True
    while running:
        format_display()
        if userTurn == 1 or userTurn % 2 == 1:
            roll = roll_Dice()
            userTurn = userTurn + 1

            while user_inputp1 != 5 or user_input != "EXIT":#While loop for player 1
                print("     1) Buy Property")
                print("     2) Get Property Info")
                print("     3) Get Player Info")
                print("     4) Build a Building")
                print("     5) End Turn")
                print("")
                user_inputp1 = input("What do you want to do? \n")
                if user_inputp1 == "1":
                    print("DNF")
                elif user_inputp1 == "2":
                    userProperty = input("For which property do you want to get the information? ")
                    searching = True
                    i = 0
                    while searching == True:#Search dictionary for propertie descriptions
                        if userProperty == map[i]["Abbrev"]:
                            print(map[i]["Place"])
                            print("Price: " + map[i]["Price"])
                            print("Owner: BANK")
                            print("Building: No")
                            print("Rent: " + map[i]["Rent"])
                elif user_inputp1 == "3":
                    print("DNF")
                elif user_inputp1 == "4":
                    print("DNF")
                elif user_inputp1 == "5":
                    user_input = EXIT_STATEMENT


        elif userTurn % 2 == 0:
            roll = roll_Dice()
            userTurn = userTurn + 1

            while user_inputp2 != 5 or user_input != "EXIT":#same as above but for player 2
                print("     1) Buy Property")
                print("     2) Get Property Info")
                print("     3) Get Player Info")
                print("     4) Build a Building")
                print("     5) End Turn")
                print("")
                user_input = input("What do you want to do? \n")
                user_inputp2 = input()
                if user_inputp2 == "1":
                    print("DNF")
                elif user_inputp2 == "2":
                    userProperty = input("For which property do you want to get the information? ")
                    searching = True
                    i = 0
                    while searching == True:
                        if userProperty == map[i]["Abbrev"]:
                            print(map[i]["Place"])
                            print("Price: " + map[i]["Price"])
                            print("Owner: BANK")
                            print("Building: No")
                            print("Rent: " + map[i]["Rent"])
                elif user_inputp2 == "3":
                    print("DNF")
                elif user_inputp2 == "4":
                    print("DNF")
                elif user_inputp2 == "5":
                    user_input = EXIT_STATEMENT




def take_turn(player, players, board):
    pass

def roll_Dice():# rolls dice twice
    return (randint(1, 6) + randint(1, 6))

def get_place(index):
    return map[index]["Place"]

def format_display():# prints the board
    output = []
    i = 0
    while i != len(map):
        output.append(map[i]["Abbrev"] + "\n" + Position[i])
        i = i + 1
    display_board(output)

#Updates the users position in the Position list while reseting the old position back to "     " and updating the oldposition value
#Method also check to see if there is more than one user at the old position to not over write the second player
def update_Position(player, number, oldposition):
    newPosition = 0
    if player == p1s:
        newPosition = (oldposition + number)%31
        p1OldPosition = get_Player_Position(p1s)
        Position[oldPosition] = p1s
        if p2s in Position[p1OldPosition]:
            Position[p1OldPosition] = p2s
        else:
            Position[p1OldPosition] = PositionBlank
    elif player == p2s:
        newPosition = (oldposition + number)%31
        p2OldPosition = get_Player_Position(p2s)
        Position[oldPosition] = p2s
        if p1s in Position[p2OldPosition]:
            Position[p2OldPosition] = p1s
        else:
            Position[p2OldPosition] = PositionBlank
    return newPosition
#Returns the index at which the Abbreviation is found
def return_Abbrev_Index(Abbrev):
    return Abbrev.find(Abbreviations)

#Returns string at index from Abbreviation
def return_from_Abbrev(Abbrev):
    return map(return_Abbrev_Index(Abbrev))

#Returns the players index, -1 for not on board
def get_Player_Position(Symbol):
    return Symbol.find(Position)

if __name__ == '__main__':
    #intro, checks of user symbol and names
    map = load_map(Board_file_name)
    p1Flag = 0
    p2Flag = 0
    p1 = input("First player, what is your name? ")
    while p1Flag == 0:
        p1s = input("First player, what symbol do you want your character to use? ")
        if len(p1s) == 1:
            p1Flag = 1
    p2 = input("Second player, what is your name? ")
    while p2Flag == 0:
        p2s = input("Second player, what symbol do you want your character to use? ")
        if len(p2s) == 1:
            p2Flag = 1
    Position[0] = p1s + " " + p2s

    PlayersList.append(p1s)
    PlayersList.append(p2s)




    play_game(0, 0, Board_file_name)