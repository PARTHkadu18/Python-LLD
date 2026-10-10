from text_memento import TextMemento
class History:
    def __init__(self):
        self.__history=[]

    def save_state(self, TextMemento):
        self.__history.append(TextMemento)

    def undo(self):
        if len(self.__history)>0:
            self.__history.pop()
            if len(self.__history)==0:
                return TextMemento("")
            return self.__history[-1]
        else:
            return TextMemento("")