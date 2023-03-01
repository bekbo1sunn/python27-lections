   ### 12
# def func12(list1, b): 
#     a = [] 
#     for i in list1: 
#         if b == 'lower': 
#             a.append(i.lower()) 
#         elif b == 'upper': 
#             a.append(i.upper()) 
#     return (a) 
# func12(["hEllo", "wORld"], 'lower')




   ### 13
# def func13(str): 
#     return {x:str.count(x) for x in str} 
# print(func13("Hello")) 



   ### 14

# def add_(a, b): 
#     return a + b 
# def sub_(a, b): 
#     return a - b 
# def mult_(a, b): 
#     return a * b 
# def div_(a, b): 
#     return a / b 
# def calc(num1,num2, operation): 
#     if operation == "+": 
#         return add_(num1, num2) 
#     elif operation == "-": 
#         return sub_(num1, num2) 
#     elif operation == "*": 
#         return mult_(num1, num2) 
#     elif operation == "/": 
#         return div_(num1, num2) 
# print(calc(40, 20, operation = "+"))



   ### 15
# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]
# def func15(users): 
#     r=[] 
#     for i in users: 
#         if i['work'].startswith('IT'): 
#             r.append(f"{i['name']}, скидки в магазине компьютерной техники!\n") 
#     h=''.join(i for i in r) 
#     return h 
# print(func15(users))


   ### 17
# employees = [ {'name': 'Jack', 'salary': 10000, 'overTime': 4}, 
#              {'name': 'Tom', 'salary': 15000, 'overTime': 3}, 
#              {'name': 'Jessica', 'salary': 20000, 'overTime': 9}, 
#              {'name': 'Helen', 'salary': 25000, 'overTime': 2}, 
#              {'name': 'Peter', 'salary': 30000, 'overTime': 7} ] 
# def func17(employees): 
#     for x in employees: 
#         if 'overTime' in x: 
#             x['salary']+=x['overTime']*200 
#             x.pop('overTime') 
#     return employees 
# print(func17(employees))




   ### 18
# list_ = [1, 'hello']
# def func18(list_):
#     list1 = []
#     list2 = []
#     for i in list_:
#         if type(i) == int:
#             list1.append(i)
#         elif type(i) == str:
#             list2.append(i)
#     return list1, list2
# print(func18(list_))



   ### 16 
# def func16(x, y):
#     res = y / x * 100
#     return f'На 100км было расходовано {round(res)}л горючего'




# def func(num):
#    if num % 2 == 0:
#       return f'Число {num} чётное'
#    return f'Число {num} нечётное'

# x = int(input())
# print(func(x))
      
    

# def func(parameter1, parameter2):
#    print(parameter1  + parameter2) 

# func(5,6)  # 5 и 6 это у нас аргументы



# def func(a, b):
#    return a - b                      # Позиционные ()

# print(func(10, 15))  # -5                  


    


# def func(a, b,*args, **kwargs):
#    return args, kwargs

# print(func(12,345,643, a=212))   # 5




# list1 = [1,2,3,4,5,6,7,8,9,10]

# def filter_nums(num):
#    res = []
#    for i in num:
#       if i % 2 == 0:                                
#          res.append(i)
#    return res









# list2 = [10,9,8,7,6,5,4,3,2,1]

# print(filter_nums(list2))    # [10,8,6,4,2]          



# def func(a, b, c):
#    return a

# print(func(a=5))






  ### 19
# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]

# def func(a):
#    for i in a:
#       a.sort(key=lambda a:a['marks'], reverse=True)
#    return a
# print(func(students))



# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]
# res = []

# def func20(x1,y1):
#     y = y1.lower()
#     for i in products:
#         for k, v in i.items():
#             if y in i['title']:
#                 res.append(i)
#     return res
# print(func20(products, 'i'))




    ### 4 
# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount
# def pay_bills(amount, log_name):
#     global balance 
#     balance -= amount
#     print(f'Вы заплатили {amount} сом за {log_name}')
# def get_balance():
#     print(f'У вас на счету {balance} сом')
# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

def count_symbols(string):
    list1 = 'ёуеыаоэяию'
    list2 = 'йцкнгшщзхъфвпрлджчсмтбь'
    res = []
    res1 = []
    res2 = []
    for i in string:
        i = str(i)
        x = i.lower()
        if x in list1:
            res.append(i)
        elif x in list2:
            res1.append(i)
        else:
            res2.append(i)
    return f'Количество гласных: {len(res)}, согласных: {len(res1)}, остальных символов: {len(res2)}'
print(count_symbols('Привет'))



