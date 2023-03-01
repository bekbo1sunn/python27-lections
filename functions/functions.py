"                                                                          Функции                                                                                  "
# функции - именованный блок кода


func = lambda num1, num2: num1 + num2
res = func(5, 10)
print(res)
# lambda - ключевое слово, для создания анонимной функции

def my_sum2(num1, num2):
    return num1 + num2 
print(my_sum2(3, 6))

def calc(num1, num2, oper):
    """
    oper - строка с операцией для вычислений 
    """

    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2 
    if oper == '*':
        return num1 * num2
    if oper == '/':
        return num1 / num2
print(calc(5,6,'*'))
print(calc(5,6,'//'))


def my_len(obj):
    'Возвращает длину обьекта'
    count = 0
    for i in obj:
        count += 1
    return count
print(my_len([2,3,4,5]))


def super_len(obj):
    try:
        return my_len(obj)
    except:
        return(my_len(str(obj)))
print(super_len([1,2,3,4,5,6,7]))
print(super_len(123456789))
print(super_len(None))
print(super_len(False))


"                                                                              DRY                                                                                "
# DRY - don't repeat yourself 

str_ = 'hello world'
print(my_len(str_))

"                                                                        Аргументы и параметры                                                                 "
# параметры - локальные переменные, значение которых мы задаем при вызове функции 
# аргументы - значения, которые мы задаем параметрам при вызове функции 
def func(var):
    local_var = 5
    print(locals())

func(6)

"                                                                       Виды параметров                                                                      "
# 1. обязательные 
# 2. необязательные 
# 2.1с дефолтным значением (по умолчание)
# 2.2 args(аргументы)
# 2.3 kwargs (key word arguments)


def func(a, b= 'default', *args, **kwargs):
    print(a, b, args, kwargs)

func('hello') 
func('hello', 100)
func('hello', 100, 84, 24, 'world')


"                                                                      Виды аргументов                                                                         "
# позиционные (по порядку параметров)
# именованные (по имени параметров)                         Мы ничего интересного не придумали, так что просто похлопайте)
def func2(a, b):
    print(f'a={a},b={b}') 

func2(10, 20) # позиционные 
func2(b=10, a=20) # именнованные 
func(1,2,3, key1='value')
'                                                                           Звездочки                                                                              '
list1 = [1,2,3,4]
list2 = [*list1]
print(list2)
dict_ = {'a':1, 'b':2}
list3 = [*dict_]
print(list3)



