

# print(5 == 5) True
# print(5 == 4) False

# " = " --- Знак присвоения 
# " == " --- Знак сравнения 

# print(4 != 5) -- True 
# print(4 != 4) -- False


# print(5 >= 10) False
# print(5 <= 10) True 


# print('5' == 5) False 
# print('hello' == 'hello') True
# print('Hello' == 'hello') False

"                                                                      AND OR NOT                                                                            "


# and --- Если хотя бы одно выражение False, программа выдает False 
# or --- Если хотя бы одно выражение True, программа выдает True
 #'a = 5' 
# not --- Отрицание (not a == 5) False 

'                                                                    Boolean Type                                                                            '

# У булевого типа всего 2 значения True и False

# print(bool(1)) --- True
# print(bool(0)) --- False
# print(bool(-11)) --- True

# print(bool('Hello')) --- True 
# print(bool('')) --- False
# print(bool(' ')) --- True 


"                                                                     None Type                                                                              "


# None - неизменяемый тип данных с одним значением None,
# который используется для обозначения пустоты
# print(bool(None)) --- False
# print(bool('None')) --- True


"                                                                   Условные операторы                                                                      "


# условные операторы - конструкция, которая исползуется для того, 
# чтобы при разных входных данных код работал по разному (в зависимости от условия)

# if условие1:
#    тело1 
#        # тело1 будет выполняться только если условие1 верно 
#else:
#    тело2 
        # тело2 будет выполняться во всех других случаях


'--------------------------------------------------------------'
# if условие1:
#   тело1 
#       # тело1 будет выполняться только если условие1 верно 
# elif условие2:
#    тело2
        # тело2 будет выполняться только если условие2 верно 
# else:
#    тело3
        # тело3 будет выполняться во всех других случаях


# В одной конструкции мы можем использовать только 1 if, 
# неогринеченное количество elif, 
# и 1 else 


# num = int(input())
# if num > 0:
#     print(f'число {num} - положительное')
# elif num == 0:
#     print(f'число {num} - это 0')
# else:
#     print(f'число {num} - отрицательное')


# password = input('Придумайте свой пароль: ')
# first_let = password[0].upper()
# if not len(password) >= 8:
#     print('Ваш пароль меньше 8 символов') 
# elif not password.startswith(first_let):
#     print('Ваш пароль не начинается с большой буквы')
# else:
#     print('Успешно создан пароль')


"                                                                    Тернарные операторы                                                                      "

# Тернарные операторы - условие в одну строку 

# тело1 if условие else тело2

# num = int(input())
# res = "Hello" if num == 5 else "Bye"
# print(res)


"                                                                         FizzBuzz                                                                              "


# num = int(input())
# if num % 3 == 0 and num % 5 == 0:
#     print('FizzBuzz')
    
# elif num % 5 == 0:
#     print('Buzz')
# elif num % 3 == 0:
#     print('Fizz')
# else:
#     print(num)
