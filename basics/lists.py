"                                                                          List                                                                                    "

# Список - это изменяемый тип данных, итерируемый, индексируемый и 
# упорядоченный тип данных, предназначенный для хранения элементов в строгом порядке

# list1 = [1, 2.5 , 'hello', [1, 2, 3], (1, 2), None, True, False ]
# list1[0] # 10
# list1[3] # [1, 2, 3]
# list1[3][-1] # 3 


"                                                                         Изменяемость                                                                             " 


# string = 'hello'
# res = string.upper()
# print(string) #hello
# print(res) #HELLO


# list1 = []
# list1.append(1)
# print(list1)

"                                                                          Методы                                                                               "


# append - метод который добавляет элемент в конец списка

# list1 = []
# list1.append('hello')
# list1.append(500)
# list1.append([1,2,3])
# print(list1) # ['hello', 500, [1,2,3]]

# # remove - метод, который удаляет елемент из списка по значению,
# # только первого вхождения этого элемента, выдаст ошибку если такого элемента нет в списке
# list2 = [10, 'hello', 20, 'world', 'hello']
# list2.remove('hello') 
# print(list2) #[10, 20, 'world', 'hello'] 


# # pop - метод который удаляет элемент из списка по индексу, 
# # если этого индекса нет тo выдаст ошибку
# list3 = [1, 2, 6, 7, 9, 54]
# list3.pop(0)
# print(list3)
# # также возвращает удаленный элемент 


# # insert - добавляет элемент по индексу  
# list5 = [1,2,3,4,5]
# list5.insert(0, 'hello')
# print(list5) 


# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list1.reverse())

# print(list(reversed(list1)))
# print(list1[::-1])

#clear - чистит список 
# list1 = [1, 2, 3, 4]
# print(list1.clear())

# count - считает количество элемента, который передаем в метод в списке
# list1 = [1,2,3,4,5,1,2,3,4,5,1,2,3]
# list1.count(1) # 3
# list1.count(5) # 2
# list1 = ['hello', 'hello', 'hello']
# list1.count('hello') # 3 
# list1.count('l') # 0

# list1 = [11, 12, 13]
# list1.count(1) #0

# index - возвращает индекс элемента

# sort - метод который сортирует по возрастанию 
# если указать .sort(reverse=True)


# copy - возвращает копию списка 
list1 = [1,2,3]
list2 = list1.copy()

# extend - расширяет список другим списком
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list1.append(list2)
print(list1) 

list1.extend(list2)