'''
File:           jumble.py
Author:         Gurjinder Singh
Date:           12/14/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    FINAL: jumble a string?

'''

def jumble(a_string, a, b):
    output = ""#string that gets stuff concatonated (however you spell that) to form an output
    strLen = len(a_string)
    checked_indexes = []#to make sure same indexes arent reused
    for i in range(len(a_string)):
        #for the length of the string, calculate what to look at.
        #if its not in the checked indexes list, concatonate to output string, and then add to list
        currentVal = ((int(a) * i) + (int(b))) % strLen#equation from doc but in code
        if currentVal not in checked_indexes:
            output = output + a_string[currentVal]
            checked_indexes.append(currentVal)
    return output#outputs string that was pieced togeather

if __name__ == "__main__":
    userin = ""
    while userin != "QUIT":
        userin = input("Enter a string to jumble: ")
        if userin != "QUIT":
            a = input("Enter 'a' : ")
            b = input("Enter 'b' : ")
            print(jumble(userin, a, b))