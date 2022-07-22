'''
File:           hw4_part2.py
Author:         Gurjinder Singh
Date:           10/2/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Caesar Salad Cipher

'''

if __name__ == "__main__":
    newString = ""
    userString = ""
    while (userString != "stop"):
        userString = input("What is the string to encrypt? (or stop)")
        newString = ""
        if (userString != "stop"):
            offset = int(input("What is the offset? "))
            for i in range(len(userString)):#loop through every char in user in
                char = ord(userString[i])
                if ((char >= 65) & (char <= 90)) | ((char >= 97) & (char <= 122)):#make sure input is between the alphabet in ascii
                    if ((char >= 65) & (char <= 90)):#calculate the output for UpperCase
                        newchar = char + (i**2) + offset
                        if(newchar > 90):
                            newchar = (newchar - 65)%26 + 65
                        newString = newString + chr(newchar)
                    elif ((char >= 97) & (char <= 122)):#calculate the output for LowerCase
                        newchar = char + (i**2) + offset
                        if(newchar > 122):
                            newchar = ((newchar - 97)%26) + 97
                        newString = newString + chr(newchar)
                else:# if the charachter isnt within the alphabet
                    newString = newString + userString[i]
            print("The encrypted string is: " + newString)
