'''
File:           hw5_part2.py
Author:         Gurjinder Singh
Date:           10/18/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Pascal Levels

'''
def pascal_level(a_list):
    output = []#The output list
    temp = 0#holds the previous value of i for calculation in the next one
    for i in range(len(a_list)): #loop through as an interger
        output.append(a_list[i] + temp) #adds the current and previous value to the output list
        temp = a_list[i]  #temp gets assigned the current value of i
    output.append(1)#added to maintain pascals triangle
    """
    :param a_list: a list represents the previous level in the pascal's triangle construction
    :return: a new list with the previous elements summed
    """
    return output


if __name__ == '__main__':
    next_line = [1]
    for i in range(10):
        print(next_line)
        next_line = pascal_level(next_line)

    print(pascal_level([1, 1, 1, 1, 29]))
    print(pascal_level([1, 1, 2, 3, 5, 8]))
    print(pascal_level([1, 1, 2, 3, 5, 8, 13, 1]))
