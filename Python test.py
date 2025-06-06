# 1. Inheritance

# class Shape:
#     def area(self):
#         pass
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
    
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14*self.radius*self.radius
    
#     def perimeter(self):
#         return 2*3.14*self.radius
    
# rectangle = Rectangle(12,4)
# circle = Circle(14)

# print("Area of Rectangle:",rectangle.area())
# print("Perimeter of Rectangle:",rectangle.perimeter())

# print("Area of Circle:",circle.area())
# print("Perimeter of Circle:",circle.perimeter())

# 2. Polymorphism

# class Animal:
#     def make_sound(self):
#         return "Animal makes sound"
    
# class Dog(Animal):
#     def make_sound(self):
#         return "Dog says Woof!"
    
# class Cat(Animal):
#     def make_sound(self):
#         return "Cat says Meow!"
    
# class Bird(Animal):
#     def make_sound(self):
#         return "Bird says Chirp"
    
# dog = Dog()
# cat = Cat()
# bird = Bird()

# print(dog.make_sound())
# print(cat.make_sound())
# print(bird.make_sound())

# 3. Class and Object Basics

# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
        
# hyundai = Car("Hyundai","Verna",2006)

# print(hyundai.make)
# print(hyundai.model)
# print(hyundai.year)

# 4. Encapsulation

# class BankAccount():
#     def __init__(self,account_number,initial_balance = 0):
#         self._account_number = account_number
#         self.__balance = initial_balance
#         self.__transaction_history = []
        
#     def deposit(self,amount):
#         if amount>0:
#          self.__balance+=amount
#          self.__transaction_history.append(("Deposit",amount))
         
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#             self.__transaction_history.append(("Withdraw",amount))
#         else:
#             print("Insufficient Funds")
    
#     def get_balance(self):
#         return self.__balance
    
#     def get_transaction_history(self):
#         return self.__transaction_history
    
# account = BankAccount("12345678",5000)

# account.deposit(2000)
# account.withdraw(3000)
# account.deposit(4000)
# account.withdraw(5000)

# print("Current Balance:",account.get_balance())
# print("Transaction History:",account.get_transaction_history())

# 5. Abstraction

# from abc import ABC,abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
    
#     @abstractmethod
#     def stop(self):
#         pass
    
# class Car(Vehicle):
#     def start(self):
#         return 'Car starts with the key'
    
#     def stop(self):
#         return 'Car also stops with the key'
    
# class Motorcylce(Vehicle):
#     def start(self):
#         return "Motorcycle starts with a kick"
    
#     def stop(self):
#         return "Motorcycle stops with the key"
    
# car = Car()
# bike = Motorcylce()

# print(car.start())
# print(car.stop())

# print(bike.start())
# print(bike.stop())

# 6. Composition 

# class Engine:
#     def __init__(self,horsepower,fuel_type):
#         self.horsepower = horsepower
#         self.fuel_type = fuel_type
        
#     def start(self):
#         print("Engine started.")
        
#     def stop(self):
#         print("Engine stopped.")
        
# class Car:
#     def __init__(self,make,model,year,horsepower,fuel_type):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.engine = Engine(horsepower,fuel_type)
        
#     def start(self):
#         print(f"Starting {self.make} {self.model} {self.year}")
#         self.engine.start()
        
#     def stop(self):
#         print(f"Stopping {self.make} {self.model} {self.year}")
#         self.engine.stop()
        
# my_car = Car("Nissan","Micra","2018",57,"Petrol")

# my_car.start()
# my_car.stop()

# 7. Static and Class Methods

# class MathsUtils:
#     @staticmethod
#     def add(x,y):
#         return x + y
    
#     @staticmethod
#     def sub(x,y):
#         return x - y
    
#     @staticmethod
#     def mul(x,y):
#         return x*y
    
#     @staticmethod
#     def div(x,y):
#         if y==0:
#             raise ValueError("Cannot divide by Zero")
#         return x/y
    
#     @classmethod
#     def factorial(cls,n):
#         if n<0:
#             raise ValueError("Factorial of a number cannot be negative.")
#         result = 1
#         for i in range(1,n+1):
#             result*=i
#         return result
    
# print("Addition:",MathsUtils.add(222,1523))
# print("Subtraction:",MathsUtils.sub(445,212))
# print("Multiplication:",MathsUtils.mul(44,22))
# print("Division",MathsUtils.div(445,12))
# print("Factorial:",MathsUtils.factorial(9))
                    
# 8. Method Overloading

# class Calculator:
#     def add(self,*args):
#         if len(args) == 2:
#             return self.add_two_nos(*args)
#         elif len(args) ==3:
#             return self.add_three_nos(*args)
#         elif len(args) >3:
#             return self.add_list_of_nos(*args)
#         else:
#             raise ValueError("There should be atleast two numbers")
        
#     def add_two_nos(self,x,y):
#         return x + y
    
#     def add_three_nos(self,x,y,z):
#         return x + y + z
    
#     def add_list_of_nos(self,*args):
#         return sum(args)
    
# calculator = Calculator()

# print("Addition of two numbers:",calculator.add_two_nos(22,44))
# print("Addition of three numbers:",calculator.add_three_nos(44,121,267))
# print("Addition of the list of numbers:",calculator.add_list_of_nos(11,55,99,12,17,18,88))

# 9 . Operator overloading

# class Vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
#     def __add__(self,other):
#         return (self.x + other.x , self.y + other.y)
    
# v1 = Vector(11,22)
# v2 = Vector(21,31)

# v3 = v1 + v2
# print(v3)

# 10 . Exception Handling

class BankAccount:
    def __init__(self,account_number,initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
        
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
        else:
            raise ValueError("Deposit amount must be positive.")
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            raise ValueError("Insufficient funds to withdraw {}.".format(amount))
        
    def check_balance(self):
        return self.balance
    
account = BankAccount("1234567",5000)
print("Initial Balance:",account.check_balance())

try:
    account.withdraw(6000)
except ValueError as e:
    print("Error",e)
    
print("Current Balance",account.check_balance())