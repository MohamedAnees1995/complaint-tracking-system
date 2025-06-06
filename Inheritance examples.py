# Basic Inheritance

# class Animal:
#     def speak(self):
#         print("Animal speaks")
        
# class Dog(Animal):
#     def bark(self):
#         print("Dog Barks")
        
# dog = Dog()

# dog.speak()
# dog.bark()

# Constructor in Inheritance

# class Vehicle:
#     def __init__(self,color):
#         self.color = color
        
# class Car(Vehicle):
#     def __init__(self,brand,color):
#         super().__init__(color)
#         self.brand = brand
        
# car = Car("Toyoto","Red")

# print(car.brand)
# print(car.color)

# Method overriding

# class Animal:
#     def speak(self):
#         print("Animal Speaks")
        
# class Dog(Animal):
#     def speak(self):
#         print("Dog Barks")
        
# dog = Dog()

# dog.speak()

# Multiple Inheritance

# class A:
#     def method_a(self):
#         print("Method A")

# class B:
#     def method_b(self):
#         print("Method B")
        
# class C(A,B):
#     pass

# c = C()

# c.method_a()
# c.method_b()

