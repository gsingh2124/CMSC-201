'''
File:           matching_brackets.py
Author:         Gurjinder Singh
Date:           11/6/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    more dreaded recursion but matching brackets

'''

'''
Parm n as an interger
return the number of times down the path returns
'''

def down_the_path(n):

    if n%15 == 0: #n/15
        return 1 + (down_the_path(n / 15))
    elif n%5 == 0:#n/5
        return 1 + (down_the_path(n / 5))
    elif n%3 == 0:#n/3
        return 1 + (down_the_path(n / 3))
    elif n <= 0:#n = 0 or n is negitive
        return 0
    else:#exit case
        return 1 + down_the_path(n - 1)

def count_down(count):
    if count <= 0:
        return 0
    else:
        return 1 + count_down(count - 1)

if __name__ == "__main__":
    for i in range(20):
        print(i, (down_the_path(i)))