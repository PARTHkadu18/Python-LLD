class File:
    def __init__(self, name):
        self.__name=name

    def show_details(self):
        print(f"File: {self.__name}")
    
class Folder:
    def __init__(self, name):
        self.__name=name
        self.__files=[]

    def add_file(self, file):
        self.__files.append(file)
    
    def show_details(self):
        print(f"Folder: {self.__name}")
        for file in self.__files:
            file.show_details()

file1=File("File1")
file2=File("File2")
file3=File("File3")

folder1=Folder("Folder1")
folder1.add_file(file1)
folder1.add_file(file2)

folder1.show_details()
