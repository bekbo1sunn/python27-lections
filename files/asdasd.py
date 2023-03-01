# with open("task3.txt", "w") as file:
#     file.write("0*1*2*3*4*5*6*7*8*9*")
#     file.seek(0)
#     print(file)



with open("task5.txt") as file:
    list_ = [int(el.replace('\n', '')) for el in file]
    
    with open("task6.txt", "w+") as file1:
        file1.write(f'{str(min(list_))}-{str(max(list_))}')


# with open("task5.txt") as file:
#     min_ = min(file)
#     file.seek(0)
#     max_ = max(file)
    
#     with open("task6.txt", "w+") as file1:
#         file1.write(f'{str(min_)}-{str(max_)}')
    # print(file.read())