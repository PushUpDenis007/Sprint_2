"""Задача 3 показалась мне макисимально не логичной, поэтому я попробовал преобразовать программу с видимостью практичности;
Создал классы и подклссы для типов спортсменов и вынес начисление очков (общее для всех) в родительский клас;
В зависимости от типа спортсмена присуждается определнное кол-во очков"""
class Sportsman ():
    def __init__(self):
        self.points=0

    def set_points(self, points):
        self.points = points

class Runner(Sportsman):
    def __init__(self):
        super().__init__()

    def get_points_for_place(self,place:int):
        if self.is_place_correct(place):
            super().set_points(101 - place) #В остальных случаях начисляются очки по формуле: 101 - place.  
        return self.points #Метод get_points_for_place() должен возвращать points.
            
    @staticmethod
    def is_place_correct(place):
        #Если место строго больше 100, должно выводиться сообщение 'Баллы начисляются только первым 100 участникам'.
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        #Если как аргумент передали значение меньше 1, должно печататься сообщение 'Спортсмен не может занять нулевое или отрицательное место'.
        elif place < 1: 
            print ('Спортсмен не может занять нулевое или отрицательное место')
        else: return True

class Swimmer(Sportsman):
    def __init__(self):
        super().__init__()

    def get_points_for_meters(self,meters:int): #Напиши метод get_points_for_meters(), который принимает аргумент meters — целое число. 
        if self.is_meters_correct(meters):
            super().set_points(meters *0.5) #В остальных случаях начисляются очки по формуле: «количество метров умножить на 0.5».
        return self.points #Метод должен возвращать points. Изначально количество очков — 0.
    
    @staticmethod
    def is_meters_correct(meters):
        #Если количество метров меньше нуля, должно выводиться сообщение 'Количество метров не может быть отрицательным'.
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else: return True 

#Напиши класс для многоборцев.
class Kicker(Runner, Swimmer):
    def __init__(self):
        super().__init__()
        self.total=0

    def get_total_points(self, meters, place):#метод get_total_points(), который принимает как аргументы meters и place;
        self.total = self.get_points_for_place(place) + self.get_points_for_meters(meters) #переменную total, которая суммирует значения методов get_points_for_place() и get_points_for_meters().
        return self.total #Метод возвращает переменную total.


runner = Runner()
print(runner.get_points_for_place(10))
print(runner.get_points_for_place(110))

swimmer = Swimmer()
print(swimmer.get_points_for_meters(10))

kicker = Kicker()
print(kicker.get_points_for_place(10))
print(kicker.get_points_for_meters(10))
print(kicker.get_total_points(100, 10)) 