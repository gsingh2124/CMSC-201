'''
File:           jelly_bean_sort.py
Author:         Gurjinder Singh
Date:           12/14/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    FINAL: sorting the beans

'''
def jelly_bean_sort(list_of_colors):
    colors = {}#dict for colors (makes sense because the dict can count how many of the same things there are)
    for i in list_of_colors:
        if i in colors:
            colors[i] = colors[i] + 1#if the color is already in dict, upp the count
        else:
            colors[i] = 1#makes a new thing of dict when a new color is added

    output = list(colors.items())

    for i in range(len(output) - 1):#bubble sort
        for j in range(len(output) - 1):
            if output[j] > output[j+1]:
                temp = output[j]
                output[j] = output[j+1]
                output[j+1] = temp

    return output

if __name__ == "__main__":
    beans = ['red','green','red','blue','blue','green','yellow','red','yellow','red','green','red','yellow','blue'
             ,'green','red','green','red','red','blue','red','green','yellow','red','blue','red','green','red']
    print(jelly_bean_sort(beans))
