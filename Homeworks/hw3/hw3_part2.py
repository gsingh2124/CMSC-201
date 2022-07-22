'''
File:           hw3_part2.py
Author:         Gurjinder Singh
Date:           9/25/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Faulhaber Summing

'''

def main():
    n = input("What is the power we want to use? ")
    p = input("How many terms do we want to calculate? ")
    out = 0 #output variable
    if int(n) < int(0) | int(p) < int(0): #input validation
        print("Both n and p must be non-negitive.")
    else:
        for i in range(1 ,int(p)+int(1)):#start at 1 and iterate until p
            out = out + (i ** int(n))
    print(out)
main()