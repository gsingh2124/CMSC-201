'''
File:           square_freeness.py
Author:         Gurjinder Singh
Date:           10/9/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    checks to see if a number and its factors are not perfect squares

'''

if __name__ == "__main__":
    userIn = input("Tell me a number x: ")
    divisior = 2
    output = ""
    if int(userIn) <= 0:#inputvalidation
        print("You cannot calculate the square freeness of " + str(userIn))
    else:
        number = int(userIn)
        if (number == 1):#special case if number is equal to 1
            output = (str(userIn) + " is square free.")
        while ((number % (divisior*2)) != 0) & ((divisior*2) < number):#makes sure values checked are within a valid range (divisor^2 isnt smaller than number)
            divisior = divisior + 1#if the current divisior squared mod the number is equal to 0, end the loop or if the divisor is in range
            if(divisior * 2) >= number:#consistantly gets used until one day its not square free
                    output = (str(userIn) + " is square free.")
            elif(number % (divisior*2)) == 0:#second check to see if its square free at the current divisor
                output = (str(userIn) + " is not square free " + str(divisior) + " divides it.")

    print(output)

