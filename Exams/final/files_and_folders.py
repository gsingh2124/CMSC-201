'''
File:           files_and_folders.py
Author:         Gurjinder Singh
Date:           12/14/2020
Section:        53
E-mail:         gsingh10@umbc.edu
Description:    FINAL: linux 2 no cap, recreating a CMI directory navigation
                thing with files and directories within directories.

'''

class CommandLine:
    def __init__(self):
        self.root = Directory('', None)
        self.current_path = self.root

    def run(self):
        command = input('>>> ')
        while command.strip().lower() != 'exit':
            split_command = command.split()
            if len(split_command):
                if split_command[0] == 'ls':
                    self.current_path.display()
            if len(split_command) >= 2:
                if split_command[0] == 'cd':
                    self.change_directory(split_command[1])
                elif split_command[0] == 'makedir':
                    self.current_path.create_directory(split_command[1])
                elif split_command[0] == 'fcreate':
                    self.current_path.create_file(split_command[1])
                elif split_command[0] == 'fwrite':
                    self.current_path.file_write(split_command[1])
                elif split_command[0] == 'fread':
                    self.current_path.file_read(split_command[1])
                elif split_command[0] == 'fclose':
                    self.current_path.close_file(split_command[1])
                elif split_command[0] == 'fopen':
                    self.current_path.open_file(split_command[1])

            command = input('>>> ')

    def change_directory(self, dir_name):
        command = dir_name.strip()
        if command == "..":
            if self.current_path.parent != ('', None):#make sure parent directory exists
                self.current_path = self.current_path.parent#chnage the path
        if dir_name in self.current_path.directories:#if there is no parent, then check the list of directories for that directory
            self.current_path = self.current_path.directories[dir_name]#set path to specified path


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.directories = {}#dict to contain directories

        self.files = {}#dict to contain files

    def display(self):#displays current directory stuff
        print("ls for directory { "+ self.name + " }")
        for i in self.directories:
            print(i)
        else:
            print("\n")
            for i in self.files:
                print(i)

    def create_file(self, file_name):
        if file_name not in self.files:#check if file name doesnt already exist
            self.files[file_name] = File(file_name)

    def create_directory(self, dir_name):
        if dir_name not in self.directories:#check if directory name doesnt already exist
            self.directories[dir_name] = Directory(dir_name, self)

    def file_write(self, file_name):
        if file_name in self.files and self.files[file_name].open:#if file is open and exists
            contents = input("Enter file contents for { " + file_name + " }:")
            self.files[file_name].write(contents + '\n')
        else:
            print("File is either not open, or doesnt exist.")

    def file_read(self, file_name):#just prints the text from file
        if file_name in self.files:
            print("Contents of { " + file_name + " }:")
            print(self.files[file_name].text)
        else:
            print("Cannot find the file: " + file_name)

    def close_file(self, file_name):#sets open variable to false for file
        if file_name in self.files:
            self.files[file_name].open = False
        else:
            print("Cannot find the file: " + file_name)

    def open_file(self, file_name):#sets open variable to true for file
        if file_name in self.files:
            self.files[file_name].open = True
        else:
            print("Cannot find the file: " + file_name)

class File:
    def __init__(self, file_name):
        self.file_name = file_name
        self.text = ''
        self.open = False

    def write(self, stufftowrite):
        if self.open:#can only write when file is open
            self.text = self.text + stufftowrite#adds onto the end of text
        else:
            print("Cannot write, the file is closed. ")


if __name__ == '__main__':
    cmd_line = CommandLine()
    cmd_line.run()
