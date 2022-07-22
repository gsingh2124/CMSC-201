'''
File:           hw1_part3.py
Author:         Gurjinder Singh
Date:           9/4/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Calculating the cost of owning an animal
                for a year based on monthly food and other expenses.
'''
import math

bigG = 6.674 * math.pow(10,-11)
mass1 = input("What is the mass of the first object in kg? ")
mass2 = input("What is the mass of the second object in kg? ")
distance = input ("What is the distance in meters between the objects? ")

topHalf = bigG*float(mass1)*float(mass2)
bottomHalf = math.pow(float(distance), 2)

print("The gravitational force between the two objects is: " + str(topHalf/bottomHalf))