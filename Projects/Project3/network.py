'''
File:           network.py
Author:         Gurjinder Singh
Date:           12/4/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Creating a phone network

'''
"""
network.py is both the definition file for the Network class as well as the driver for the program.

In network you need to implement the functions which the driver will call for the all the different commands.
"""

from phone import Phone
from switchboard import Switchboard

"""
import json
import csv (you can do either if you choose, or just use the regular file io)

Some constants below are for the driver, don't remove them unless you mean to.  
"""

HYPHEN = "-"
QUIT = 'quit'
SWITCH_CONNECT = 'switch-connect'
SWITCH_ADD = 'switch-add'
PHONE_ADD = 'phone-add'
NETWORK_SAVE = 'network-save'
NETWORK_LOAD = 'network-load'
START_CALL = 'start-call'
END_CALL = 'end-call'
DISPLAY = 'display'


class Network:
    def __init__(self):
        """
            Construct a network by creating the switchboard container object

            You are free to create any additional data/members necessary to maintain this class.
        """
        self.switchboards = []

    def searchSwitchboards(self, area_code):#search returns switchboard object
        output = None
        for i in self.switchboards:
            if i.area_code == area_code:
                output = i
        return output

    def presentSwitchboards(self, area_code):#search returns true or false
        flag = False
        for i in self.switchboards:
            if i.area_code == area_code:
                flag = True
        return flag

    def load_network(self, filename):#loads network
        """
        :param filename: the name of the file to be loaded.  Assume it exists and is in the right format.
                If not, it's ok if your program fails.
        :return: success?
        """
        file = open(filename, 'r')
        for split_command in file.readlines():
            if len(split_command) == 3 and split_command[0].lower() == SWITCH_CONNECT:
                area_1 = int(split_command[1])
                area_2 = int(split_command[2])
                the_network.connect_switchboards(area_1, area_2)

            elif len(split_command) == 2 and split_command[0].lower() == SWITCH_ADD:
                the_network.add_switchboard(int(split_command[1]))

            elif len(split_command) == 2 and split_command[0].lower() == PHONE_ADD:  # Add phone
                number_parts = split_command[1].split(HYPHEN)
                area_code = int(number_parts[0])
                phone_number = int(''.join(number_parts[1:]))

                switchBoard = the_network.searchSwitchboards(area_code)
                if switchBoard != None:
                    if not switchBoard.checkPhone(phone_number):
                        switchBoard.add_phone(phone_number)

    def save_network(self, filename, list):#Saves network
        """
        :param filename: the name of your file to save the network.  Remember that you need to save all the
            connections, but not the active phone calls (they can be forgotten between save and load).
            You must invent the format of the file, but if you wish you can use either json or csv libraries.
        :return: success?
        """
        file = open(filename, 'a+')
        for i in list:
            file.write(i + "\n")
        file.close()

    def add_switchboard(self, area_code):#adds switchboard to networks list of switchboards with check
        flag = False
        for i in self.switchboards:
            if i.area_code == area_code:
                flag = True
        if not flag:
            self.switchboards.append(Switchboard(area_code))
        else:
            print("Area code already exists.")

    def connect_switchboards(self, area_1, area_2):#Connects 2 switchboards togeather with areacode>switchboard object algorithm
        """
            Connect switchboards should connect the two switchboards (creates a trunk line between them)
            so that long distance calls can be made.

        :param area_1: area-code 1
        :param area_2: area-code 2
        :return: success/failure
        """
        if self.presentSwitchboards(area_1) == False or self.presentSwitchboards(area_2) == False:
            print("One or more of the switchboards do not exist")
        else:
            self.searchSwitchboards(area_1).add_trunk_connection(self.searchSwitchboards(area_2))
            self.searchSwitchboards(area_2).add_trunk_connection(self.searchSwitchboards(area_1))

    def display(self):#Display method for returning all data
        for i in self.switchboards:
            print("Switchboard with area code: " + str(i.area_code))
            print("     Trunk lines are: ")
            for j in i.trunklines:
                print("         Trunkline connection to: " + str(j.area_code))
            print("     Local phone numbers are:")
            for j in i.phones:
                print(j.display(j.number))

if __name__ == '__main__':
    # FileIO contains commands to append to the save command
    #   Each required command has its own FileIo append
    FileIO = []
    the_network = Network()
    s = input('Enter command: ')
    while s.strip().lower() != QUIT:
        split_command = s.split()
        if len(split_command) == 3 and split_command[0].lower() == SWITCH_CONNECT:
            area_1 = int(split_command[1])
            area_2 = int(split_command[2])
            the_network.connect_switchboards(area_1, area_2)

            FileIO.append(str(SWITCH_CONNECT + " " + str(area_1) + " " +  str(area_2)))

        elif len(split_command) == 2 and split_command[0].lower() == SWITCH_ADD:
            the_network.add_switchboard(int(split_command[1]))

            FileIO.append(str(SWITCH_ADD + " " + str(split_command[1])))

        elif len(split_command) == 2 and split_command[0].lower() == PHONE_ADD:                                         #Add phone
            number_parts = split_command[1].split(HYPHEN)
            area_code = int(number_parts[0])
            phone_number = int(''.join(number_parts[1:]))

            FileIO.append(str(PHONE_ADD + " " + str(area_code) + " " + str(phone_number)))

            switchBoard = the_network.searchSwitchboards(area_code)
            if switchBoard == None:
                print("Invalid area_code, create a new switchboard or enter a valid area code.")
            else:
                if switchBoard.checkPhone(phone_number):
                    print("Phone number already exists in area code")
                else:
                    switchBoard.add_phone(phone_number)
        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_SAVE:
            the_network.save_network(split_command[1], FileIO)
            print('Network saved to {}.'.format(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_LOAD:
            the_network.load_network(split_command[1])
            print('Network loaded from {}.'.format(split_command[1]))
        elif len(split_command) == 3 and split_command[0].lower() == START_CALL:                                        #Starts call
            src_number_parts = split_command[1].split(HYPHEN)
            src_area_code = int(src_number_parts[0])
            src_number = int(''.join(src_number_parts[1:]))

            dest_number_parts = split_command[2].split(HYPHEN)
            dest_area_code = int(dest_number_parts[0])
            dest_number = int(''.join(dest_number_parts[1:]))

            switch = the_network.searchSwitchboards(src_area_code)
            if switch == None:
                print("Area code does not exist")
            else:
                phone = switch.findPhone(src_number)
                if phone == None:
                    print("Source phone number does not exist")
                else:
                    phone.connect(dest_area_code,dest_number)

        elif len(split_command) == 2 and split_command[0].lower() == END_CALL:                                          #Ends call
            number_parts = split_command[1].split('-')
            area_code = int(number_parts[0])
            number = int(''.join(number_parts[1:]))

            switch = the_network.searchSwitchboards(area_code)
            if switch == None:
                print("Area code not found")
            else:
                phone = switch.findPhone(number)
                if phone == None:
                    print("Phone not found")
                else:
                    phone.disconnect()
                    print("Endcall ran")
        elif len(split_command) >= 1 and split_command[0].lower() == DISPLAY:
            the_network.display()

        s = input('Enter command: ')
