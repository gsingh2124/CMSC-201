'''
File:           favorite_nums.py
Author:         Gurjinder Singh
Date:           10/20/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Dictionary practice

'''

def print_favorite_numbers(who, favorites):
    if who in favorites:
        print(favorites[who])
    else:
        print(str(who) + " was not found.")

    """
    :param who: this is a string, representing a person in our dictionary
    :param favorites: the favorite numbers dictionary
    :return: None
    """


def add_favorite_number(who, number, favorites):
    flag = 0
    for i in favorites:
        if number in favorites[i]:
            print(str(number) + " was found " + str(i) + "'s favorites.")
            flag = 1
    if who not in favorites and flag == 0:
        favorites[who] = [number]
        print(str(number) + " added to " + str(who) + "'s favorites.")
    elif who not in favorites:
        favorites[who] = []
    elif flag == 0:
        favorites[who].append(number)
        print(str(number) + " added to " + str(who) + "'s favorites.")
    """
    :param who: add "who" to the dictionary if they're not already there and give them a blank list
            otherwise, add the number to their favorites list if the number isn't already in someone's list.
    :param number: the number to add
    :param favorites: the favorites dictionary
    :return: None (dictionaries are mutable, so you don't need to return it to modify it)
    """
    pass


if __name__ == '__main__':
    favorites = {}
    in_string = input('What do you want to do (add favorite number), print favorite numbers for <person>, or quit? ')
    while in_string.strip().lower() != 'quit':
        if in_string.strip().lower().startswith('print favorite numbers for'):
            print_favorite_numbers(in_string.strip().split()[-1], favorites)
        if len(in_string.split()) == 2:
            who, num = in_string.split()
            num = int(num)
            add_favorite_number(who, num, favorites)

        in_string = input('What do you want to do (add favorite number), or quit? ')
