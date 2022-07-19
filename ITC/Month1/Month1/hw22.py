# 1) Создать класс Phone, у него должен быть атрибут batteryLife,
#  изначальное значение которого равно 100% и метод turnOn(), 
# который при вызове понижает процент заряда телефона на 10%,
#  также должен быть метод charge(), при вызове которого заряд 
# повышается на 10%, но главное, нельзя чтобы он заряжал его больше чем на 100%.
# class Phone:
#     def __init__(self,batteryLife, turn0n,charge):
#         self.batteryLife=batteryLife
#         self.turn0n=turn0n
#         self.charge=charge
# p=Phone(100, 10, 10,)
# print(p.batteryLife,'%',  p.turn0n,'%',  p.charge+ +p.turn0n,'%') 

class Phone:
    def __init__(self,batterlife=100):
        self.batterlife=batterlife
    def turn0n(self,p):
        self.batterlife=self.batterlife - p
        if self.batterlife >= 0:
         print(self.batterlife,'%')
        else:
            print("Телефон разряжен")
    def charge(self,p):
        self.batterlife = self.batterlife + p
        if self.batterlife <=100:
            print(self.batterlife,'%')
        else:
            print("Ваш заряд телефона заряжен 100%")
mi=Phone(50)
mi.turn0n(60)
mi.charge(20)
# 2) Создать класс Student с атрибутом student = True, он должен
#  быть родительным классом четырех переменных. У переменных Alex, 
# Sony, Ann, Debra должен быть атрибут возраста, класса в школе 
# (или курса университета) и название учебного заведения.

# class Student():
#     def __init__(self,age,grade,scoolname):
#         self.age=age
#         self.grade=grade
#         self.scoolname=scoolname
# Alex = Student(18, 1, "ОшМУ")
# print(Alex.age,Alex.grade,Alex.scoolname)
# print("")
# Sony = Student(20, 3, "ОшГУ")
# print(Sony.age,Sony.grade,Sony.scoolname)
# print("")
# Ann = Student(19, 2, "ОшТУ")
# print(Ann.age,Ann.grade,Ann.scoolname)
# print("")
# Debra = Student(15, 3, "Гагарин")
# print(Debra.age,Debra.grade,Debra.scoolname)
# print("")



# 3) Создать класс Band, у него должны быть 4 атрибута, members,
#  albums, songs, listenings. в Members должны быть записаны члены 
# этой музыкальной группы, в Albums названия всех альбомов, в Songs 
# 10 песен группы и в Listenings количество прослушиваний. Вам надо 
# записать минимум 3 группы с этим классом.
# class Band:
#     def __init__(self,members,albums,songs,listenings):
#         self.members=members
#         self.albums=albums
#         self.songs=songs
#         self.listenings=listenings
# Nirvana = Band(["Kurt","Krist","Dave"],["Bleach","Nevermind","Incestring"],
# ["Like Teen Spirit","Rape Ne","Come As You Are","Been A Son","D-7"],12000000) 
# print(Nirvana.members,Nirvana.albums,Nirvana.songs,Nirvana.listenings)
# print("")
# TheBeatles = Band(["Pol Mackartni","Jon Lennon","Jorj Harison","Ringo Star"],
# ["Help","Revolver","Let It Be"],
# ["Michele","Yesterday","Girl","Come Together","Jingl Bell Rock"],73000000)
# print(TheBeatles.members,TheBeatles.albums,TheBeatles.songs,TheBeatles.listenings)
# print("")
# LedZeppelin=Band(["Robert Plant","Jon Pol Jons","Jimmy Page","Jon Bonem"],
# ["Led Zeppelin I","Houses of the Holy","Presence"],
# ["Whole Lotte Love","Imigrant Song","Black Dog","Kashmir","Ramble On"],3000000)
# print(LedZeppelin.members,LedZeppelin.albums,LedZeppelin.songs,LedZeppelin.listenings)
# print("")
# Queen=Band(["Freddi Merkyri","Rodjer Teilor","Braian Mei","Jon Dikon"],
# ["Jazz","Innuendo","Flash Gordon"],["The Show Must Go On","We Will Rock You"
# ,"Another One Bites The Dust","We Are The Champions","I Want To Break Free"],15000000000)
# print(Queen.members,Queen.albums,Queen.songs,Queen.listenings)
