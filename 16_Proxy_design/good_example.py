import time

class HighResImage:
    def __init__(self, file_name):
        self.__file_name=file_name
        self.__image_data=None
        self.load_from_disk()

    def load_from_disk(self):
        time.sleep(1)
        self.__image_data=f"[[Loaded image data of {self.__file_name}]]"
        print(f"Loaded {self.__file_name} from disk")

    def display(self):
        print(self.__image_data)

class ImageProxy:
    def __init__(self, file_name):
        self.__file_name=file_name
        self.__real_image=None

    def display(self):
        if self.__real_image==None:
            self.__real_image=HighResImage(self.__file_name)
        self.__real_image.display()

class PhotoGallery:
    def __init__(self):
        self.__images: list[ImageProxy]=[]

    def add_image(self, file_name):
        self.__images.append(ImageProxy(file_name))

    def display_galary(self):
        for image in self.__images:
            image.display()
    
    def show_image(self, ind):
        self.__images[ind].display()

pg=PhotoGallery()
pg.add_image("img1")
pg.add_image("img2")
pg.add_image("img3")

# pg.show_image(2)
# pg.show_image(1)
