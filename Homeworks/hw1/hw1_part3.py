'''
File:           hw1_part3.py
Author:         Gurjinder Singh
Date:           9/4/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Calculating the cost of owning an animal
                for a year based on monthly food and other expenses.
'''

pet_type = input("What type of animal is it? ")
monthly_food = input("How much do you spend monthly for their food? ")
monthly_supplies = input("How much do you spend on other supplies? ")
annual_cost = (int(monthly_food) + int(monthly_supplies)) * (12)

print("The annual cost of owning an " + pet_type + " is $" + str(annual_cost))