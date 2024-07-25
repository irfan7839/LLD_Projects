from LLD_Projects.composite_design_pattern.file_system.file_system_interface import FileSystem


class File(FileSystem):

    def __init__(self, file_name):
        self.file_name = file_name

    def ls(self):
        print('file name is:', self.file_name)

