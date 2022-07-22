'''
File:           hw4_part3.py
Author:         Gurjinder Singh
Date:           10/2/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Draw a Circle, But Don't Stand in it

'''

if __name__ == "__main__":
    r = (input("What is the radius? (between 0 and 20) "))
    output = ""
    if (int(r) < 20) | (int(r) > 0):#input validation
            for i in range((int(r)*-1), (int(r) + 1)):#loooooping X
                for j in range((int(r) * -1), (int(r) + 1)):#loooooping Y
                    if (i**2 + j**2) <= (int(r)**2): #(x^2 + y^2 is within r^2 draws a "*" and if its not a " "
                        output = output + "*"
                    else:
                        output = output + " "
                output = output + "\n"#line break
    print(output)