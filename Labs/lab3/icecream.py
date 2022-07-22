'''
File:           icecream.py
Author:         Gurjinder Singh
Date:           9/25/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Lab 3, for loops with icecream stuff.

'''

def main():
    ice_cream_flavors = ["vanilla", "strawberry", "chocolate"]
    toppings = ["caramel", "marshmallow", "gummi bears"]

    print("Part 1---------------")
    for flavor in ice_cream_flavors:
        print(flavor)
    print("Part 2---------------")
    for flavor in ice_cream_flavors:
        for topping in toppings:
            print(flavor + " is tasty with " + topping)
    print("Part 3---------------")
    for flavor in ice_cream_flavors:
        if flavor == "strawberry":
            print("strawberry is fine on its own!")
        else:
            for topping in toppings:
              print(flavor + " is tasty with " + topping)
main()