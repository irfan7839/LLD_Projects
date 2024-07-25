from LLD_Projects.composite_design_pattern.file_system.file_system_interface import FileSystem


class Directory(FileSystem):
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.dir_list = []

    def ls(self):
        print('directory name:', self.dir_name)
        for file in self.dir_list:
            file.ls()

    def add_file(self, dir_name):
        self.dir_list.append(dir_name)
        print('dir added successfully')
