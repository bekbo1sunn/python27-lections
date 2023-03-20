class A:
    def instance_method(self):
        print('метод обьекта')
        print('self', self)

obj = A()
obj.instance_method()
# метод обьекта
# self <__main__.A object at 0x7fa064d57af0>
# когда мы вызываем метод у обьекта, то нам не нужно то нам не нужно 
# передавать его в self, он передаётся автоматически


A.instance_method(obj)
# метод обьекта
# self <__main__.A object at 0x7fa064d57af0>


class A:
    @classmethod
    def class_method(cls):
        print('метод класса')
        print('cls', cls)

A.class_method()
# метод класса
# cls <class '__main__.A'>

# примеры 
class C:
    counter = 0

    def __init__(self) -> None:
        # обьект создается
        self._inc_counter()

    def __del__(self):
        self._dec_counter()

    @classmethod
    def _inc_counter(cls):
        #cls - class c
        cls.counter += 1

    @classmethod
    def _dec_counter(cls):
        cls.counter -= 1

obj = C()
obj1 = C()
obj2 = C()
obj3 = C()
print(C.counter)

class Pizza:
    def __init__(self, radius, *ingredients):
        self.r = radius
        self.ingrdients = ingredients

    def cook(self):
        print(f'Пицца размером {self.r*2}')
        print(f'Ингредиенты {self.ingrdients}')

    @classmethod
    def four_cheese(cls, radius):
        pizza = cls(radius,'1cheese', '2cheese', '3cheese', '4cheese' )
        return pizza
    
pizza = Pizza(15, 'сыр, колбаса', 'помидор')
pizza.cook()

pizza4 = Pizza(15, '1cheese', '2cheese', '3cheese', '4cheese')
pizza4.cook()

pizza5 = Pizza.four_cheese(20)
pizza5.cook()

class A:
    @staticmethod
    def static_method():
        print('static method')

obj = A()
obj.static_method()

class Cylinder:
    def __init__(self, diameter, height) -> None:
        self.di = diameter
        self.h = height
        self.area = self.get_area(diameter, height)

    @staticmethod
    def get_area(di, h):
        from math import pi
        circle_area = pi * di**2 / 4
        side_area = pi * di * h
        return circle_area * 2 + side_area
    
obj = Cylinder(4, 10)
print(round(obj.area, 2))