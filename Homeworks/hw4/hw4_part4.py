'''
File:           hw4_part4.py
Author:         Gurjinder Singh
Date:           10/2/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Checkerboard of Cards

'''

if __name__ == "__main__":
    symbols = ["\u2660","\u2665","\u2666","\u2663"]
    userIn = int(input("What size of board do you want? (between 1 and 50) "))
    output = ""
    for i in range(userIn):#
        for j in range(userIn):
            offset = (i + j)%4# column + row divided by 4 giving the offset to give the pattern
            if (offset == 0):
                output = output + (symbols[0])#spade
            if (offset == 1):
                output = output + (symbols[1])#heart
            if (offset == 2):
                output = output + (symbols[2])#diamond
            if (offset == 3):
                output = output + (symbols[3])#clover
        output = output + "\n"#new line
    print(output)