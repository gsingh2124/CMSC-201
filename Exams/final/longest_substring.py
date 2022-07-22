'''
File:           longest_substring.py
Author:         Gurjinder Singh
Date:           12/14/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    FINAL: Find strings inside of strings

'''

def longest_substring(total_string, find_string):
    #Count down from len(find_string) by 1 until 0
    for i in range(len(find_string), 0, -1):#Loop the length of the total_string
        for j in range(len(find_string) - i + 1):#loop the length of the find_string
            #ex: hello find hel
            #if h in hello
            #return i,
            #if he in hello
            #return i,
            #etc,
            if (find_string[j:j + i] in total_string):
                return i


if __name__ == "__main__":
    userin = ""
    while userin != "QUIT":
        userin = input("Enter a string: ")
        if userin != "QUIT":
            a = input("Enter a string to find in it: ")
            print(longest_substring(userin, a))
