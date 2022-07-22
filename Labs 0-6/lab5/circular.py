'''
File:           circular.py
Author:         Gurjinder Singh
Date:           10/9/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    checks to see if a string is circular?

'''

if __name__ == "__main__":
    userIn = str(input("Enter a string: ")).lower()
    x = "".join(userIn.split())#rids of white spaces, all lower case
    #print(x)
    rotation = 0#indicator if the string doesnt rotate (boolean flag)
    #for i in range(len(x)):
    #    print(str(i) + x[i])#prints index with the associated char
    for k in range(1, len(x)-1):#loop thru -1 because of bounds
        if x[k:] + x[:k] == x:#if (x[index] to end of x) + (x[index] to begining of x) == x), then continue
            rotation = 1#count the rotation
            print(str(x) + " is a rotation with offset " + str(k))
    if rotation == 0:#no rotations
        print("There are no rotations of the string")