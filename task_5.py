#Напиши класс Results. Проинициализируй в нём атрибуты victories, draws, losses через конструктор.
class Results:
    def __init__(self,victories, draws, losses):
        self.victories=victories
        self.draws=draws
        self.losses=losses

#Напиши класс Football, который наследуется от класса Results.
class Football(Results):
    def __init__(self,victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
       return f"Футбольных побед: {self.victories}"
    
    def number_of_draws(self):
       return f"Футбольных ничьих: {self.draws}"
    
    def number_of_losses(self):
       return f"Футбольных поражений: {self.losses}"

    def total_points(self):
       return f"Общее количество очков: {3*self.victories+self.draws}"
    
class Hockey(Results):
    def __init__(self,victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self):
       return f"Хоккейных побед: {self.victories}"
    
    def number_of_draws(self):
       return f"Хоккейных ничьих: {self.draws}"
    
    def number_of_losses(self):
       return f"Хоккейных поражений: {self.losses}"

    def total_points(self):
       return f"Общее количество очков: {2*self.victories+self.draws}"

#Создай объекты football_team и hockey_team классов Football и Hockey соответственно. В качестве параметров передай (2, 2, 2).
football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

#Вызови все методы для объектов football_team и hockey_team. Используй цикл for. Названия методов при этом не должны повторяться для обоих объектов.
for team in (football_team, hockey_team):
    for method_name in dir(team):
        if "number_of" in method_name or "total_" in method_name:
            method=getattr(team, method_name)
            print(method())