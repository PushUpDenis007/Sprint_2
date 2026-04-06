#Напиши класс PointsForPlace. Он получает количество очков в зависимости от места, которое занял спортсмен.
class PointsForPlace:
    def __init__(self):
        self.points=0

    #В этом классе напиши метод get_points_for_place(), который принимает аргумент place — целое число.
    def get_points_for_place(self,place:int):
        if PointsForPlace.IsPlaceCorrect(place):
            self.points += 101 - place #В остальных случаях начисляются очки по формуле: 101 - place.
        return self.points #Метод get_points_for_place() должен возвращать points.
        
    @staticmethod
    def IsPlaceCorrect(place):
        #Если место строго больше 100, должно выводиться сообщение 'Баллы начисляются только первым 100 участникам'.
        if place > 100:
            print ('Баллы начисляются только первым 100 участникам')
        #Если как аргумент передали значение меньше 1, должно печататься сообщение 'Спортсмен не может занять нулевое или отрицательное место'.
        elif place < 1: 
            print ('Спортсмен не может занять нулевое или отрицательное место')
        else: return True
  
#Напиши класс PointsForMeters.
class PointsForMeters:
    def __init__(self):
        self.points=0

    def get_points_for_meters(self,meters:int): #Напиши метод get_points_for_meters(), который принимает аргумент meters — целое число. 
        if PointsForMeters.IsMetersCorrect(meters):
            #В остальных случаях начисляются очки по формуле: «количество метров умножить на 0.5».
            self.points += meters *0.5
        #Метод get_points_for_place() должен возвращать points.
        return self.points #Метод должен возвращать points. Изначально количество очков — 0.
    
    @staticmethod
    def IsMetersCorrect(meters):
        #Если количество метров меньше нуля, должно выводиться сообщение 'Количество метров не может быть отрицательным'.
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else: return True 

#Напиши класс TotalPoints для многоборцев. Он наследуется сразу от двух классов — PointsForPlace и PointsForMeters и реализует все их методы. 
class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()
        self.total=0

    def get_total_points(self, meters, place):#метод get_total_points(), который принимает как аргументы meters и place;
        self.total = PointsForPlace().get_points_for_place(place) + PointsForMeters().get_points_for_meters(meters) #переменную total, которая суммирует значения методов get_points_for_place() и get_points_for_meters().
        return self.total #Метод возвращает переменную total.

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))
print(points_for_place.get_points_for_place(110))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 