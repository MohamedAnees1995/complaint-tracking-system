# import math
# from abc import ABC,abstractmethod

# class Shape(ABC):
    
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Circle(Shape):
    
#     def __init__(self,radius):
#         self.radius = radius
        
#     def area(self):
#         return math.pi*self.radius*self.radius
    
#     def perimeter(self):
#         return 2*math.pi*self.radius
    
# class Rectangle(Shape):
    
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
        
#     def area(self):
#         return self.length*self.width
    
#     def perimeter(self):
#         return 2*(self.length +self.width)
    
# class Triangle(Shape):
    
#     def __init__(self,side1,side2,side3):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
        
#     def area(self):
#         s=(self.side1 + self.side2 + self.side3/3)
#         return math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
    
#     def perimeter(self):
#         return self.side1 + self.side2 + self.side3
    
# triangle = Triangle(6,8,12)
# circle = Circle(15)
# rectangle = Rectangle(12,14)

# print("Area of Triangle:",triangle.area())
# print("Perimeter of Triangle:",triangle.perimeter())

# print("Area of Circle:",circle.area())
# print("Perimeter of Circle:",circle.perimeter())

# print("Area of Triangle:",rectangle.area())
# print("Perimeter of Triangle:",triangle.perimeter())

class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
class Duck:
    def quack(self):
        return "Quack!"
    
def make_animal_speak(animals):
    for animal in animals:
        try:
            print(animal.speak())
        except AttributeError:
            print("This animal doesn't speak")
            
dog = Dog()
cat = Cat()
duck = Duck()

animals = [dog,cat,duck]

make_animal_speak(animals)