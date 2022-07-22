'''
File:           path_of_ascension.py
Author:         Gurjinder Singh
Date:           10/9/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Finds increasing patterns in some list that gets computed somehow

'''
import sys
from random import seed, randint

if __name__ == "__main__":
    userIn = input()#input for user seed
    if len(userIn) >= 2:
        seed(userIn)
    sequenceLen = int(input("What length of sequence do you want to input? "))
    ascension_list = []
    currentValue = 1
    maxValue = 0
    if sequenceLen <= 1000 and sequenceLen >= 1:#check for requirements
        for _ in range(sequenceLen):
            ascension_list.append(randint(0, 100))#Creates a sequence based on the seed and size chosen
        print(ascension_list)
        for i in range(1,sequenceLen):#Goes by index starting at 1
            if (ascension_list[i] > ascension_list[i - 1]):#Checks to see if the current value is greater than the one before
                currentValue = currentValue + 1#if it is, the current value goes up by 1 for the next comparison
            else:
                if(currentValue > maxValue):#is the max value is overtaken by the current value
                    maxValue = currentValue#the max value is set to the current value
                currentValue = 1#current value resets to 1 to start again
        if(currentValue > maxValue):#final check for max value
            maxValue = currentValue
        print("The max ascending length is " + str(maxValue))
    else:
        print("Value must be between 1 and 1000")
