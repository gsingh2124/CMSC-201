'''
File:           hw4_part5.py
Author:         Gurjinder Singh
Date:           10/2/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Number guesser

'''
import sys
from random import randint, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])
if __name__ == "__main__":
    winner = 0
    number = randint(1,100) #random number between 1 and 100
    steps = 0 #counter for number of steps it takes to guess correctly
    while winner == 0:
        steps = steps + 1
        guess = int(input("Guess a number between 1 and 100: "))
        if (guess > number):
            print("Your guess is too high.")
        if(guess < number):
            print("Your guess is too low.")
        if (guess == number):
            print("You guessed the value! It took you " + str(steps) + " steps.")
            winner = 1