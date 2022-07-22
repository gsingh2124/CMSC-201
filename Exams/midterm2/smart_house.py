'''
File:           smart_house.py
Author:         Gurjinder Singh
Date:           11/21/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    Smart home

'''
class Device:
    def __init__(self, name, toggle):#init device
        self.name = name
        self.toggle = toggle


class SmartHouse:
    def __init__(self, address):#init house
        self.address = address
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def get_device(self, the_id):
        for i in self.devices:
            if i.name == the_id:
                return i
        return None

    def save_house(self, file_name):#saves house
        file = open(file_name, 'a+')
        for i in self.devices:
            file.write(i.name + " " + str(i.toggle) + "\n")
        file.close()

    def load_house(self, file_name):#loads house from a file
        file = open(file_name, 'r')
        for i in file.readlines():
            current = i.split(" ")
            if current[len(current) - 1] == "True\n":
                self.add_device(Device(current[0], True))
            elif current[len(current) - 1] == "False\n":
                self.add_device(Device(current[0], False))
        file.close()

    def display(self):#displays the devices at the house
        print("Address: " + self.address)
        print("Devices:")
        for i in self.devices:
            if i.toggle == True:
                print("     " + i.name + " is " + "on")
            elif i.toggle == False:
                print("     " + i.name + " is " + "off")


if __name__ == '__main__':
    address = input('What is the address of the house?')
    house = SmartHouse(address)

    command = input('What do you want to do? (add device, toggle device, load <file>, save <file>, display) ').lower()
    while command != 'quit':
        if command == 'add' or command == 'add device':
            the_id = input('What is the device id?')
            if not house.get_device(the_id):
                yes_no = input('Is the device on? (yes/no)')
                if yes_no == 'yes':
                    house.add_device(Device(the_id, True))
                elif yes_no == 'no':
                    house.add_device(Device(the_id, False))
            else:
                print('There is no device id: {} in the ')
        elif command == 'toggle' or command == 'toggle device':
            the_id = input('What is the device id?')
            the_device = house.get_device(the_id)
            if the_device:
                on_off_toggle = input('On, Off or Toggle? ').lower()
                if on_off_toggle == 'on':
                    the_device.toggle = True
                elif on_off_toggle == 'off':                    the_device.toggle = False
                elif on_off_toggle == 'toggle':
                    the_device.toggle = not the_device.toggle
            else:
                print('There is no device id: {} in the ')
        elif command == 'load':
            file_name = input('What is the filename to load from? ')
            house.load_house(file_name)
            print('The house has been loaded from {}'.format(file_name))
        elif command == 'save':
            file_name = input('What is the filename to save as? ')
            house.save_house(file_name)
            print('The house has been saved in {}'.format(file_name))
        elif command == 'display':
            house.display()
        else:
            print('unknown command', command)

        command = input('What do you want to do? (add device, toggle device, load <file>, save <file>, display) ').lower()
