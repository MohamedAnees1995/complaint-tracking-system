# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
    
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
    
# def make_sound(animal):
#     return animal.speak()

# dog = Dog()
# cat = Cat()

# print(make_sound(dog))
# print(make_sound(cat))

# Function Polymorphism

# def add(x,y):
#     return x + y

# print(add(20,40))
# print(add("Hello","World"))

# Polymorphism with abstract base classes (ABCs)

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
        
#     def area(self):
#         return self.length*self.width
    
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14*self.radius*self.radius
    
# #Using polymorphism

# shapes = [Rectangle(5,4), Circle(10)]
# for shape in shapes:
#     print("Area:",shape.area())

# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
        
#     def area(self):
#         return self.length*self.width
    
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14*self.radius*self.radius
    
# rectangle = Rectangle(21,22)

# circle = Circle(8) 
            
# print("Area of a Rectangle:",rectangle.area())

# print("Area of a Circle:",circle.area())


# class Animal:
#     def sound(self):
#         print("Generic Animal Sound") 
        
# class Dog(Animal):
#     def sound(self):
#         print("Dog Barks!")
        
# class Cat(Animal):
#     def sound(self):
#         print("Cat Meows!")

# animal = Animal()
# dog = Dog()
# cat = Cat()    
            
# animal.sound()
# dog.sound()
# cat.sound()

# In this example we have different object animal,dog and cat and we have same method which responds in different ways.

# Duck Typing :It is a concept in programming languages like Python where the type or class of an object is determined by its behavior rather than its explicit type or inheritance hierarchy. 

# class Duck:
#     def quack(self):
#         print("Quack , quack!")
        
# class Person:
#     def quack(self):
#         print("I'm quacking like a duck!")
        
# #Function that accepts any object with quack method.

# def make_quack(obj):
#     obj.quack()
    
# duck = Duck()
# person = Person()

# make_quack(duck)
# make_quack(person)

# Operator overloading is a feature in Python (and many other object-oriented programming languages) that allows operators such as +, -, *, /, ==, !=, >, <, etc., to be redefined for user-defined classes.

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self,other):
        return Point(self.x + other.x,self.y + other.y)
    
    def __sub__(self,other):
        return Point(self.x - other.x,self.y - other.y)
    
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
p1 = Point(1,2)
p2 = Point(3,4)

result_addition = p1 + p2
print("Addition Result:",result_addition)

result_subtraction = p1 - p2
print("Subtraction Result:",result_subtraction)

print("Equality Check:", p1 == p2)  # Output: False

print(p1,p2)

class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        
    def __add__(self,other):
        return Point(self.x + other.x,self.y+other.y)
    
    def __sub__(self,other):
         return Point(self.x - other.x,self.y - other.y)
     
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"{self.x},{self.y}"
    
p1 = Point(5,10)
p2 = Point(5,12)

result_addition = p1 + p2 
print("Addition:",result_addition)

result_subtraction = p1 - p2
print("Subtraction:",result_subtraction)

print("Equality check:",p1 == p2)

print("The two points are",p1,p2)
        
# In essence, overloading is about providing different versions of a method within a single class, while overriding is about specializing the behavior of a method inherited from a parent class.     
        