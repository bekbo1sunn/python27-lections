# with open("task3.txt", "w") as file:
#     file.write("0*1*2*3*4*5*6*7*8*9*")
#     file.seek(0)
#     print(file)



# with open("task5.txt") as file:
#     list_ = [int(el.replace('\n', '')) for el in file]
    
#     with open("task6.txt", "w+") as file1:
#         file1.write(f'{str(min(list_))}-{str(max(list_))}')


# with open("task5.txt") as file:
#     min_ = min(file)
#     file.seek(0)
#     max_ = max(file)
    
#     with open("task6.txt", "w+") as file1:
#         file1.write(f'{str(min_)}-{str(max_)}')
    # print(file.read())

    ### 6
# def read_last(lines, filename): 
#     with open(filename) as file: 
#         list_ = file.readlines() 
#         if lines < len(list_): 
#             i = 0 
#             reversed_list_ = list_[::-1] 
#             while i<lines: 
#                 print(reversed_list_[i].replace('\n', '')) 
#                 i+=1 
#         else: 
#             list_.reverse() 
#             for i in list_: 
#                 print(i.replace('\n', '')) 


import json
with open('db.json') as file:
    string = file.read()
    list_ = json.loads(string)

for i in list_:
    i['description'] = '...'

with open('new_db.json', 'w') as file:
    file.write(str(list_))
    
# read_last(1, 'article.txt')