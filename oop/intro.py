class Person:
    # переменные внутри класса это атрибуты
    arms = 2
    legs = 2

    def __init__(self, name) -> None:
        # __init__ dunder метод, который добавляет в оббект self атрибуты которые отличаются у разных обьектов
        self.name = name

    # функции внутри класса это методы
    def walk(): 
        print('Я хожу') 

person1 = Person('bekbolsun')
print(person1.name )

# Аттрибуты класса и аттрибуты обьекта класса 

class A:
    var1 = 'переменная класса'
    
    # def __init__(self) -> None:
    #     self.var2 = 'переменная обьекта'

obj = A()
print(obj)
        
# print(dir(A))