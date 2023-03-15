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




import datetime


class SmartPhones:
    battery = 0
    def __init__(self, name, color, memory) -> None:
        self.name = name
        self.color = color
        self.memory = memory

    def __str__(self) -> str:
        return self.name + ' ' + self.memory
    
    def charge(self, num):
        self.battery += num
        return self.battery
    
class Iphone(SmartPhones):
    def __init__(self, name, color, memory, ios) -> None:
        self.name = name
        self.color = color
        self.memory = memory
        self.ios = ios

    def send_imessage(self, meassage):
        res = f'sending {meassage} from {self.name} {self.memory }'
        return res

class Samsung(SmartPhones):
    def __init__(self, name, color, memory, android) -> None:
        self.name = name
        self.color = color
        self.memory = memory
        self.android = android

    def show_time(self):
        self.time_ = datetime.datetime.now().time()
        return self.time_


phone = SmartPhones('generic', 'blue', '128GB') 
print(phone)

print(phone.battery) 
phone.charge(20) 
print(phone.battery) 

iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello')) 

samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time()) 