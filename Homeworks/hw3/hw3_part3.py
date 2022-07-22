'''
File:           hw3_part3.py
Author:         Gurjinder Singh
Date:           9/25/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Command program for lists

'''

def main():
    steps = input("How many steps should we run? ")
    names = []
    largestName = ""#used for holding the largest string
    for i in range(int(steps)):
        userIn = input("Enter a command: ")
        command = userIn[0:3]
        if command == "add":#adding names
            names.append(userIn[4:len(userIn)])
            print(userIn[4:len(userIn)] + " added.")
        if command == "rem":#removing names
            print(userIn[7:len(userIn)] + " removed.")
            names.remove(userIn[7:len(userIn)])
        if command == "max":#determining the largest string size
            largestName = ""
            for i in names:
                if len(i) > len(largestName):
                    largestName = i
                    for j in names:
                        if len(j) == len(largestName):#alphabetical something orderer
                            if j > i:
                              largestName = j

            print("The max name is " + largestName)
main()