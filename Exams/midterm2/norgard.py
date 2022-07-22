'''
File:           norgard.py
Author:         Gurjinder Singh
Date:           11/21/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Norgard's Sequence or something like that

'''
def calcNograd(usernum):
    if usernum == 0:#a0 = 0
        return 0
    elif (int(usernum) % 2) == 0:#a2n = -an
        return calcNograd(int(usernum)/2) * -1
    else:#a2n+1 = an+1
        return calcNograd(int(usernum)/2) + 1

if __name__ == "__main__":
    userin = input("What value do you want to calculate? ")
    print(calcNograd(userin))