'''
File:           phone.py
Author:         Gurjinder Singh
Date:           12/4/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    class for phone objects

'''
"""
    Phone Class Starter Code

    This code defines the basic functionality that you need from a phone.
    When these functions are called they should communicate with the
    switchboards to find a path
"""


class Phone:
    def __init__(self, number, switchboard):
        """
        :param number: the phone number without area code
        :param switchboard: the switchboard to which the number is attached.
        """
        self.number = number
        self.switchboard = switchboard
        self.call = None
        self.otherPhone = None
        # Number is interger number
        # switchboard is the associated phone associated switchboard
        # call contains a phone object, ment to make algorithms easier
        # otherphone is the otherphones number

    def connect(self, area_code, other_phone_number):
        """
        :param area_code: the area code of the other phone number
        :param other_phone_number: the other phone number without the area code
        :return: **this you must decide in your implementation**
        """

        if self.call != None: #Force closes current call to make new call (makes more sense and stops alot of errors)
            print("Disconnecting current call to make new call")
            self.disconnect()

        previous_codes = []#recursive function call to locate other phone
        output = self.switchboard.connect_call(area_code, other_phone_number, previous_codes)
        if output == None:
            print("Phone not found")
        else:#swaps data between the 2 phone objects, making eachone linked
            self.call = output
            self.otherPhone = output.findPhone(other_phone_number)
            self.otherPhone.call = self.switchboard
            self.otherPhone.otherPhone = self

            #output.findPhone(other_phone_number).call = self.switchboard

            #output.findPhone(other_phone_number).otherPhone = self
            #print(self.call.area_code)
            #print(self.otherPhone.number)
            #print(self.otherPhone.call.area_code)
            #print(self.otherPhone.otherPhone.number)
            return output

    def searchList(self, list, number):#test method
        for i in list:
            if i.number == number:
                print(i.number)

    def display(self, phonenumber):#display
        output = ""
        if self.call == None:
            output = ("         Phone with number: " + str(self.number) + " is not in use.")
        else:
            output = ("         Phone with number: " + str(self.number) + " is connected to " + str(self.call.area_code) + "-" + str(self.otherPhone.otherPhone.number))
        return output

    def disconnect(self):
        """
        This function should return the connection status to disconnected.  You need
        to use new members of this class to determine how the phone is connected to
        the other phone.

        You should also make sure to disconnect the other phone on the other end of the line.
        :return: **depends on your implementation**
        """
        if self.call == None:
            print(str(self.switchboard.area_code) + "-" + str(self.number) + " is not in a call")
        else:#swaps data for both phones back to None (emulating disconnecting)
            print("Disconnected (" + str(self.switchboard.area_code) + "-" + str(self.number) + ") and (" + str(self.call.area_code) + "-" + str(self.otherPhone.number) + ")")
            self.otherPhone.call = None
            self.otherPhone.otherPhone = None
            self.call = None
            self.otherPhone = None



