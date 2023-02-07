"                                                                        Строки                                                                                   "


#Строки - неизменяемый тип данных, предназначенный  для хранения текста или последовательности символов

string1 = 'строка в 1 кавычках'
string2 = "Строка в 2 кавычках"
string3 = " Don't"
string4 = ' Study in "Makers Incubator"'
string5 = ''' 
многострочный текст
тут можно использовать любые "кавычки"  
'''
string6 = 'hello' + ' ' + 'world' # 'hello world'
string7 = 'hello' * 3 # 'hellohellohello'
string8 = 'hello' + str(1) 

'                                                                     Экранизация строк                                                                            '
print('hello\nworld') # перенос строки "\n" 
print('hello\tworld') # отступ (табуляция) '\t' 
print('\\')           # это отображение \
print('\'')           # это отображение ' 
print('\r')           # это перенос каретки в начал 
print('\v')           #перенос на новую строку со смещение на длину предыдущей строки


"                                                                        Индексация                                                                                 "
# индекс это прядковый номер символа в строке (начиная с 0)
" h e l l o"
# 0 1 2 3 4
#-5-4-3-2-1
string = 'hello world'
string[0]  #'h'
string[5]  #' '
string[-1] #'d'

#срез части строки 
print(string[6:9]) #'wor'
string[0:5]        #'hello' 
string[6:]         # от 6 до конца 
string[:7]         # от начало до 7
string[:]          # ничего не срезает
string[0:11:2]     # срез с шагом 2
string[::-1]       # обратная запись "dlrow olleh"


"                                                                      Форматирование строк                                                                       "

title = 'пирог'
price = 35 
string = f'Название {title}, цена: {price}'
#Название: пирог, цена: 35 

format1 = 'Название: %s, цена: %s'
print(format1 % ('Яблоко', 80))


format2 = 'Название : {}, цена: {}'
print(format2.format('Груша', 60))


"                                                                        Методы строк                                                                               "
# Метод - функция, которая принадлежит определенному типу данных, обращаемся к ней через точку 
print(dir(str))# посмотреть все доступные методы для данного типа данных 
'hello'.upper() # HELLO 
'HELLO'.lower() # hello 
'HeLLo'.swapcase() # hEllO 
'hello world'.title() # Hello World 
'hello world'.capitalize() #Hello world 
'hello'.center(11) # '   hello   '
'hello'.count('l') # 2 
'hello'.count('ll') #1 
'Hello'.count('hello') # 0 
'hello world'.split() #['hello', 'world'] 
'hello world'.split('o') # ['hell'. ' w', 'rld']
' '.join(['hello', 'world']) # hello world
'%'.join(['hello', 'world']) # hello%world
'hello world'.find('w') # 6 
'hello world'.find('o') # 4
'hello world'.rfind('0') #7 
