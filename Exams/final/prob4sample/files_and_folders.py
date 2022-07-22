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
        pass


class Directory:
    def __init__(self, name, parent):
        pass

    def display(self):
        pass

    def create_file(self, file_name):
        pass

    def create_directory(self, dir_name):
        pass

    def file_write(self, file_name):
        pass

    def file_read(self, file_name):
        pass

    def close_file(self, file_name):
        pass

    def open_file(self, file_name):
        pass


class File:
    pass


if __name__ == '__main__':
    cmd_line = CommandLine()
    cmd_line.run()
