'''
File:           lab8.py
Author:         Gurjinder Singh
Date:           10/30/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    2d array something something

'''


def create_new_weird_2d_list(height, width, value):
    """
    Creates a 2d list where all values are initialized to the supplied value
    :param height: the amount of sublists
    :param width: the size of each sublist
    :param value: the value to initialize each item in the list
    :return: a 2d list
    """
    row = []
    mat = []

    for i in range(width):
        row.append(value)

    for i in range(height):
        mat.append(row)

    return mat


def create_new_not_weird_2d_list(height, width, value):
    """
    Creates a 2d list where all values are initialized to the supplied value
    :param height: the amount of sublists
    :param width: the size of each sublist
    :param value: the value to initialize each item in the list
    :return: a 2d list
    """
    array = []#make list

    for i in range(height):
        array.append(['']*width)#put arrays in array
    for i in range(height):#for loop to assign value to each block in array
        for j in range(width):
            array[i][j] = value#nested forloop not needed if 'array.append(['']*width)' on line 43 replaced [''] with [value] but hint so...
    # hint hint hint: make two nested for loops that utilize range()
    return array


if __name__ == '__main__':
    matrix = create_new_weird_2d_list(4, 4, 0)
    matrix[0][1] = 1
    matrix[2][3] = 2
    print(matrix)
    # I'm expecting [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2], [0, 0, 0, 0]]
    # but what do I get...?
    matrix = create_new_not_weird_2d_list(4, 4, 0)
    matrix[0][1] = 1
    matrix[2][3] = 2
    print(matrix)
