from abc import ABC, abstractmethod

class FileSystem(ABC):
    @abstractmethod
    def show_details(self):
        pass

class File(FileSystem):
    def __init__(self, name):
        self.__name=name

    def show_details(self):
        print(f"File: {self.__name}")
    
class Folder(FileSystem):
    def __init__(self, name):
        self.__name=name
        self.__components=[]

    def add(self, component):
        self.__components.append(component)
    
    def show_details(self):
        print(f"Folder: {self.__name}")
        for component in self.__components:
            component.show_details()

file1=File("File1")
file2=File("File2")
file3=File("File3")

folder1=Folder("Folder1")
folder1.add(file1)
folder1.add(file2)

folder2=Folder("Folder2")
folder2.add(file3)

folder2.add(folder1)

folder2.show_details()
