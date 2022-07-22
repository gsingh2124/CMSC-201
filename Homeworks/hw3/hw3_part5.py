'''
File:           hw3_part5.py
Author:         Gurjinder Singh
Date:           9/25/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Eightfold Path Part II

'''

def main():
    print()
    paths = ["Right Resolve", "Right View", "Right Samadhi", "Right Mindfulness", "Right Effort",
             "Right Livelihood", "Right Conduct", "Right Speech"]
    userIn = int(input("Enter an angle to determine the point on the Eightfold Path: "))
    if int(userIn)%45 == 0:#Validate user input is divisible by 45
        print("You have selected " + paths[((userIn%360)//45)])
        #first mod by 360 to get a number between 1-8 then // by 45 to get it on the circle if its negitive
    else:
        print("You have not reached enlightenment yet, try another angle divisible by 45")
main()