from text_memento import TextMemento

class TextEditor:
    def __init__(self):
        self.__text = ""
        
    def write(self, words):
        self.__text += words
    
    def save(self):
        return TextMemento(self.__text)

    def get_text(self):
        return self.__text

    def restore(self, tm):
        self.__text=tm.get_saved_text();