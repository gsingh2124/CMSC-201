'''
File:           hw1_part5.py
Author:         Gurjinder Singh
Date:           9/4/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    energy calculator
'''
import math

objMass = input("Enter the rest mass in kg ")
objVel = input("Enter the velocity in m/s ")
topHalf = float(objMass)*(299792458*299792458)
bottomHalf = math.sqrt(1-((float(objVel)*float(objVel))/(299792458*299792458)))
energy = topHalf/bottomHalf
print("The Lorentz Energy in the object ofrest mass " + objMass + " and velocity " + objVel + " is " + str(energy))