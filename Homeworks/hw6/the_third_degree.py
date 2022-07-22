'''
File:           the_third_degree.py
Author:         Gurjinder Singh
Date:           11/6/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    dreaded recursion

'''

def the_third_degree(n):
    if n == 0 or n == 1 or n == 2:
        if n == 0: #    2       n=0 Cases from the doc
            return 2
        if n == 1: #    1       n=1
            return 1
        if n == 2: #    5       n=2
            return 5
    else:#formula from the doc
        output = (3*the_third_degree(n - 1)) + (2*the_third_degree(n - 2)) + the_third_degree(n - 3)
        return output


if __name__ == '__main__':
   for i in range(10):
       print(the_third_degree(i))