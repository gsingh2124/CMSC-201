'''
File:           crabs.py
Author:         Gurjinder Singh
Date:           9/25/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    sorting crabs and while loops

'''

def main():
    allcrabs = []#all crabs user inputs
    lower = []#lower than user considerd number
    higher = []#higher than user considerd number
    userIn = ""
    light = 0#Used for sorting between high and lower algorithm
    lout = ""#output for lower than weight
    hout = ""#output for heigher than weight
    while userIn != "STOP":#Get user data for crabs
        userIn = input("Enter crab weight, (STOP to end) ")
        if userIn != "STOP":
            allcrabs.append(int(userIn) + .0)

    while (userIn != "light") and (userIn != "heavy"):#Validate user input for weight of crabs
        userIn = input("Do you want to keep light or heavy crabs? ")
        if userIn != "light" and userIn != "heavy":
            print("You must enter light or heavy")
        if userIn == "light":
            light = 1
        elif userIn == "heavy":
            light = 0
    userIn = input("What weight determines if the crab is light or heavy? ")
    if light == 1:#computation for lower than weight crabs
        for i in allcrabs:
            if int(i) < int(userIn):
                lower.append(i)
            elif int(i) >= int(userIn):
                higher.append(i)
        for i in lower:
            (lout) = lout + (str(i) + ", ")
        for i in higher:
            hout = hout + (str(i) + ", ")
        print("You are keeping the crabs with wights [" + lout + "]")
        print("You are not keeping the crabs with weights [" + hout + "]")
    elif light == 0:#computation for heigher than weight crabs
        for i in allcrabs:
            if int(i) > int(userIn):
                higher.append(i)
            elif int(i) <= int(userIn):
                lower.append(i)
        for i in lower:
            lout = lout + (str(i) + ", ")
        for i in higher:
            hout = hout + (str(i) + ", ")
        print("You are keeping the crabs with wights [" + hout + "]")
        print("You are not keeping the crabs with weights [" + lout + "]")





main()