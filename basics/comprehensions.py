"===================Comprehensions==================="
# генератор, с помощью которого можно создавать последовательность используя цикл for

# list1 = []
# for i in range(1, 11):
#     list1.append(i)
# # list1 = [1,2,3,4,5,6,7,8,9,10]

# list1 = [i for i in range(1,11)]
# # print(list1)  [1,2,3,4,5,6,7,8,9,10]

# # результат for элемент in последовательность
# # результат for элемент in последовательность if фильтр

# comprehensions = (i for i in range(1, 11))


# генератор - итерируемый обьект, который не хранит в себе 
# полностью все элементы последовательности, а генерирует их когда требуется 

# print(next(comprehensions)) #1
# print(next(comprehensions)) #2
# print(next(comprehensions)) #3
# print(next(comprehensions)) #StopIteration

# # next - функция которая принимает в себя генератор, запрашивает следующий 
# # элемент у генератора и возвращает его 


# "                                                                  Синтаксический сахар                                                                        "
# # list comprehensions 
# list_compr = [i for i in 'hello']
# print(list_compr)
# # ['h', 'e', 'l', 'l', 'o']


# # dict comprehensions 
# dict_compr = {i:str(i) for i in range(1,4)}


# # фильтр 
# string = 'HelLo WorlD'
# res = [i for i in string if i.islower()]
# print(res)


# res = []

# for i in string:
#     if i.islower():
#         res.append(i)
# print(res)


# list1 = list(range(0, 11, 2))
# print(list1)


# list2 = list(range(0, 11))
# res = []
# for i in list2:
#     if i % 2 == 0:
#         res.append(i)
# print(res)


# res = [i * 100 for i in range(1, 11)]
# print(res)


# res = ['hello' for i in range(5)]
# print(res)

# list_ = ['a', 'b', 'c']
# res = [f'Hello {i}' for i in list_]
# print(res)

# res = [[x for x in range(1, i +1)] for i in range(1, 6)]
# print(res)

res = []
for  i in range(1, 6):
    inner_list = []
    for x in range(1, i +1):
        inner_list.append(x)
    res.append(inner_list)
print(res)


list1 = [[1,2,3], [4,5,6], [7,8,9]]
res = [i for inner_list in list1 for i in inner_list]
print(res)


res = ["четное" if i % 2 == 0 else 'нечетное' for i in range(1,7) ]
print(res) 

dict1 = {'a':1, 'b':2, 'c':3}
res = {v:k for k, v in dict1.items() }
print(res)


res = {i:[x for x in range(1, i +1)] for i in range(1, 6)}
print(res)



# set comprehensions 
set_comp = {x for x in range(10)}
print(set_comp)

