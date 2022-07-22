'''
File:           switchboard.py
Author:         Gurjinder Singh
Date:           12/4/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    class for switchboard objects

'''
"""
    Switchboard class

"""

from phone import Phone


class Switchboard:
    def __init__(self, area_code):
        """
        :param area_code: the area code to which the switchboard will be associated.
        """
        self.area_code = area_code
        self.trunklines = []
        self.phones = []
        # you will probably need more data here.

    def checkPhone(self, phone_number):#returns true or false based on if the phone is present in the SB list
        output = False
        for i in self.phones:
            if i.number == phone_number:
                output = True
        return output

    def checkTrunkline(self, switchboard):#returns true or false based on if the trunkline is present in the SB list
        output = False
        for i in self.trunklines:
            if i == switchboard:
                output = True
        return output

    def add_phone(self, phone_number):#Adds phone to list
        """
        This function should add a local phone connection by creating a phone object
        and storing it in this class.  How you do that is up to you.

        :param phone_number: phone number without area code
        :return: depends on implementation / None
        """
        if not self.checkPhone(phone_number):
            self.phones.append(Phone(phone_number, self))
        else:
            print("Phone number already exists")

    def add_trunk_connection(self, switchboard):#Adds switchboard to current trunkline list
        """
        Connect the switchboard (self) to the switchboard (switchboard)

        :param switchboard: should be either the area code or switchboard object to connect.
        :return: success/failure, None, or it's up to you
        """
        if not self.checkTrunkline(switchboard):#as long as the switchboard isnt present in trunklines, add it
            self.trunklines.append(switchboard)
        else:
            print("Trunk line already exists in current switchboard.")

    def findNumber(self, number):#returns true or false depending on if the number is present in the list
        output = False
        for i in self.phones:
            if i.number == number:
                output = True
        return output

    def findPhone(self, number): #returns the phone object when found in the list
        output = None
        for i in self.phones:
            if i.number == number:
                output = i
        return output

    def connect_call(self, area_code, number, previous_codes):#uhhhhh
        """
        This must be a recursive function.

        :param area_code: the area code to which the destination phone belongs
        :param number: the phone number of the destination phone without area code.
        :param previous_codes: you must keep track of the previously tracked codes
        :return: Depends on your implementation, possibly the path to the destination phone.
        """
        # add starting element to previous codes
        #check if current element (starting first) is equal to the areacode
        #   if it is, check to see if the phone number is present in it
        #       if it is, return the switch itself.
        #   if its not, return None as the user mistook the areacode
        #loop thru trunklines,
        #   for each trunkline, recurse backto connect(call) it checks the area code again, and if not, it goes deeper into the trunk lines
        #       none is returned when all elements of trunk lines have been checked an no matching area code is found
        previous_codes.append(self.area_code)
        if self.area_code == area_code:
            if self.findPhone(number).number == number:
                return self
            else:
                return None
        else:
            for i in self.trunklines:
                if not i in previous_codes:
                    return i.connect_call(area_code, number, previous_codes)
                else:
                    return None