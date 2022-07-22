'''
File:           find_dipthongs.py
Author:         Gurjinder Singh
Date:           10/9/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Finds dipthongs in a string

'''

if __name__ == "__main__":
    # A E I O U
    vowel_pairs = ["ae", "ai", "ao", "au", "ay",#List of possible pairs
                   "ea", "ei", "eo", "eu", "ey",
                   "ia", "ie", "io", "iu", "iy",
                   "oa", "oe", "oi", "ou", "oy",
                   "ua", "ue", "ui", "uo", "uy",
                   "ya", "ye", "yi", "yo", "yu"]
    dipthongs = [] # to return the found diphongs
    userIn = input("Enter a string with a lot of dipthongs: ")
    userIn = userIn.lower()
    dipthongCounter = 0;
    loopCount = 0
    while loopCount < (len(userIn)-1):#loop thru the string with the length -1 to prevent out of bounds errors
        if (userIn[loopCount] + userIn[loopCount+1]) in vowel_pairs:#check char1+char2 to see if they are a pair
            dipthongCounter = dipthongCounter + 1
            dipthongs.append(userIn[loopCount] + userIn[loopCount + 1])
            loopCount = loopCount + 2#count 2 to skip over the accounted for pair
        else:
            loopCount = loopCount + 1
    for i in dipthongs:#print the found diphongs
        print(i)
    print("The dipthong count is " + str(dipthongCounter))
