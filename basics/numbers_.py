"                                                                              Числа                                                                              "

# int - целые числа 

a = 5
print(type(a)) #<class 'int'>

b = '5'
print(type(b)) #<class 'str'>

c = int('10')
print(type(c)) #<class 'int'>


# float - числа с плавающей точкой (дробные)

a = 10.5 
print(type(a)) #<cass 'float'>

b = float('15.3')
print(type(b)) #<cass 'float'>


#print(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+)
# 0.999999999999999999999999


#decimal - точное дробное число 
# Чтобы его использовать нужно его импортировать 
from decimal import Decimal 
a = Decimal ('0.1')
print(a+a+a+a+a+a+a+a+a+a)
# a = 1.0 


# bin - бинарное число 
a = bin(10)
print(a) #0b1010

# чтобы перевести с бинарного в обычную СС
# b = int(a, 2)


# hex - 16 - система счисления 
# b = int(a, 16)


#complex - комплексные числа (3l+5j-7l)
a = complex (10,3)
print(a) #(10+3j)


'                                                                  Операции над числами                                                                        '


5+7 
10-9
2*5 
10/5
10//5 # цельночисленное деление 
5 % 2 # остаток от деления 
2 ** 3 # возведение в степень (8 = 2*2*2)
25 ** 0.5 # нахождения корня от числа (5)

# модуль числа 
abs(-5) # 5
abs(10) # 10

# pow 
#1. возводит в степень 
#2. находит остаток от деления на 3 - число 

pow(2, 3) # 8= 2*2*2=2**3
pow(2, 3, 4) # 0 = (2*2*2)%4 


# divmod 
# 1 число - целочисленное деление 
# 2 число - остаток от деления 
res = divmod(5, 2)
print (res)
# 2 = 5 // 2 
# 1 = 5 % 2 

divmod(17, 3)
# 17 // 3
# 17 % 3 


# sqrt - нахождение квадратного корня 
from math import sqrt # импортируем с библиотеки math 
sqrt(25)
sqrt (12)