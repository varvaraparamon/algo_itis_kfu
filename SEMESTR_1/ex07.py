"""
Разработать программу которая ведет список музыкальных треков (исполнитель, название, автор, год, имя файла)
Предусмотреть 
- ввод треков
- вывод списка всех треков
- поиск трека по названию
- сохранение треков в файле
- загрузка треков из файла при запуске программы
"""

class Track:
    def __init__(self, singer, name, author, year, file):
        self.singer = singer
        self.name = name
        self.author = author
        self.year = year
        self.file = file
    
    def trackname(self):
        return self.name
    
    def print_track(self):
        print(self.singer, self.name, self.author, self.year, self.file)

class TrackList:
    def __init__(self, l = []):
        self.l = l

    def add_track(self, track):
        self.l.append(track)

    def print_list(self):
        for track in self.l:
            track.print_track()
        
    def find_by_name(self, name):
        for track in self.l:
            if track.name == name:
                track.print_track()

    def load_from_file(self, file):
        with open(file, "r") as f:
            for line in f:
                line = line.strip().split() 
                self.add_track(Track(line[0], line[1], line[2], line[3], file))


t = TrackList()
t.load_from_file("ex07.txt")
t.print_list()
print()

t.add_track(Track("Coldplay", "Viva_la_Vida",  "Martin",  "2008",  "ex07.txt"))
t.print_list()
print()

t.find_by_name("Smells_Like_Teen_Spirit")

