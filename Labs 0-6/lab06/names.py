'''
File:           names.py
Author:         Gurjinder Singh
Date:           10/13/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Lab 6, for loops with icecream stuff.

'''


def sum_list(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]
    return sum
    """
    Sums a list of integers
    :param numbers: a list of integers
    :return: the sum of the integers in numbers
    """


def get_string_lengths(strings):
    stringLengths = []
    for i in strings:
        stringLengths.append(len(i))
    return stringLengths
    """
    Given a list of strings, return a list of integers representing
    the lengths of the input strings
    :param strings: a list of strings
    :return: a list of integers representing the lengths of the input strings
    """


def get_names():
    userIn = ''
    names = []
    while (userIn != "STOP"):
        userIn = input("Enter a name to add to the list, enter STOP to stop.")
        userIn = "".join(userIn.split(" "))
        if userIn != "STOP":
            names.append(userIn)
    return names
    """
    Asks the user for a list of names
    :return: a list of strings for the names the user entered
    """


if __name__ == '__main__':
    kitties = [
        "Jules",
        "Stubby",
        "Tybalt",
        "Scooter",
        "KC",
        "Garfield",
        "Bucky"
    ]

    # print the sum of the lengths of the strings in kitties
    print("There are " + str(sum_list((get_string_lengths(kitties)))) + " letters in kitties.")
    puppers = [
        "Charlie",
        "Chuck",
        "Chuckadero",
        "Char",
        "Charmander",
        "Charles, Lord of Hearts, King of Snuggles"
    ]

    # prints the sum of the lengths of the strings in puppers
    print("There are  " + str(sum_list((get_string_lengths(puppers)))) + " letters in puppies.")
    # gets names from the user and reports how many letters are in all the names
    names_sum = sum_list(get_string_lengths(get_names()))
    print("There are " + str(names_sum) + " letters in the names you entered.")