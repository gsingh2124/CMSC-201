'''
File:           nth_day.py
Author:         Gurjinder Singh
Date:           12/14/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    FINAL: Calculating the total gifts given on day of christmas

'''

def nth_day_of_christmas(day):
    if day == 1: #on the first day of christmas something something gave to me 1 present
        return 1
    if day <= 0: #no presents for you
        return 0
    else:#formula from doc, day times day+1 divided by 2 (// so no remainder)
        gifts = ((day * (day + 1))//2)
        return gifts + nth_day_of_christmas(day - 1)

if __name__ == "__main__":
    userin = ""
    while userin != "QUIT":
        userin = input("Enter the day of christmas: ")
        if userin != "QUIT":
            print(nth_day_of_christmas(int(userin)))
