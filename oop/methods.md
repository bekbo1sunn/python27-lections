# class/static/instance methods
> instance method - методы которые первым аргументом принимает
обьект от класса(instance, self). Используются они для работы с обьектом и его аттрибутами

```py
class A:
    def instance_method(self):
        print('метод обьекта')
        print('self', self)

obj = A()
obj.instance_method()
# метод обьекта
# self <__main__.A object at 0x7fa064d57af0>
```

> **class methods** - методы которые первым аргументом принимает
класс(cls). Используются они для работы с классом и его аттрибутами

```py
class A:
    @classmethod
    def class_method(cls):
        print('метод класса')
        print('cls', cls)

A.class_method()
# метод класса
# cls <class '__main__.A'>
```
> Для создания class метода, нужно использовать декоратор ` @classmethod `


> **static method**  - методы которые не взаимодейсвуют с обьектом и классом,
но находятся внутри класса (по принципу инкапсуляции)