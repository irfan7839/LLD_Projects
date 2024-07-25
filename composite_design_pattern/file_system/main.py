from LLD_Projects.composite_design_pattern.file_system.directory import Directory
from LLD_Projects.composite_design_pattern.file_system.file import File


class Main:
    @staticmethod
    def start():
        file = File('name.txt')
        file2 = File('irfan.py')
        dir1 = Directory('a')
        dir2 = Directory('b')
        dir1.add_file(file)
        dir2.add_file(file2)
        dir1.add_file(dir2)
        dir1.ls()


main = Main()
main.start()