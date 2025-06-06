# # # class Language:
# # #     def say_hello(self):
# # #         raise NotImplementedError("Please use say_hello in child class")

# # # class French(Language):
# # #     def say_hello(self):
# # #         print("Bonjour")
            
# # # class Chinese(Language):
# # #     def say_hello(self):
# # #         print("你好")
        
# # # def intro(lang):
# # #     lang.say_hello()
    
# # # Sarthak = French()
# # # John = Chinese()

# # # intro(Sarthak)
# # # intro(John)

# # # class A:
# # #     def method(self):
# # #         print("A method")
        
# # # class B(A):
# # #     def method(self):
# # #         print("B method")
# # #         super().method()
        
# # # class C(A):
# # #     def method(self):
# # #         print("C method")
# # #         super().method()
        
# # # class D(B,C):
# # #     pass

# # # obj = D()
# # # obj.method()
        
# # class Vehicle:
# #     def drive(self):
# #         print("Vehicle is being driven")
        
# # class Car(Vehicle):
# #     def drive(self):
# #         print("Car is on the road")

# # class Motorcycle(Vehicle):
# #     def drive(self):
# #         print("Motorcycle is cruising")
        
# # car = Car()
# # motorcycle = Motorcycle()

# # car.drive()
# # motorcycle.drive()

# # from abc import ABC,abstractmethod
# # import math

# # class Shape(ABC):
# #     @abstractmethod
# #     def calculate_area(self):
# #         pass

# # class Rectangle(Shape):
# #     def __init__(self,length,width):
# #         self.length = length
# #         self.width = width
        
# #     def calculate_area(self):
# #         return self.length*self.width

# # class Circle(Shape):
# #     def __init__(self,radius):
# #         self.radius = radius
        
# #     def calculate_area(self):
# #         return math.pi*(self.radius*self.radius)
    
# # rectangle = Rectangle(22,21)
# # circle = Circle(6)

# # print("Area of Rectangle:",rectangle.calculate_area())
# # print("Area of Circle:",circle.calculate_area())

# # def print_info(obj):
# #     print(obj.info())
    
# # class Dog:
# #     def info(self):
# #         return "I am a Dog"
    
# # class Cat:
# #     def info(self):
# #         return "I am a Cat"
    
# # dog = Dog()
# # cat = Cat()


# # print_info(dog)    
# # print_info(cat)


# # class BankAccount:
# #     def __init__(self,account_number,initial_balance =0):
# #         self._account_number = account_number
# #         self.__balance = initial_balance
# #         self.__transaction_history = []
        
# #     def deposit(self,amount):
# #         self.__balance +=amount
# #         self.__transaction_history.append(("Deposit",amount))
        
# #     def withdraw(self,amount):
# #         if amount<=self.__balance:
# #             self.__balance-=amount
# #             self.__transaction_history.append(("Withdraw",amount))
# #         else:
# #             print("Insufficient Funds")
            
# #     def get_balance(self):
# #         return self.__balance
    
# #     def get_transaction_history(self):
# #         return self.__transaction_history
    
# # account = BankAccount("12345678",20000)

# # account.deposit(50000)
# # account.withdraw(35000)
# # account.deposit(90000)
# # account.withdraw(120000)

# # print(account.get_balance())
# # print(account.get_transaction_history())        

# # from abc import ABC,abstractmethod

# # class Shape(ABC):
# #     @abstractmethod
# #     def area(self):
# #         pass
# #     @abstractmethod
# #     def perimeter(self):
# #         pass

# # class Square(Shape):
# #     def __init__(self,side):
# #         self.side = side
        
# #     def area(self):
# #         return self.side*self.side
    
# #     def perimeter(self):
# #         return 4*self.side

# # class Rectangle(Shape):
# #     def __init__(self,length,breadth):
# #         self.length = length
# #         self.breadth = breadth
        
# #     def area(self):
# #         return self.length*self.breadth
    
# #     def perimeter(self):
# #         return 2*(self.length + self.breadth)
    
# # class Circle(Shape):
# #     def __init__(self,radius):
# #         self.radius = radius
        
# #     def area(self):
# #         return 3.14*self.radius*self.radius
    
# #     def perimeter(self):
# #         return 2*3.14*self.radius

# # square = Square(23)
# # rectangle = Rectangle(12,23)
# # circle = Circle(19)

# # print("Area of Square:",square.area())
# # print("Perimeter of a Square:",square.perimeter())

# # print("Area of a Rectangle:",rectangle.area())
# # print("Perimeter of a Rectangle:",rectangle.perimeter())

# # print("Area of a Circle:",circle.area())
# # print("Perimeter of a Circle:",circle.perimeter())

# class Vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
    
#     def __add__(self,other):
#         return Vector(self.x + other.x, self.y + other.y)
    
# v1 = Vector(22,34)
# v2 = Vector(13,45)

# result = v1 + v2

# print(f"The addition of two vectors is:",({result.x},{result.y}))

# Duck-typing example with a custom context manager
# class MyContextManager:
#     def __enter__(self):
#         print("Entering context")
#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting context")

# # Using MyContextManager as a context manager
# with MyContextManager():
#     print("Inside context")

    
# class MyContextManager():
#     def __enter__(self):
#         print("Entering context")
    
#     def __exit__(self,exc_type,exc_value,traceback):
#         print("Exiting context")
        
# with MyContextManager():
#     print("Inside context")
        

def main():
    
    name = input("Enter your name:")
    
    age = input("Enter your age:")
    
    if age.isdigit():
        age = int(age)
        if age<0:
            print("Enter a valid age")
        else:
            print(f"Hello,{name}!")
            if age<18:
                print("You are under 18 years old")
            elif age>= 18 and age<65:
                print("You are an adult")
            else:
                print("You are a senior citizen")
    else:
        print("Ener a valid age")
        
if __name__=="__main__":
    main()
                    
            
             

        


        
    
            

            
        