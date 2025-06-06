Abstract Base Classes (ABCs):

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14*self.radius*self.radius
    
    def perimeter(self):
        return 2*3.14*self.radius
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length + self.width)
    
circle = Circle(12)
rectangle = Rectangle(8,5)

print(circle.area())
print(circle.perimeter())

print(rectangle.area())
print(rectangle.perimeter())
    
#     @abstractmethod
#     def perimeter(self):
#         pass
    
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14*self.radius*self.radius
    
#     def perimeter(self):
#         return 2*3.14*self.radius
    
# class Rectangle(Shape):
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
    
#     def area(self):
#         return self.length*self.breadth
    
#     def perimeter(self):
#         return 2*(self.length + self.breadth)
    
# circle = Circle(22)
# rectangle = Rectangle(44,22)

# print("Area of a circle:",circle.area())
# print("Perimeter of a circle:",circle.perimeter())

# print("Area of a rectangle:",rectangle.area())
# print("Perimeter of a rectangle:",rectangle.perimeter())

# Interface classes

# from abc import ABC,abstractmethod

# class Animal:
    
#     @abstractmethod
#     def speak(self):
#         pass
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
    
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
    
# dog = Dog()
# cat = Cat()

# print("Dog speaks",dog.speak())
# print("Cat speaks",cat.speak())

# 1. Abstract Data Types (ADTs)

# my_list = [1,2,3,4,5]

# my_list.append(6)
# my_list.remove(3)

# print(my_list)

# 2. Classes and Objects 

# class Car:
#     def __init__(self,make,model):
#         self.make = make
#         self.model = model
        
# car = Car("TATA","Nano") # Here wer have created an object of class Car named "car"

# print(car.model)
# print(car.make)

# 3. Encapsulation 

# class Person:
#     def __init__(self,name,age):
#         self._name = name   #Protected attribute
#         self.__age = age    #Private attribute
        
#     def get_age(self):
#         return self.__age
          
#     def get_name(self):
#         return self._name
    
#     def set_name(self,new_name):
#         self._name = new_name
        
#     def set_age(self,new_age):
#         self.__age = new_age    
    
# person = Person("Alice",25)

# print(person.get_name())
# print(person.get_age())

# person.set_name("Rajnikanth")

# person.set_age(65)

# print(person.get_name())
# print(person.get_age())

# 4.Functions and Modules

# def greet(name):
#     return f"Hello {name}!"

# import math

# print(greet("Shavukath Ali"))

# print(math.sqrt(9000))

# 5. Interfaces and Abstract Base Classes (ABCs):

# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length*self.width
    
#     def perimeter(self):
#         return 2*(self.length + self.width)
    
# rectangle = Rectangle(45,20)

# print("Area of the Rectangle is",rectangle.area())
# print("Perimeter of the Rectangle is",rectangle.perimeter())
        
# 6. Generators and Iterators:

# Generator function definition 

# def squares(n):
#     for i in range(n):
#         yield i**2
        
# # # Calling the function

# square_gen = squares(20)

# # # Iterating over the function

# for square in square_gen:
#     print(square)

# def squares(n):
#     for i in range(n):
#         yield i**2

# square_gen = squares(20)

# for square in square_gen:
#     print(square)

# class Duck:
#     def quack(self):
#         print("Quack!")
        
#     def swim(self):
#         print("Swim!")
        
# class Person:
#     def quack(self):
#         print("I can imitate a duck by saying Quack!")
        
#     def swim(self):
#         print("I can swim too!")
        
# def make_it_quack_and_swim(duck_like):
#     duck_like.quack()
#     duck_like.swim()
    
# obj = Duck()
# obj.quack()
# obj.swim()

# obj = Person()
# obj.quack()
# obj.swim()

# numbers = [1,2,3]
# person = ("Jane",25,"Python Dev")
# letters = "abc"
# ordinals = {"one":"first", "two":"second","three":"third"}
# even_digits = {2,4,6,8}
# collections = [numbers,person,letters,ordinals,even_digits]

# for collection in collections:
#     for value in collection:
#         print(value)
        
class Bird:
    def fly(self):
        print("Fly with wings")
        
class Airplane:
    def fly(self):
        print("Fly with fuel")
        
class Fish:
    def swim(self):
        print("Fish swim in the sea")
        
# Attributes having same name are considered as duck typing    

for features in Bird(),Airplane() ,Fish():
    features.fly()
    
    
# class Database:
#     def connect(self):
#         return "Connected to the database"
        
# class MockDatabase:
#     def connect(self):
#         return "Connected to the mock database"
#     def load_fixture(self,fixture):
#         return f'Loaded {fixture} into the mock database'

# def setup_database(db):
#     print(db.connect())
#     if hasattr(db,'load_fixture'):
#         print(db.load_fixture("test_data"))
        
# real_db = Database()
# test_db = MockDatabase()
# setup_database(real_db)
# setup_database(test_db)        
    
# from abc import ABC,abstractmethod

# class Flyer(ABC):
#     @abstractmethod
#     def fly(self):
#         pass
    
# class Bird:
#     def fly(self):
#         return 'Flap flap!'
    
# class Airplane:
#     def fly(self):
#         return 'Zoom zoom!'
    
# class Car:
#     def run(self):
#         return 'Vroom vroom!'
    
# def in_the_sky(flier):
#     if isinstance(flier,(Bird,Airplane,Car)):
#         print(flier.fly())
#     else:
#         raise TypeError("The object does not know how to fly")
    
# pigeon = Bird()
# beoing = Airplane()
# toyota = Car()

# print(pigeon.fly())
# print(beoing.fly())

# in_the_sky(pigeon)
# in_the_sky(beoing)

# in_the_sky(toyota)

# class Duck:
#     def quack(self):
#         return "Quack quack!"

# class Person:
#     def quack(self):
#         return "I can mimic a duck!"

# def in_the_forest(creature):
#     print(creature.quack())

# duck = Duck()

# person = Person() 

# in_the_forest(duck)

# in_the_forest(person)   

# class Duck:
#     def quack(self):
#         return 'Quack!'

# class Dog:
#     def bark(self):
#         return 'Woof!'

# def in_the_forest(creature):
#     print(creature.quack())

# fido = Dog()
# in_the_forest(fido)

# Output:
# AttributeError: 'Dog' object has no attribute 'quack'

# class Duck:
#     def quack(self):
#         return 'Quack!'

# class Dog:
#     def bark(self):
#         return 'Woof!'

# def in_the_forest(creature):
#     if hasattr(creature,"quack"):
#        print(creature.quack())
#     else:
#         print("Creature does not quack")

# fido = Dog()
# in_the_forest(fido)

# Output:
# AttributeError: 'Dog' object has no attribute 'quack'

# class Duck:
#     def quack(self):
#         return "Quack"
    
# class Person:
#     def quack(self):
#         return "I can quack like a duck"
    
# def make_it_quack(creature):
#     return creature.quack()
    
# donald = Duck()
# Rahul = Person()

# print(make_it_quack(donald))
# print(make_it_quack(Rahul))



