    ### 19
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# x = 8
# res = []
# for i in list_:
#     if i >= x:
#         res.append(i)
# number = len(res)
# print(number)

    ### 20
# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# total = 0
# for i in list_:
#         if type(i) == int or i.isdigit():
#             total = total + int(i)
# print(total)

   ### 19
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# x = 8
# for x in list_:
#     number = list_.count(x)
# print(number)

# dict1  = {'a':1, 'b':2, 'c':3}
# res = {}
# for key, value in dict1.items():
#     res[value] = key 
# print(res)

# dict1 = {
#     'a':{'key':1},
#     'b':{'key':2},
#     'c':{'key':3},
# }
# res = {}
# for keys, values in dict1.items():
    
# print(res) 
   # 22
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = lists[0]
# min_list = lists[0]
# for i in lists:
#     if len(i) > len(max_list) and len(i) >= 0:
#             max_list = i
#     if len(i) < len(min_list) and len(i) >= 0:
#             min_list = i
# if len(max_list) > 1:
#     print(f'max_list {max_list}')
#     print(f'min_list {min_list}')
# else:
#     print(f'max_list {max_list}')
#     print(f'min_list {None}')

  ### 
# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list1 = []

# for i in range(step):
#     list1.append(list_[i::step])
# print(list1)

   ###35


# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# merge_from = input()
# merge_to = input()

# result = []
# temp = []
# for i in chars:
#     if i == merge_from:
#         temp.append(i)
#     elif i == merge_to:
#         temp.append(i)
#         result.append(''.join(temp))
#         temp = []
#     elif temp:
#         temp.append(i)
#     else:
#         result.append(i)

# print(result)

    ### 29
# import itertools
# list_ = [1, 2, 3]
# combinations = list(itertools.permutations(list_, len(list_)))
# for i in combinations:
#     print(i)

    ### 7 
# res = input()
# num = res.split(',')
# list_ = list(num)
# tuple_ = tuple(num)
# print(list_)
# print(tuple_)

   ### 8
# list_ = [1, 2, 3, 4]
# new_list = []
# for i in list_:
#     new_list.append(str(i))
# print(new_list)
    ### 18
# name1 = input().split()[-1]
# name2 = input().split()[-1]
# name3 = input().split()[-1]
# name4 = input().split()[-1]
# name5 = input().split()[-1]
# lists = [name1, name2, name3, name4, name5]
# lists.sort()
# print(lists)

  ### 25
# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# letter = input()

# result = []
# for i in list_:
#     if i[0] == letter:
#         result.append(i)
# print(result)


    ### 27
# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# res = []
# for i in list1:
#     if i in list2:
#         res.append(i)
# if len(res):
#     print(True)
# else: 
#     print(False)


### 28
# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# repeats = 3
# res = []
# for i in list_:
#     if list_.count(i) >= repeats and i not in res:
#         res.append(i)
# print(res)


   ### 31
# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# res = []
# for i in colors:
#     res.append(i[::-1])
# res.sort(key=len)
# print(res)
    

    ### 33 
# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]] 
# for i in lists:
#     res = max(lists, key=sum)
# print(res)

   ### 34
# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20] 
# repeated = [] 
# for i in list_: 
#     if list_.count(i) > 1: 
#         repeated.append(i) 
# print(repeated)

       #### Словари
# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)
   ### 8
# a = {'a': 1, 'b': 2, 'c': 1}
# res = {}
# for i in a.keys():
#     print(i)

   ### 9
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {} 
# for k, v in a.items(): 
#     if v%2==0: 
#         b.setdefault(k, 2) 
#     else: 
#         b.setdefault(k,v) 
# print(b)

    ### 10
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for keys, values in a.copy().items():
#     if values == None:
#             a.pop(keys)
# print(a)


   ### 11
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for k, v in a.items():
#     a[k] = v / 5 
# print(a)


    ### 12
# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for k, v in a.copy().items():
#     if v % 2 == 0:
#         a.pop(k)
# print(a)


   ### 13
# a = {'a': 1, 'b': 2, 'c': 3} 
# res = {}
# for key, value in a.items():
#     res[value] = key
# print(res)


   ### 17 
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# del dict_['a']
# print(dict_)


  ### 21  
# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# dict2 = {} 
# for k, v in dict1.items(): 
#     if v % 2 != 0: 
#         dict2.setdefault(k, 1) 
#     else: 
#         dict2.setdefault(k,v) 
# print(dict2)

    ### 22
# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for k, v in dict_.copy().items():
#     if v != None:
#         dict_.pop(k)
# print(dict_)


   ### 23
# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'}
# dict2 = {}
# for k, v in dict1.items():
#     dict2[k ** 2] = v
# print(dict2)


   ### 24 
# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {}
# for i in list_:
#     dict_[i] = len(i)
# print(dict_)


   ### 25
# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5} 
# max_ = max(dict_.values()) 
# for k in dict_.keys(): 
#     if dict_[k] == max_: 
#         print(k)


   ### 26 
# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {}
# for k, v in dict1.items():
#     dict2[k] = v ** 3
# print(dict2)


  ## 27
# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}} 
# for k,v in list(dict_.items()): 
#     for v2 in v.values(): 
#         dict_[k] = v2 
# print(dict_)


#    ## 28 

# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}} 
# dict2 = {} 
# for k,v in list(dict1.items()): 
#     res = 1 
#     for j in v.values(): 
#         res = res * j 
#     dict2[k] = res 
# print(dict2)


   ### 29
# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_ = {}
# res = []
# res1 = []
# for i in list_:
#    if type(i) == str:
#         res.append(i)
#    if type(i) == int:
#          res1.append(i)
# dict_ = dict(zip(res, res1))
# print(dict_)


    ### 30
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0} 
# sorted_values = sorted(dict_.values()) 
# sorted_dict = {} 
# for i in sorted_values: 
#     for k in dict_.keys(): 
#         if dict_[k] == i: 
#             sorted_dict[k] = dict_[k] 
# print(sorted_dict)


   ### 31
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0} 
# sorted_values = sorted(dict_.values(), reverse = True) 
# sorted_dict = {} 
# for i in sorted_values: 
#    for k in dict_.keys(): 
#       if dict_[k] == i: 
#          sorted_dict[k] = dict_[k]       
# print(sorted_dict)


   ### 32 
# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = input()
# if key in dict_:
#     print("Key is present in the dictionary")
# else:
#     print("Key is not present in the dictionary")


   ### 33
# dict1 = {1:10, 2:20} 
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60} 
# dict4={} 
# dict4.update(dict1) 
# dict4.update(dict2) 
# dict4.update(dict3) 
# print(dict4)


   ### 34 
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = {}
# dict_ = dict(zip(list1, list2))
# print(dict_)


   ### 35
# dict_ = { 'math': { 'sum': sum }, 'vars': { 'a': 5, 'b': 20, 'c': 50 } } 
# res = dict_.get('vars') 
# for k,v in dict_.items(): 
#    for j in v.values(): 
#       if type(j) != int: 
#          print(j(res.values()))


   ### 36
# a = {'a': 10, 'b': 9, 'c': 3} 
# result = 1 
# for key in a: 
#    result = result * a[key] 
# print(result)

# a = {4, 6, 100, -45, -6}
# b = {4, 5, -5, -6}
# res = a.difference(b)
# print(res)

# a = {4, 6, 100, -45, -6}
# b = {4, 5, -5, -6}
# if a.issuperset(b):
#    print('Надмножество!')

# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}
# if any(number in robert for number in kail) and any(number in robert for number in merri):
#     print("kail merri")
# elif any(number in robert for number in kail):
#     print("kail")
# elif any(number in robert for number in merri):
#     print("merri")
# else:
#     print("no one")


   ### 14
# tilek = {'Dodo', 'ImperiaPizza', 'FreshBox'} 
# timur = {'OchakKebab', 'FreshBox'}
# alexander = {'FreshBox', 'KFC'}
# elina = {'Dodo', 'ImperiaPizza', 'FreshBox', 'OchakKebab', 'KFC'}
# set1 = tilek.intersection(timur, alexander, elina)
# print(set1)


   ### 15
# ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 
# ingredients.add('помидор')
# ingredients.discard('колббаса')
# ingredients.remove('шпинат')
# ingredients.add('базилик')
# ingredients.discard('сыр чеддар')
# ingredients.add('сыр моцарелла')
# print(ingredients)


    ### 17
# set1 = {i for i in range(0, 10, 2)}
# set2 = {i for i in range(1, 10, 2)}
# res = set1.intersection(set2)
# if len(res) > 0:
#    print('Множества пересекаются!')
# else:
#    print('Множества не пересекаются!')


# a = [set(), set(), set()]
# inp1 = input()
# inp2 = int(input())
# if inp2 == 1:
#    print({inp1},{'default value'}, {'default value'})
# elif inp2 == 2:
#    print({'default value'}, {inp1}, {'default value'})
# elif inp2 == 3:
#    print({'default value'}, {'default value'}, {inp1})


   ### 16
# a = [{}, {}, {}] 
# inp1 = input()  
# inp2 = int(input())
# if inp2 == 1:
#     a[0] = {inp1}
# elif inp2 == 2:
#     a[1] = {inp1}
# elif inp2 == 3:
#     a[2] = {inp1}
# for i in range(len(a)):
#     if not a[i]:
#         a[i] = {"default value"}
# print(a)


# list_ = [i ** 2 if i % 2 == 0 else i for i in range(1, 11)]
# print(list_)


   ### 11
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {v:[k for k in range(1, k+1)] for v, k in a.items()}
# print(dict_)

   ### 12
# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k:'even' if i % 2 ==0 else 'odd' for k, i in dict_.items()}
# print(a)


   ### 13
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list1 = list(string_.split())
# list_ = [i for i in list1 if i.isdigit()]
# print(list_)

   ### 14 
# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# new_dict = {k:max(v, key=v.get) for k, v in dict_.items()}
# print(new_dict)
 
 

   ### 15
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k:y for k,v in my_dict.items() for x,y in v.items()} 
# print(dict_)


# list_ = [False, True, False, True, False, True, False, True, False, True] 
# list1 = [1 if x == True else 0 for x in list_]
# print(list1)


# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}} 
# list1 = [y for k,v in dict_.items() for x,y in v.items()] 
# print(list1)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# name = {k:len(k) ** 2 for k in list_name if len(k) > 4}
# print(name)


    ### 28
# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110} 
# list1 = [k.upper() for k,v in dict_.items() if 200 < v < 5000]
# print(list1)


   ### 29 
# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110} 
# dict2 = {k.replace('i',''):k.count('i') for k,v in dict1.items()} 
# print(dict2)



   ### 31 
# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# readers = [i for i, v in SPL_Patrons if v > 100]
# print(readers)



   ### 32
# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# saved_amount = [round(v * 11.95, 2) for k, v in SPL_Patrons ]
# print(saved_amount)



   ### 33
# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]
# spisok = [[x[0], x[1] * 42] for x in prairie_pirates if x[2]==True] 
# print(spisok)




   ### 34
# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }

# res = {v['likes'] for v in dict_.values() if v['rating'] > 3 }
# print(sum(res))



   ### 35
# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }
# dict1=[c['id'] for a,b in dict_.items() for c in b['comments'] if len(dict_[a]['comments'])>3] 
# print(dict1)


   ### 37
# dict_ = {1:'Hello', 2:'world', 3:'python'}
# dict_ = dict({k:len(v) if k % 2 == 0 else len(v) ** 3 for k, v in dict_.items()})
# print(dict_)


   ### 38
# set1 = {x for x in range(1,11)}
# set2 = {x for x in range(11, 21)}
# full_set = set1.union(set2)
# if len(full_set) < 20:
#     print(f'В этом сете было {20 - len(full_set)} повторения, его длина составляет {len(full_set)}')
# elif len(full_set) == 20:
#    print('Ваш объединенный сет полностью уникальный!')



# list_ = [1, 2, 3, 4]
# for i in range(0, len(list_) + 1):
#     print(list_[i])




# try:
#     inp1 = input()
#     list1 = []
#     list_ = []
#     list1.append(inp1)
#     for i in list1:
#         if i.isdigit():
#             list_.append(i)
            
# except ValueError:
#     print(' Данный элемент не является числом!')
        



    
