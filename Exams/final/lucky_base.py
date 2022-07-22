'''
File:           lucky_base.py
Author:         Gurjinder Singh
Date:           12/14/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    FINAL: Custom base number calculator (base 7)

'''

def lucky_base(number):
    output = ""
    if number == 0:#check from doc
        return 0
    while int(number) > 0: #make sure numbers checked are positive
        calcNum = int(number) % 7#Calculate the num
        output = str(calcNum) + output#Concatonate the num
        number = int(number) // 7#set number equal to num/7 w no remainder
    return str(output)

if __name__ == "__main__":
    userin = ""
    while userin != "QUIT":
        userin = input("Enter a number to convert: ")
        if userin != "QUIT":
            print("Base 7 of " + userin + " is " + lucky_base(userin))