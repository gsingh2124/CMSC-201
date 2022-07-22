'''
File:           houses_and_people.py
Author:         Gurjinder Singh
Date:           11/6/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    practice with classes?

'''
class Person:
    def __init__(self, name, currentHouse = ""):
        self.name = name#initilize Person data (name and house)
        self.the_house = currentHouse
    def go_in(self, house):
        if self.name in house.renter:
            print(self.name + " is already in the house.")#check to see if the person already exists in the house list
        elif self.name not in house.renter:
            self.the_house = house
            house.renter.append(self.name) #add the person to the renter list for the house they want to be in
    def leave(self, house):
        if self.the_house not in house.renter:#check to see if the person is already not in the house
            print(self.name + " is not in the house.")
        elif self.the_house in house.renter:
            self.the_house = ""#reset house to blank for person
            house.renter.remove(self.name)#remove house form renter list



class House:
    def __init__(self, address):
        self.address = address
        self.renter = [] #var to store people that are in the house
    def display(self):#displays ig
        print("The house is at:" + str(self.address))
        for person in self.renter:
            print("     " + person)


if __name__ == '__main__':
    print('The options are:\n\tcreate <person name>\n\tperson-name enter house-address\n\tperson-name exit house-address\n\tdisplay')
    in_string = input('What do you want to do? ')
    people_list = []
    house_list = []
    while in_string.strip().lower() not in ['quit', 'q']:
        enter_string = in_string.split('enter')
        exit_string = in_string.split('exit')
        if in_string.split()[0:2] == ['create', 'person']:
            people_list.append(Person(' '.join(in_string.split()[2:])))
            print('Person {} created'.format(people_list[-1].name))
        elif in_string.split()[0:2] == ['create', 'house']:
            house_list.append(House(' '.join(in_string.split()[2:])))
            print('House {} created'.format(house_list[-1].address))
        elif len(enter_string) == 2:
            if not any(enter_string[0].strip() == person.name for person in people_list):
                print('The person isn\'t in the list.')
            elif not any(enter_string[1].strip() == house.address for house in house_list):
                print('The person isn\'t in the list.')
            else:
                the_house = None
                the_person = None
                for house in house_list:
                    if house.address == enter_string[1].strip():
                        the_house = house
                for person in people_list:
                    if person.name == enter_string[0].strip():
                        the_person = person
                if the_person and the_house:
                    the_person.go_in(the_house)
                else:
                    print('Something went wrong.  ')
        elif len(exit_string) == 2:
            if not any(exit_string[0].strip() == person.name for person in people_list):
                print('The person isn\'t in the list.')
            elif not any(exit_string[1].strip() == house.address for house in house_list):
                print('The person isn\'t in the list.')
            else:
                the_house = None
                the_person = None
                for house in house_list:
                    if house.address == exit_string[1].strip():
                        the_house = house
                for person in people_list:
                    if person.name == exit_string[0].strip():
                        the_person = person
                if the_person and the_house:
                    the_person.leave(the_house)
                else:
                    print('Something went wrong.  ')
        elif in_string.lower().strip() == 'display':
            for house in house_list:
                house.display()
            print('These people aren\'t in a house')
            for person in people_list:
                if not person.the_house:
                    print(person.name)

        in_string = input('What do you want to do? ')
