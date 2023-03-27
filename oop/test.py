   ### 3

# class MyString(str):
#     def __init__(self, word):
#         self.word = word
        

#     def append(self, word1):
#         # self.word1 = word1
#         self.word += word1
#         return self.word

#     def pop(self):
#         pop = self.word[-1]
#         self.word = self.word[:-1]
        
#         return pop


#     def __str__(self) -> str:
#         return self.word

# example = MyString('String') 
# example.append('hello') 
# print(example)

# print(example.pop()) 
# print(example) 

   ### 4
# class MyDict(dict):
#     def __init__(self, items):
#         self.items = items
#     def get(self, key):
#         self.key = key
#         for k, v in self.items.items():
#             if k == key:
#                 return v
#             else:
#                 return 'Are you kidding?'

# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some')) 
            

   ### 5
# class Person:
#     def display(self):
#         print(f'name:{self.name}, age:{self.age}')

# class Student(Person):
#     def __init__(self, name, age, faculty) -> None:
#             self.name = name
#             self.age = age
#             self.faculty = faculty

#     def display_student(self):
#         print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')


# obj_student = Student('Rick', 21, 'science')
# obj_student.display() 
# obj_student.display_student() 



   ### 6
# class ContactList(list):
#     def __init__(self, list1):
#         self.list1 = list1


#     def search_by_name(self, name):
#         self.name = name
#         res = []
#         for i in self.list1:
#             if self.name in i:
#                 res.append(i)

#         return res 
    
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya')) 



# import datetime


# class SmartPhones:
#     battery = 0
#     def __init__(self, name, color, memory) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory

#     def __str__(self) -> str:
#         return self.name + ' ' + self.memory
    
#     def charge(self, num):
#         self.battery += num
#         return self.battery
    
# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.ios = ios

#     def send_imessage(self, meassage):
#         res = f'sending {meassage} from {self.name, self.memory }'
#         return res

# class Samsung(SmartPhones):
#     def __init__(self, name, color, memory, android) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.android = android

#     def show_time(self):
#         self.time_ = datetime.datetime.now().strftime('%H:%M:%S')
#         return self.time_


# phone = SmartPhones('generic', 'blue', '128GB') 
# # print(phone)

# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello')) 

# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time()) 


   ### 7    

# import datetime


# class SmartPhones:
#     battery = 0
#     def __init__(self, name, color, memory) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory

#     def __str__(self) -> str:
#         return self.name + ' ' + self.memory
    
#     def charge(self, num):
#         self.battery += num
#         return self.battery
    
# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.ios = ios

#     def send_imessage(self, meassage):
#         res = f'sending {meassage} from {self.name} {self.memory }'
#         return res

# class Samsung(SmartPhones):
#     def __init__(self, name, color, memory, android) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.android = android

#     def show_time(self):
#         self.time_ = datetime.datetime.now().time()
#         return self.time_


# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone)

# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 

# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello')) 

# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())   


# class CustomError(Exception):
#     def __init__(self, word):
#         self.word = word
        

#     def capitals_error(self, capitals_error):
#             raise capitals_error('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
        
# def check_letters(string:str):
#     if string.isupper():
#         print(f'ВСЕ ОТЛИЧНО! {string}')
#     else:
#         string = CustomError(string)
#         string.capitals_error()

# check_letters("hello")
   ### 8 
# верный ответ

# class CustomError(Exception): 
#    def __init__(self, message): 
#       self.message = message 
# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def check_letters(message1): 
#    if message1 == message1.upper(): 
#       return f'ВСЕ ОТЛИЧНО! {message1}' 
#    else: 
#       raise capitals_error 
   
# print(check_letters("hello"))





# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'


# class Employee(Person):
#     def __init__(self,name, last_name, work, status):
#         self.name = name
#         self.last_name =last_name
#         self.work = work
#         self.status = status

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}'



# class Student(Person):
#     def __init__(self,name, last_name, university, course):
#         self.name = name
#         self.last_name =last_name
#         self.university = university
#         self.course = course

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе'

# def get_human_info(string):
#     print(string.get_info())

# employee = Employee('Иван', 'Петров','Рога и копыта', 'директор')
# student = Student('Иван', 'Петров','КГТУ', 3)
# person = Person('Иван', 'Петров')

# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person) 


# from abc import ABC, abstractmethod
# from math import pi
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
    
# class Triangle(Shape):
#     def __init__(self, base, height) -> None:
#         self.base = base
#         self.height = height

#     def get_area(self):
#         res = self.base * self.height / 2
#         return res

# class Square(Shape):
#     def __init__(self, lenght) -> None:
#         self.lenght = lenght

#     def get_area(self):
#         res = self.lenght ** 2
#         return res

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         self.radius = radius
#     def get_area(self):
        
#         res = pi * self.radius**2
#         return res

# triangle = Triangle(5,5)
# square = Square(5)
# circle = Circle(5)


# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area())

# """
# 1) Создайте класс Auto в нем реализуйте метод ride который выводит сообщение 'Riding on a ground'.

# Создайте класс Boat реализуйте метод swim, который выводит 'Floating on water'.

# Создайте класс Amphibian который наследуется от класса Auto и Boat.

# Создайте от него объект obj и вызовите все методы.

# Ввод:

# obj = Amphibian() 
# obj.ride() 
# obj.swim() 
# Вывод:

# Riding on a ground 
# Floating on water 
# """

# class Auto:
#   def ride(self):
#     print('Riding on a ground')

# class Boat:
#   def swim(self):
#     print('Floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian() 
# obj.ride() 
# obj.swim() 


    
# """
# 2)Создайте класс ContactList, который должен наследоваться от встроенного класса list.

# В вашем классе должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений.

# Создайте экземпляр класса в переменной all_contacts и передайте список ваших контактов.

# Примерный ввод:

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya')) 
# Метод search_by_name возвращает все строки содержащие подстроку "Olya":

# ['Ivan Olya', 'Olya Ivan'] 
# """

# class ContactList(list):
#   def __init__(self, list_):
#     self.list_ = list_

#   def search_by_name(self, name):
#     res = []
#     for i in self.list_:
#       if name in i:
#         res.append(i)
#     return res
    
# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya')) 
  
    
    
    


# """

# 3) Напишите класс Person, который будет хранить информацию о пользователе. У объекта будут следующие атрибуты экземпляра класса: имя(name), фамилия(last_name), возраст(age), почта (email).
# При инициализации объекта, передавать аргументы классу не нужно, все его атрибуты по умолчанию будут равны None и также все они будут приватными.
# Поэтому реализуйте для каждого атрибута методы доступа get и set не используя декораторы property и setter. У вас будут такие методы: get_name, set_name, get_last_name, set_last_name, get_age, set_age, get_email, set_email.
# Создайте экземпляр john класса Person выедите все его атрибуты, затем измените их как показано ниже и после снова выведите на экран.
# Пример:

# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com
# """

# class Person:
#     def __init__(self):
#       self.name = None
#       self.last_name = None
#       self.age = None
#       self.email = None

      
#     def set_name(self, __name):
#       self.name = __name
#       return self.name

#     def get_name(self): 
#         return self.name
      
#     def set_last_name(self, __last_name):
#       self.last_name = __last_name
#       return self.last_name

#     def get_last_name(self):
#       return self.last_name

#     def set_age(self, __age):
#       self.age = __age
#       return self.age

#     def get_age(self):
#       return self.age
    
#     def set_email(self, __email):
#       self.email = __email
#       return self.age

#     def get_email(self):
#       return self.email
      

# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.co
      

###  5
# class OS:
#     def __init__(self, version):
#         self.version = version

# class Windows(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами CTRL + C'

# class MacOS(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами COMMAND + C'
# class Linux(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами CTRL + SHIFT + C'

# win = Windows(2)
# mac = MacOS(2)
# lin = Linux(2)

# print(win.copy("Полиморфизм — одна из основных парадигм ООП"))
 
# print(mac.copy("Полиморфизм - разное поведение одного и того же метода в разных классах")) 
 
# print(lin.copy("На самом деле одинаковым является только имя метода, его исходный код зависит от класса"))

  ### 6 
# class Language:
#     def __init__(self, level, type):
#         self.level = level
#         self.type = type

# class Python(Language):
#     def write_function(self, func_name, arg):
#         self.func_name = func_name
#         self.arg = arg
#         return f'def {self.func_name}({arg}):'

#     def create_variable(self, var_name, value):
#         self.var_name = var_name
#         self.value = value
#         if type(value) == str:
#             return f"{self.var_name} = '{self.value}'"
#         return f"{self.var_name} = {self.value}"

# class JavaScript(Language):
#     def write_function(self, func_name, arg):
#         self.func_name = func_name
#         self.arg = arg
#         a = '{     }'
#         return f'function {func_name}({arg}) {a};'

#     def create_variable(self, var_name, value):
#         self.var_name = var_name
#         self.value = value
#         if type(value) == str:
#             return f"let {self.var_name} = '{self.value}';"
#         return f"let {self.var_name} = {self.value};"

# py = Python(1, 2)
# js = JavaScript(1, 2)

# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))

# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))


   ### 7
# class Money:
#     def __init__(self, country, symbol):
#         self.country = country
#         self.symbol = symbol

# class Dollar(Money):
#     rate = 84.80
#     def exchange(self, num):
#         amount = f'$ {num} равен {self.rate * num} сомам'
#         return amount

# class Euro(Money):
#     rate = 98.40
#     def exchange(self, num):
#         amount = f'€ {num} равен {self.rate * num} сомам'
#         return amount

# dollar = Dollar('USA', '$')
# euro = Euro('sadas', '#')

# print(dollar.exchange(100))
# print(euro.exchange(100))


# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         area = self.pi * self.radius ** 2
#         return area

# circle = Circle(2)
# Circle.color = 'синий'
# print(circle.color) 
# print(circle.get_area()) 

# from abc import ab



# class MoneyFmt:
#     def __init__(self, amount):
#         self.amount = amount
    
#     @staticmethod
#     def dollarize(float_num):
#         if float_num >= 0:
#             return f"${float_num:,.2f}"
#         float_num = abs(float_num)
#         return f"-${float_num:,.2f}"

#     def update(self, new_amount):
#         self.amount = new_amount
    
#     def __repr__(self):
#         return str(self.amount)
    
#     def __str__(self):
#         return self.dollarize(self.amount)

# cash = MoneyFmt(12345678.021) 
# print(cash) 
# cash.update(100000.4567) 
# print(cash) 
# cash.update(-0.3) 
# print(cash) 
# print(repr(cash))

      # 1 
# class Product:
#     base_price = 20000
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color

#     def has_garantiya(self, year):
#         if year > self.year + 2:
#             return 'Ваша гарантия истекла '
#         return 'Гарантия действительна'

#     def change_price(self, rate):
#         rate = 20
#         procent = self.base_price / 100 * rate
#         self.base_price = self.base_price + procent
#         return self.base_price

# obj = Product('A218', 2008, 'red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2010)) 
# print(obj.base_price)    


    # 3 mixins
# from datetime import datetime
# class Clock:
#     def current_time(self):
#         print(datetime.now().strftime("%H:%M:%S"))
    
# class Alarm:
#     def on(self):
#         print("Будильник включен")

#     def off(self):
#         print("Будильник выключен")

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         self.on()

# clock = AlarmClock()
# clock.current_time() 
# clock.alarm_on()



# from datetime import datetime
# class Clock:
#     @staticmethod
#     def current_time():
#         print(datetime.now().strftime("%H:%M:%S"))
    
# class Alarm:
#     @staticmethod
#     def on():
#         print("Будильник включен")

#     @staticmethod
#     def off():
#         print("Будильник выключен")

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         self.on()

# clock = AlarmClock()
# clock.current_time() 
# clock.alarm_on()



# class RadioMixin:
#     def play_music(self, title):
#         print(f'Песня называется {title}')

# class Auto(RadioMixin):
#   def ride(self):
#     print('Riding on a ground')

# class Boat(RadioMixin):
#   def swim(self):
#     print('Floating on water')

# class Amphibian(Auto, Boat, RadioMixin):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian() 
# auto.play_music('hello')
# boat.play_music('world')
# obj.play_music('fsfdasd')



# from datetime import datetime 

# class CreateMixin: 
#     def create(self, todo, key): 
#         if key in self.todos: 
#             return 'Задача под таким ключом уже существует' 
#         self.todos[key] = todo 
#         return self.todos 

# class DeleteMixin: 
#     def delete(self, key): 
#         delete_ = self.todos.pop(key, None) 
#         if not delete_:
#             return 'нет такого ключа'
#         return delete_

# class UpdateMixin: 
#     def update(self, key, new_value): 
#         self.todos[key] = new_value 
#         return self.todos 

# class ReadMixin: 
#     def read(self): 
#         return sorted(self.todos.items())

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin): 
#     todos = {} 

#     def set_deadline(self, deadline): 
#         day, month, year = deadline.split("/")
#         datetime_deadline = datetime(int(year), int(month), int(day))
#         datetime_now = datetime.now()
#         return (datetime_deadline - datetime_now).days + 1

# task = ToDo() 
# print(task.set_deadline('31/12/2022'))
