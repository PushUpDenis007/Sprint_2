#Он рассчитывает почасовую заработную плату сотрудников за неделю.
class EmployeeSalary:
    hourly_payment=400 #С помощью переменной hourly_payment установи почасовой уровень оплаты, равный 400.

    def __init__(self,name, hours, rest_days, email): #Проинициализируй атрибуты name, hours, rest_days, email через конструктор.
        self.name=name
        self.hours=hours
        self.rest_days=rest_days
        self.email=email
    
    @classmethod
    def get_hours(cls,name, rest_days, email):
        hours=(7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod 
    def get_email(cls,name, hours, rest_days):
        return cls(name, hours, rest_days, email=f"{name}@email.com")
    
    @classmethod
    def set_hourly_payment(cls,hourly_payment):
        cls.hourly_payment=hourly_payment
    
    def salary(self):
        return self.hours * self.hourly_payment

#проверка
Inna=EmployeeSalary.get_hours(name=123,rest_days=3,email=123)
print (f'{Inna.__dict__} \n {Inna.salary()}')
Sergey=EmployeeSalary.get_email(name=123,hours=2,rest_days=3)
print (f'{Sergey.__dict__} \n {Sergey.salary()}')
EmployeeSalary.set_hourly_payment(10)
print (f'{Inna.salary()}')
print (f'{Sergey.salary()}')