'''
File:           matching_brackets.py
Author:         Gurjinder Singh
Date:           11/6/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    more dreaded recursion but matching brackets

'''

def match_brackets(bracket_string, count=0):
    #if len(bracket_string) == 0 or count < 0:# lets me know in main if its true or false
    if len(bracket_string) == 0:#empty string bad string and if
        if count == 0:
            return True
        elif len(bracket_string) == 0 and count > 0:
            return False
        elif count < 0:# uneven meaning mismatch in number of brackets
            return False
    else:
        if bracket_string[0] == "{":#modifying the count of brackets
           count = count + 1
        if bracket_string[0] == "}":
         count = count - 1

    #bracket_string[1:] = " "#set the first index = 0
    #bracket_string.strip(" ")# strip the first index because its now a space
    #didnt work because strings are immutable?
    if len(bracket_string) != 0:
        bracket_string = bracket_string[1:]
    if count != 0 or not count < 0 or len(bracket_string) != 0:
        return match_brackets(bracket_string, count)#pass it back thru and hope for the best


if __name__ == "__main__":
    user_input = " "
    while input != "quit":
        user_input = input("Enter a string with brackets: ")
        output = match_brackets(user_input)
        print(output)
