#Создай класс Movies:
class Movies:
    def __init__(self):
        self.movies=[] #проинициализируй в нём пустой список self.movies через конструктор;

    def add_movie(self,movie): #добавь метод add_movie(). Он будет принимать параметр movie и добавлять его в конец списка self.movies.
        self.movies.append(movie)

#Создай два дочерних класса — Comedy и Drama. Они наследуют метод add_movie(). 
class Comedy(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self,movie):
        super().add_movie(movie)
        return f'Комедии: {self.movies}' #Затем возвращать записи вида Комедии: '[]' и Драмы: '[]' соответственно.

class Drama(Movies):
    def __init__(self):
        super().__init__()

    def add_movie(self,movie):
        super().add_movie(movie)
        return f"Драмы: {self.movies}"

#Вызови метод add_movie() для объекта Comedy(). Входной параметр — 'Большой куш'. Выведи на экран результат.
print(Comedy().add_movie('Большой куш'))
#Вызови метод add_movie() для объекта Drama(). Входной параметр — 'Оружейный барон'. Выведи на экран результат.
print(Drama().add_movie('Оружейный барон'))