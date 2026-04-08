#Прекод:
class Case:
    def __init__(self, test_case_id, name, step_description, expected_result):
        self.test_case_id = test_case_id
        self.name = name
        self.step_description = step_description
        self.expected_result = expected_result

    def print_test_case_info(self):
        print(f"ID тест-кейса:  {self.test_case_id}"
              f"\nНазвание: {self.name}"
              f"\nОписание шага: {self.step_description}"
              f"\nОжидаемый результат: {self.expected_result}")

#Создай подкласс ExtendedCase.       
class ExtendedCase(Case): 
    def __init__(self,test_case_id, name, step_description, expected_result, precondition:str, environment:str): #precondition и environment. Тип данных для них — строки.
        super().__init__(test_case_id, name, step_description, expected_result) #Он наследует все атрибуты из класса Case.  
        self.precondition=precondition
        self.environment=environment

    def print_test_case_info(self): #Переопредели метод print_test_case_info() в классе ExtendedCase.
        super().print_test_case_info()
        print(f"Предусловие: {self.precondition}"
              f"\nОкружение: {self.environment}")

#Создай объект case класса ExtendedCase. 
case = ExtendedCase('1', 'Наличие кнопки Принять', '1. Открыть вкладку приёма документов 2. Проверить наличие кнопки ', 'Кнопка доступна', 'Открыть сервис', 'Яндекс Браузер')
#Вызови метод print_test_case_info() для объекта casе.
case.print_test_case_info()