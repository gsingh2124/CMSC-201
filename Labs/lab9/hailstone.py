'''
File:           lab9.py
Author:         Gurjinder Singh
Date:           11/6/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    dreaded recursion

'''


# Input:   the height of the hailstone
# Output:  a recursive call, which at the end returns
#          the number of "steps" taken for the
#          hailstone to reach a height of 1
def flight(height, steps = 0):

#### BASE CASES:
# if height is zero or lower, print out an "invalid" message and return 0

    if height <= 0:
        print("invalid")
        return 0
# stops when it reachs height of 1 (the ground)
    if height == 1:
        return steps - 1
#### RECURSIVE CASES:
# if the current height is even, divide it by 2
    if steps != 0:
        if height % 2 == 0:
            print("Height of " + str(int(height/2)))
            return flight(height/2, steps + 1)
    # if the current height is odd, multiply it by 3, then add 1
        if height % 2 == 1:
            print("Height of " + str(int((height*3)+1)))
            return flight((height*3)+1, steps + 1)
    else :
        print("Height of " + str(height))
        return flight(height, steps + 1)
def main():
    steps = 0
    print("Welcome to the Hailstone Simulator!")
    msg = "Please enter a height for the hailstone to start at: "
    startHeight = int(input(msg))

    steps = flight(startHeight)



    print("\nIt took", steps, "steps to hit the ground.")

    print("Thank you for using the Hailstone Simulator!\n")


main()



