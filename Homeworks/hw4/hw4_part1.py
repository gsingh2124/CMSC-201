'''
File:           hw4_part1.py
Author:         Gurjinder Singh
Date:           10/2/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Rock Paper Scissors

'''
import sys
from random import choice, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])
if __name__ == "__main__":
    userIn = ""
    while userIn != "stop":
        the_choice = choice(["rock", "paper", "scissors"])
        userIn = input("Enter rock, paper, or scissors to play, stop to end. \n")
        userIn = userIn.lower() #confused on weather or not input validation extends beyond the example
        if (userIn == the_choice):#Series of if statements checking the inputs and printing the correct outputs
            print("Both " + the_choice + ", there is a tie.")
        elif (userIn == "paper") & (the_choice == "rock"):
            print("Paper covers rock, you win.")
        elif (userIn == "paper") & (the_choice == "scissors"):
            print("Scissors cut paper, you lose.")
        elif (userIn == "rock") & (the_choice == "paper"):
            print("Paper covers rock, you lose.")
        elif (userIn == "rock") & (the_choice == "scissors"):
            print("Rock crushes scissors, you win.")
        elif (userIn == "scissors") & (the_choice == "rock"):
            print("Rock crushes scissors, you lose.")
        elif (userIn == "scissors") & (the_choice == "paper"):
            print("Scissors cut paper, you win.")
        elif (userIn == "stop"):
            userIn = "stop"
        else:
            print("You need to select rock, paper, or scissors.")