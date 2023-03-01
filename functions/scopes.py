# '                                                                   Области видимости / пространства имен                                                        '
# # LEGB - (local, enclosed, global, build - in)





# # чтобы посмотреть все глобальные переменные - globals

# a = 5
# b = 7
# print(globals())




# var = 'глобальная'

# def func():
#     var = 'замкнутое'
#     def inner_func():
#         var = 'локальное'
#         def inner_inner_func():
#             var = 'Супер локальная переменная'
#             print(var)
#         print(var)
#         inner_inner_func()
#     print(var)
#     inner_func()
# func()
# print(var)

# local - пространство внутри функции(локальное пространство)

# a = 'hello'
# def func(a,b):
#     print('GLOBAL', globals())
#     print('LOCAL', locals())

# func(10, 50)

# num1 = 10
# def func():
#      print(num1)

# func()

# def count(i):
#     counter = 0
#     def increase_counter():
#         nonlocal counter
#         counter += 1
#         print(counter)

#     for _ in range(i):
#         increase_counter()

# count(10)

# def func():
#     a = 10
#     def inner_func():
#         a = 15
#         def inner_inner_func():
#             nonlocal a 
#             a += 1
#         inner_inner_func()
#         print(a)
#     inner_func()

# func()

print(globals())