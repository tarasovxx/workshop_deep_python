class MyClass:
   def __init__(self):
       self._protected_var = 10    #protected attribute

       self.__private_var = 20     #private attribute

   def _protected_method(self):      #protected method
       return "protected metchod"

   def __private_method(self):      #private method
       return "private method"

   def public_method(self):
        result = self._protected_var
        s = ""
        i = 0
        s += self._protected_method()
        i += self.__private_var
        s += self.__private_method()
        return s


# Определение базового класса (суперкласса)
class Animal:
   def __init__(self, name):
       self.name = name

   def speak(self):
       pass

# Определение подкласса, который наследует базовый класс
class Dog(Animal):
   def speak(self):
       return f"{self.name} говорит: Гав!"

# Создание объектов классов
animal = Animal("Животное")
dog = Dog("Бобик")

# Вызов метода speak() для каждого объекта
print(animal.speak())  # Выведет: None (нет реализации в базовом классе)
print(dog.speak())  # Выведет: Бобик говорит: Гав!


# Определение базового класса (суперкласса)
class Shape:
   def area(self):
       pass

# Определение подклассов с переопределением метода area()
class Circle(Shape):
   def __init__(self, radius):
       self.radius = radius

   def area(self):
       return 3.14 * self.radius ** 2

class Square(Shape):
   def __init__(self, side_length):
       self.side_length = side_length

   def area(self):
       return self.side_length ** 2


class Engine:
    def start(self):
        print("Двигатель запущен")

    def stop(self):
        print("Двигатель остановлен")

class Car:
    def __init__(self):
        self.engine = Engine()  # Композиция: объект Car содержит объект Engine

    def drive(self):
        print("Автомобиль начал движение")
        self.engine.start()

    def park(self):
        print("Автомобиль припаркован")
        self.engine.stop()


class Parent1:
    def method1(self):
        return "Метод 1 из Parent1"

class Parent2:
    def method2(self):
        return "Метод 2 из Parent2"

class Child(Parent1, Parent2):
    def method3(self):
        return "Метод 3 из Child"

child = Child()

result1 = child.method1()
result2 = child.method2()
result3 = child.method3()

# Вывод результатов
print(result1)  # Выведет: Метод 1 из Parent1
print(result2)  # Выведет: Метод 2 из Parent2
print(result3)  # Выведет: Метод 3 из Child

import sys
class LookingGlass:
    def __enter__(self) -> str:
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return "Some String"

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print("Please DO NOT divide by zero!")
            ## сообщаем интерпретатору, что было обработано исключение
            return True

with LookingGlass() as what:
    print("Alice, Kitty and Snowdrop")
    print(what)


