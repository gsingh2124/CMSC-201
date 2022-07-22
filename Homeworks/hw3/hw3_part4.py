'''
File:           hw3_part4.py
Author:         Gurjinder Singh
Date:           9/25/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    List merge

'''

def main():
    numElements = input("How many elements do you want in each list? ") #get number of elements in each list
    list1 = []
    list2 = []
    list1out = ""
    list2out = ""
    listMergeout = ""
    listMerge = []
    for i in range(int(numElements)):
        list1.append(input("What do you want to put in the first list? "))#Get inputs for list 1
    for i in range(int(numElements)):
        list2.append(input("What do you want to put in the second list? "))#Get inputs for list 2
    for i in list1:
        list1out = list1out + " '" + i + "' "#print list 1
    for i in list2:
        list2out = list2out + " '" + i + "' "#print list 2
    print("The first list is " + list1out)
    print("The second list is " + list2out)
    for i in range(int(len(list1)*2)):#merge the 2 lists
        if (i % 2) == 0:
            listMerge.append(list1[int(i/2)])
        else:
            listMerge.append(list2[int(i/2)])
    for i in listMerge:
        listMergeout = listMergeout + " '" + i + "' "#print merged list
    print("The merged list is: " + listMergeout)
main()