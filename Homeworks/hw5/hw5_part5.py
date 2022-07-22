'''
File:           hw5_part5.py
Author:         Gurjinder Singh
Date:           10/18/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Reverse Selection

'''
import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

# USE IF YOU ARE TESTING AND DON'T WANT TO USE COMMAND LINE ARGUMENTS
# seed(input('What seed do you want to use? '))
# END SECTION

STOP_PARAM = 'STOP'
MAX_INT = 100
"""
    Start coding here!
"""


def swap(the_list, i, j):
    temp = the_list[i]
    the_list[i] = the_list[j]
    the_list[j] = temp

    """
    :param the_list: the list that we're reverse sorting
    :param i: the first position to swap
    :param j: the second position to swap
    """


def find_max_index_after(i, the_list):
    index = 0
    max = 0
    while i < len(the_list):
        if the_list[i] > max:
            max = the_list[i]
            index = i
        i = i + 1
    return index

    """
    :param i: start at position i to look for the max
    :param the_list: the list to search
    :return: the INDEX of the maximum, not the maximum itself!
    """



def reverse_selection_sort(the_list):
    index = 0
    for i in range(len(the_list)):
        index = find_max_index_after(i, the_list)
        swap(the_list,index,i)
    return the_list

    """
    :param the_list: the list to reverse sort
    :return: the reverse sorted list
    """


"""
    Your code should end here.  The driver below should not be modified during submission.
"""


if __name__ == '__main__':
    length_or_stop = input('What length of list do you want to sort? (or STOP to end)')
    while length_or_stop != STOP_PARAM:
        try:
            the_list = [randint(0, MAX_INT) for _ in range(int(length_or_stop))]
            print('The list is: ', the_list)
            print('The reverse sort is: ', reverse_selection_sort(the_list))
        except ValueError:
            print('You entered a non-STOP non-integer, try again. ')
        length_or_stop = input('What length of list do you want to sort? (or STOP to end)')
