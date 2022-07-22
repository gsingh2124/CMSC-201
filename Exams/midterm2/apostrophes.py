'''
File:           apostrophes.py
Author:         Gurjinder Singh
Date:           11/21/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    add apostrophes to sentences

'''
def apostriphy(userString, index):
    output = userString
    if len(userString) == (index + 1):#check if the string is the last letter
        if output[index] == "s" or output[index] == "S":#if the last lettr is s, put an apostophy
            output = output[:index] + "'" + output[index:]
        print(output)
    else:
        if output[index] == "s" or output[index] == "S":
            if not (output[index + 1].isalnum()):#make sure next index is not a number
                output = output[:index] + "'" + output[index:]
                index = index + 1
            #else:
        apostriphy(output, index + 1)

if __name__ == "__main__":
    userinput = input()
    apostriphy(userinput, 0)