from abc import ABC, abstractmethod

class Song:
    def __init__(self, title):
        self.__title=title

    def get_title(self):
        return self.__title

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

class PlaylistIterator(Iterator):
    def __init__(self, song_list):
        self.__song_list=song_list
        self.__position=0

    def has_next(self):
        return self.__position<len(self.__song_list)

    def next(self):
        if self.has_next():
            song=self.__song_list[self.__position]
            self.__position+=1
            return song
        return None

class Playlist:
    def __init__(self):
        self.__playlist=[]

    def add_song(self, song):
        self.__playlist.append(song)
    
    def createIterator(self):
        return PlaylistIterator(self.__playlist)

pl=Playlist()
pl.add_song(Song("Song1"))
pl.add_song(Song("Song2"))
pl.add_song(Song("Song3"))
pl.add_song(Song("Song4"))

it=pl.createIterator()

while it.has_next():
    print(it.next().get_title())