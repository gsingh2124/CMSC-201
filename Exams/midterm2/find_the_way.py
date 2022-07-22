'''
File:           find_the_way.py
Author:         Gurjinder Singh
Date:           11/21/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    path finding algorithm

'''
import sys
import random

ALLOWED = '_'
FORBIDDEN = '*'


def create_map(x, y, p):
    """
    :param x: the number of rows of the grid
    :param y: the number of cols of the grid
    :param p: the probability of a forbidden space
    :return: the grid, the starting location
    """
    the_grid = [[FORBIDDEN if random.random() < p else ALLOWED for j in range(y)] for i in range(x)]
    x = random.randint(0, x - 1)
    y = random.randint(0, y - 1)
    the_grid[x][y] = 's'
    return the_grid, [x, y]


def find_path(grid, x0, y0, rows, columns, currentPosition):
    if x0 == (rows - 1) or y0 == (columns - 1) or x0 == 0 or y0 == 0:#if any coordinate is on a wall, return true
        grid[x0][y0] = currentPosition
        return True
    #Template for the checks goes as:
    #1.Check if doing one of the possible moves stays in bounds
    #2.Then check to see if the move you are making would land you on an allowed tile
    #3.if its allowed, set your old position to forbidden, so you can recurse onto the position you called from.
    #   this means if you can make that move, pretend like the old place you were at is forbidden and check all cases again so you dont trace back
    #       This step recurses until the base case (the method above this explanation) is returned.
    #4.once returned, recursion traces back each of its moves from its depths, and we set thoes positions to allowed again (this isnt actually necessary to the program but its used for matching the sample output)
    #5.once set to allowed,
    #   if the result was true, then while moving back to normal in the recursion depth,
    #       each level of the depth gets marked with its counter, tracing its steps with a number
    if y0 < (columns - 1):#up
        if grid[x0][y0 + 1] == ALLOWED:
            grid[x0][y0] = FORBIDDEN
            result = find_path(grid, x0, y0 + 1, rows, columns, currentPosition + 1)
            grid[x0][y0] = ALLOWED
            if result == True:#trace back
                grid[x0][y0] = currentPosition
                return True
    if y0 > 0:#down
        if grid[x0][y0 - 1] == ALLOWED:
            grid[x0][y0] = FORBIDDEN
            result = find_path(grid, x0, y0 - 1, rows, columns, currentPosition + 1)
            grid[x0][y0] = ALLOWED
            if result == True:#trace back
                grid[x0][y0] = currentPosition
                return True
    if x0 < (rows - 1):#right
        if grid[x0 + 1][y0] == ALLOWED:
            grid[x0][y0] = FORBIDDEN
            result = find_path(grid, x0 + 1, y0, rows, columns, currentPosition + 1)
            grid[x0][y0] = ALLOWED
            if result == True:#trace back
                grid[x0][y0] = currentPosition
                return True
    if x0 > 0:#left
        if grid[x0 - 1][y0] == ALLOWED:
            grid[x0][y0] = FORBIDDEN
            result = find_path(grid, x0 - 1, y0, rows, columns, currentPosition + 1)
            grid[x0][y0] = ALLOWED
            if result == True:#trace back
                grid[x0][y0] = currentPosition
                return True
    return False#if none of them could do it, false



def find_the_way_out(the_grid, starting_position):
    """
    :param the_grid: this is a 2d grid, either the positions will be ALLOWED which is a space, or "*" or "s". s is the starting position passed as a list
        and * is
    :param starting_position: the starting list/tuple coordinate for the starting position.
    :return: True if there is a way out, False if not

    You need to implement this function
    You are permitted to add helper functions but you shouldn't change the signature (name and parameters) of this function.
    """
    x0 = starting_position[0]
    y0 = starting_position[1]
    rows = len(the_grid)
    columns = len(the_grid[0])
    currentPosition = 0
    result = find_path(the_grid, x0, y0, rows, columns, currentPosition)

    return result


def display(the_grid):
    """
        This should display the grid on the screen.
    :param the_grid: the 2d grid.
    """
    print('\n'.join(''.join([str(x).ljust(3) for x in the_grid[i]]) for i in range(len(the_grid))))


if __name__ == '__main__':
    if len(sys.argv) == 5:
        seed = int(sys.argv[1])
        x_dimension = int(sys.argv[2])
        y_dimension = int(sys.argv[3])
        probability = float(sys.argv[4])
    else:
        seed = input('What is the seed (enter a string): ')
        x_dimension = int(input('Enter the x dimension: '))
        y_dimension = int(input('Enter the y dimension: '))
        probability = float(input('Enter a float between 0 and 1 to represent the probability of a forbidden space: '))

    random.seed(seed)

    while input('Again? ').strip().lower() == 'yes':
        the_grid, starting = create_map(x_dimension, y_dimension, probability)
        display(the_grid)
        print(find_the_way_out(the_grid, starting))
        display(the_grid)
