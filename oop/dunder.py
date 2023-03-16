# dunder (double underscore) - методы у которых 2 в начале и в конце
# магия в том что мы их не вызываем напрямую 

class A:
    def __new__(cls):
        print('__NEW__')
        return super().__new__(cls)
    
    def __init__(self) -> None:
        print('__INIT__')
        pass
        
obj = A()
#__NEW__
#__INIT__  - вызываются при создании обьекта 

print(dir(object))

# __eq__ ==
# __ge__ >=
# __gt__ >
# __le__ <=
# __lt__ <
# __ne__ !=
# __sub__ -
# __floordiv__ /
# __truediv__ //

# __str__ - str, print 
