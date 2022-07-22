'''
File:           pickets_problem.py
Author:         Gurjinder Singh
Date:           12/14/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    FINAL: Pickets problem

'''

def picket_problem(board):
    pickets = []#make a list of all picket locations
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:#1 means location is a picket
                pickets.append((i, j))#append picket location

    output = True#always true, until one false is found below
    for i in range(len(pickets)):#loop thru again
        for j in range(len(pickets[i])):
            picket1a = (pickets[i][0])
            picket1b = (pickets[j][0])
            picket2a = (pickets[i][1])
            picket2b = (pickets[j][1])
            #since the board is setup in a way that pickets = 1
            #and spaces = 0
            #we can check to see if certine locations values subtracted from each other
            #are greater than 1 or 0, if its equal to 0, the loop continues
            #a number greater than 1 indicates one of the conditions is saying there is an adjacent picket
            if not i == j:
                check1 = abs(picket1a - picket1b)  # abs is used because of the order of pickets being checked
                check2 = abs(picket2a - picket2b)  # they need to be positive to compare against 1
                if ((picket2b - picket2a) == (picket1b - picket1a)):
                    if check1 > 1 and check2 > 1:
                        output = False
                if ((picket2b - picket2a) == (picket1b - picket1a)):
                    if check1 > 1 and check2 > 1:
                        output = False

    return output


if __name__ == "__main__":
    #setup so board is read as 1/0
    S = 0#space
    P = 1#picket


    print("This is just a test. boards used are in code")
    #test boards

    #board given from doc
    board1 = [[S, S, S, S, S], [S, S, P, S, S], [P, S, S, P, S], [S, S, P, S, S], [S, S, S, S, S]]
    #print(picket_problem(board1))

    #all picket board
    board2 = [[P, P, P, P, P], [P, P, P, P, P], [P, P, P, P, P], [P, P, P, P, P], [P, P, P, P, P]]
    #print(picket_problem(board2))

    #all space board
    board1a = [[S, S, S, S, S], [S, P, P, S, S], [P, S, S, P, S], [S, S, S, P, S], [S, S, S, S, S]]
    #print(picket_problem(board1a))

    # all space board
    board2a = [[P, S, S, S, S], [P, P, S, S, S], [S, S, S, P, S], [S, S, S, S, P], [P, P, S, P, P]]
    #print(picket_problem(board2a))

    # all space board
    board3a = [[S, S, S, S, S], [S, S, P, S, S], [P, S, S, P, S], [S, S, P, S, S], [S, S, S, S, S]]
    #print(picket_problem(board3a))

    # all space board
    board3 = [[S, S, S, S, S], [S, S, S, S, S], [S, S, S, S, S], [S, S, S, S, S], [S, S, S, S, S]]
    #print(picket_problem(board3))

    board99 = [[P, S, S, S, S, S, S, P],
              [S, S, S, S, S, S, S, S],
              [S, S, S, S, S, S, S, S],
              [S, S, S, S, S, S, S, S],
              [S, P, S, S, S, S, S, S],
              [S, S, S, S, S, P, S, S]]
    print(picket_problem(board99))

    # board from diagram in doc
    board4 = [[S, S, S, S, S, S, S, S],
              [S, S, S, P, S, P, S, S],
              [S, S, S, S, S, S, S, S],
              [S, S, S, P, S, P, S, S],
              [S, S, S, S, S, S, S, S],
              [S, S, S, S, S, S, S, S]]
    #print(picket_problem(board4))

    #board from diagram with green spaces filled with pickets
    board5 = [[S, S, P, S, S, S, P, S],
              [S, S, S, P, S, P, S, S],
              [S, S, S, S, S, S, S, S],
              [S, S, S, P, S, P, S, S],
              [S, S, P, S, S, S, P, S],
              [S, P, S, S, S, S, S, P]]
    #print(picket_problem(board5))

    #board from diagram with red spaces as open, and green spaces as pickets
    board6 = [[S, S, P, S, S, S, P, S],
              [S, S, S, S, S, S, S, S],
              [S, S, S, S, S, S, S, S],
              [S, S, S, S, S, S, S, S],
              [S, S, S, S, S, S, S, S],
              [S, P, S, S, S, S, S, P]]
    #print(picket_problem(board6))