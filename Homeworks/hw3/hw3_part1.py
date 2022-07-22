'''
File:           hw3_part1.py
Author:         Gurjinder Singh
Date:           9/25/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Somebody feed the pupper

'''
def main ():
    tasks = []
    numtasks = input("How many tasks do you have? ")
    removedTasks = []
    if int(numtasks) <= 0:
        print("That's either negative or zero")
    else:
        for i in range(0, int(numtasks)):
            tasks.append(input("Enter next task "))
        print("Here are your tasks:")
        for i in range(0, int(numtasks)):
            print(str(i + 1) + ". " + tasks[i])
        for i in range(0, int(numtasks)):
            taskComplete = input("have you completed \"" + tasks[i] + "\" (yes/no) ")
            if str(taskComplete) == "yes":
                removedTasks.append(tasks[i])
        for i in removedTasks:
            tasks.remove(i)
        for i in tasks:
            print("A remaining task is " + i)
main()