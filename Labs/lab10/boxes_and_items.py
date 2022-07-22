'''
File:           boxes_and_items.py
Author:         Gurjinder Singh
Date:           11/13/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    lab 10 classes practice

'''
class Box:
    def __init__(self, length, width, height):
        self.volume = length * width * height
        self.unoccupied_space = self.volume
        self.items = []
    def place(self, item):#place item into box
        if item.volume > self.unoccupied_space:
            print("Item too big, remove or insert smaller item.")#check 1
        elif item in self.items:
            print("Item already exists in this box, remove or add to a different box.")#check 2
        else:
            self.items.append(item)#add item
            self.unoccupied_space = self.unoccupied_space - int(item.volume)
    def remove(self, item):#remove item
        if item in self.items:#check to see if in box and remove
            self.unoccupied_space = self.unoccupied_space + item.volume
            self.items.remove(item)
        else:#output for not in
            print("Item already in box")


class Item:
    def __init__(self, name, length, width, height):
        self.name = name
        self.volume = length * width * height
        def volume(self):
            return volume


if __name__ == '__main__':
    box_list = []
    item_list = []
    command = input('What do you want to do? ')
    while command.strip().lower() != 'quit':
        if command.strip().startswith('create box'):
            try:
                x, y, z = [int(x) for x in command.split()[2:]]
                box_list.append(Box(x, y, z))
            except:
                print('oops probably the wrong number of arguments')
        elif command.strip().startswith('create item'):
            name = command.split()[2]
            try:
                x, y, z = [int(x) for x in command.split()[3:]]
                item_list.append(Item(name, x, y, z))
            except:
                print('oops probably wrong number of arguments')
        elif command.strip().startswith('display boxes'):
            for i, box in enumerate(box_list):
                print("Box {}: with volume {} with {} space left".format(i + 1, box.volume, box.unoccupied_space))
                for item in box_list[i].items:
                    print('\t', item.name, 'is in the box.')
        elif command.strip().startswith('display items'):
            for i, item in enumerate(item_list):
                print("Item {}: with volume {}".format(item.name, item.volume))
        elif command.strip().startswith('place'):
            name_of_item = command.split()[1]
            the_item = None
            for item in item_list:
                if item.name == name_of_item:
                    the_item = item
            number_of_box = int(command.split()[3]) - 1
            if number_of_box in range(len(box_list)) and the_item:
                box_list[number_of_box].place(the_item)
            else:
                print('Error with box number or item name')
        elif command.strip().startswith('remove'):
            name_of_item = command.split()[1]
            the_item = None
            for item in item_list:
                if item.name == name_of_item:
                    the_item = item
            number_of_box = int(command.split()[3]) - 1
            if number_of_box in range(len(box_list)) and the_item:
                box_list[number_of_box].remove(the_item)
            else:
                print('Error with box number or item name')
        command = input('What do you want to do? ')
