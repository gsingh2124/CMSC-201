'''
File:           calculator.py
Author:         Gurjinder Singh
Date:           11/21/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    calculate stuff from a file

'''
class Variable:
    variables = []
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
def findVar(number):#finds variable by value
    for i in Variable.variables:
        if i == number:
            return i
def findVarbyName(name):#finds variable by name
    for i in Variable.variables:
        if i.getName() == str(name):
            return i
def printVariables():#prints all variables
    out = ""
    for i in Variable.variables:
        out = out + str(i.getName()) + " " + str(i.getValue()) + "\n"
    return out[:-1]
def printVariable(name):#prints a variable by name
    out = ""
    for i in Variable.variables:
        if i.getName() == name:
            out = out + str(i.getName()) + " " + str(i.getValue()) + "\n"
    return out[:-1]
def deleteOldVar(name):#deletes old variable
    for i in Variable.variables:
        if i.getName() == name:
            Variable.variables.remove(i)
def calculate(file_name):#calculates from a file

    #if varA == None:
    #    print("Variable not made yet")
    #else:
    #^ these statements are repeated many times, they are checks to make sure the variable being called exists or not

    output = ""
    file = open(file_name, 'r')#open file
    for i in file.readlines():#read every line, i is assinged to an indivisual line
        current = i
        current = i.strip("\n")#get rid of the \n
        current = current.split(" ")#split the line into its core string words
        if current[0] == "create":
            if not current[1].isnumeric():#check if numeric
                if findVar(current[1]) == None:#check if doesnt exist
                    Variable.variables.append(Variable(current[1],current[2]))#make variable
                else:
                    print("Variable already exists")
            else:
                print("Variable name cannot be a number")
        elif current[0] == "add":
            if current[1].isnumeric() and current[2].isnumeric():#if both numeric
                deleteOldVar(str(current[3]))
                Variable.variables.append(Variable(current[3], int(current[1])+int(current[2])))
            elif current[1].isnumeric() and not current[2].isnumeric():#if one numeric one variable
                varA = findVarbyName(current[2]).getValue()
                if varA == None:
                    print("Variable not made yet")
                else:
                    value = int(current[1]) + int(varA)
                    deleteOldVar(str(current[3]))
                    Variable.variables.append(Variable(current[3],value))
            elif current[2].isnumeric() and not current[1].isnumeric():#if one numeric and one variable
                varA = findVarbyName(current[1]).getValue()
                if varA == None:
                    print("Variable not made yet")
                else:
                    value = int(current[2]) + int(varA)
                    deleteOldVar(str(current[3]))
                    Variable.variables.append(Variable(current[3], value))
            elif not current[1].isnumeric() and not current[2].isnumeric():#if both variables
                varA = findVarbyName(current[1]).getValue()
                varB = findVarbyName(current[2]).getValue()
                if varA == None or varB == None:
                    print("Variable not made yet")
                else:
                    value = int(varA) + int(varB)
                    deleteOldVar(str(current[3]))
                    Variable.variables.append(Variable(current[3], value))

        elif current[0] == "display":
            if current[1] == "all":
                print(printVariables())
            elif current[1] != "all" and not i[1].isnumeric():
                print(printVariable(str(current[1])))

        elif current[0] == "mul":
            if current[1].isnumeric() and current[2].isnumeric():#if both are numeric
                deleteOldVar(str(current[3]))
                Variable.variables.append(Variable(current[3], int(current[1]) * int(current[2])))# if one is numeric and one is a variable
            elif current[1].isnumeric() and not current[2].isnumeric():
                varA = findVarbyName(current[2]).getValue()
                if varA == None:
                    print("Variable not made yet")
                else:
                    value = int(current[1]) * int(varA)
                    deleteOldVar(str(current[3]))
                    Variable.variables.append(Variable(current[3], value))
            elif current[2].isnumeric() and not current[1].isnumeric():# if one is numeric and one is a variable
                varA = findVarbyName(current[1]).getValue()
                if varA == None:
                    print("Variable not made yet")
                else:
                    value = int(current[2]) * int(varA)
                    deleteOldVar(str(current[3]))
                    Variable.variables.append(Variable(current[3], value))
            elif not current[1].isnumeric() and not current[2].isnumeric():#if both are variables
                varA = findVarbyName(current[1]).getValue()
                varB = findVarbyName(current[2]).getValue()
                if varA == None or varB == None:
                    print("Variable not made yet")
                else:
                    value = int(varA) * int(varB)
                    deleteOldVar(str(current[3]))
                    Variable.variables.append(Variable(current[3], value))

if __name__ == "__main__":
    userinput = input("What file do you wish to run? ")
    calculate(userinput)