class Song:
    def __init__(self, title):
        self.__title=title

    def get_title(self):
        return self.__title

class Playlist:
    def __init__(self):
        self.__songs=[]

    def add_song(self, song):
        self.__songs.append(song)
    
    def get_playlist(self):
        return self.__songs


pl=Playlist()
pl.add_song(Song("Song1"))
pl.add_song(Song("Song2"))
pl.add_song(Song("Song3"))

for i in range(len(pl.get_playlist())):
    print(pl.get_playlist()[i].get_title())