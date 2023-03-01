
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operator = input("Выберите оператор (+, -, *, **, /, //, %): ")
    if operator == "+":
        result = num1 + num2
        print(f"Результат: {result}") 
    elif operator == "-":
        result = num1 - num2
        print(f"Результат: {result}") 
    elif operator == "*":
        result = num1 * num2
        print(f"Результат: {result}") 
    elif operator == '**':
         result = num1 ** num2
         print(f"Результат: {result}") 
    elif operator == "/":
        result = num1 / num2
        print(f"Результат: {result}") 
    elif operator == '//':
        result = num1 // num2 
        print(f"Результат: {result}") 
    elif operator == '%':
        result = num1 % num2
        print(f"Результат: {result}") 
    else:
        print("Данной операции нет в системе")  
except ValueError:
        print("Введены не корректные данные")
except ZeroDivisionError:
     print('Нельзя делить на ноль')
