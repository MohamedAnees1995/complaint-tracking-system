# # OOPS is a way to write a program
# # In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming

# # class Car:
# #     def __init__(self, brand, model):  # Here we initialize the attributes of the class when an object is created
# #         self.brand = brand  # These are the different attributes of the class
# #         self.model = model  # self is used to access attributes(variables) and methods(functions) of the object.
# #         self.speed = 0      # We initialize the speed to 0
    
# #     def accelerate(self, increase):  # These functions are additional methods of the car 
# #         self.speed += increase
    
# #     def brake(self, decrease): 
# #         self.speed -= decrease
    
# #     def honk(self):
# #         return "Beep! Beep!"
    
# # car1 = Car("Toyota","Camry")  # Creating a car object 
# # car2 = Car("Ford","Mustang")

# # car1.accelerate(40)
# # print("Speed of the Toyota Camry:",car1.speed,"Km/hr")

# # car2.accelerate(50)
# # print("Speed of the Ford Mustang:",car2.speed,"Km/hr")

# # my_car.accelerate(30) # Accelerating the car
# # print("Current speed of the car :",my_car.speed) 

# # my_car.brake(10) # Decreasing the speed by 10
# # print("Current speed of the car :",my_car.speed) 

# # print(my_car.honk())
   
# # __init__ me ham structural behavior define karte jo har ek object ka us class me common hoga
   
# # aur methods usme use karke uske andar ke functions ko ham define kar sakte hai
    
    
# # class Employee:
# #     def __init__(self,name,id,age):
# #         self.name = name
# #         self.id = id
# #         self.age = age
        
# # person = Employee("Anees","119919",28)
# # print("The name of the person is  :",person.name)    
# # print("The id of the person is :",person.id)
# # print(f"The age of {person.name} is: {person.age}")

# class DMO:
#     def __init__(self,tamername,digimonname):
#         self.tamername = tamername
#         self.digimonname = digimonname 
      
        
#     def level(self, level_value):
#         return level_value
        
# player1=DMO("MohamedAnees","AlSuhulia")

# print(f"The player {player1.tamername} has {player1.digimonname} as his digimon and has High level : {player1.level(140)}")

# class Rectangle:
#      def __init__(self,length,width):
#          self.length = length
#          self.width = width
         
#      def Area(self):
#          return self.length*self.width
     
#      def Perimeter(self):
#          return 2*(self.length + self.width)

# rectangle1 = Rectangle(10,20)

# print("Area of a Rectangle is :", rectangle1.Area()) # Use parenthesis when u call function
# print("Perimeter of a Rectangle is :", rectangle1.Perimeter())
    
# class Student:
#      def __init__(self,name,age,grade,hobby):
#          self.name = name
#          self.age = age
#          self.grade = grade
#          self.hobby = hobby
         
#      def display_info(self):
#          return f"Name :{self.name},Age :{self.age},Grade :{self.grade},Hobby :{self.hobby}"
     
# student1 = Student("Suhaib",24,"B","Cricket")
# student2 = Student("Saad",20,"C","Football")
# student3 = Student("Mayank",25,"D","Cricket")

# print(student1.display_info())
# print(student2.display_info())
# print(student3.display_info())

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.account_number = account_number
#         self.balance = balance
        
#     def deposit(self,amount):
#         self.balance+=amount
        
#     def withdraw(self,amount):
#         if amount<=self.balance:  # If Balance is greater than or equal to amount.
#             self.balance-=amount   # Then withdraw the amount from the balance.
#         else:
#             print('Insufficient Balance.')
            
# account1 = BankAccount("12345678",1000)

# account1.deposit(2000)
# print("Balance after deposit :" , account1.balance )

# account1.withdraw(2000)
# print("Balance after withdrawal",account1.balance)

# class Calculator:
#     def __init__(self,name,model,number):
#         self.name = name
#         self.model = model
#         self.number = number
        
#     def add(self,num):
#         self.number+=num
    
#     def subtract(self,num):
#         self.number-=num
    
#     def multiply(self,num):
#         self.number*=num 
        
#     def divide(self,num):
#         if num!=0:
#             self.number/=num
#         else:
#             print("Error:Cannot divide by Zero")
            
# my_calculator = Calculator("Casio","Basic",199)

# my_calculator.add(550)
# print("Result after adding these numbers:",my_calculator.number)    # Addition

# my_calculator.subtract(222)
# print("Result after subtracting these numbers:",my_calculator.number) # Subtraction

# my_calculator.multiply(12)
# print("Result after multiplying these numbers:",my_calculator.number) # Multiplication

# my_calculator.divide(189)                   
# print("Result after dividing these numbers:",my_calculator.number)  # Division

#Instance attributes are bound to the instance of a class
#Class attributes are bound to the class itself rather than the instance of the class

# class Dog:
#     species = "labrador"
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
# dog1 = Dog("Tommy",5)
# dog2 = Dog("Jimmy",4)

# print("The species of Dog1 is:",dog1.species)
# print("The species of Dog2 is:",dog2.species)

# Dog.species = "Poodle"

# print('The species of Dog1 after modification:',dog1.species)
# print('The species of Dog2 after modification:',dog2.species)                 

# class Circle:
#     pi = 3.14          #Static attribute
    
#     def __init__(self,radius):
#         self.radius = radius
        
#     def area(self):
#         return Circle.pi*(self.radius**2)
    
#     def circum(self):
#         return 2*Circle.pi*(self.radius)
    
    

    
# circle1 = Circle(5)
# print("Area of circle 1 is:",circle1.area())
# print("The circumference of circle 1 is:",circle1.circum())

# circle2 = Circle(10)
# print("Area of cirlce 2 is:",circle2.area())
# print("The circumference of circle 2 is:",circle2.circum())

# circle1.radius = 22        
        
# print("Area of circle 1 after modification is:",circle1.area()) 
# print("The circumference of circle 1 is:",circle1.circum())

# circle2.radius = 12

# print("Area of circle 2 after modification is:",circle2.area()) 
# print("The circumference of circle 2 is:",circle2.circum())  

# Methods in class 

# # 1. Instance Methods : '''Instance methods are defined within a class and are intended to be called on instances of the class.
# They typically take the self parameter as the first argument, which refers to the instance on which the method is called.
# Instance methods can access and modify instance attributes.'''

# 2. Class Methods : Class methods are defined using the @classmethod decorator and are intended to be called on the class itself.
# 3. Static Methods : Static methods are defined using the @staticmethod decorator and are not bound to the class or its instances.         

#Decorator function : They are powerful features that allows us to modify or extend the behavior of the function or method without modifying its code.
#Decorator function takes another function as input and return a new function with extended or modified behaviour.

#Instance method example

# class Myclass:
#     def __init__(self,value):
#         self.value = value
        
#     def instance_method(self):
#         return f"Instance method called with value : {self.value}"
    
# obj = Myclass(22)

# print(obj.instance_method())
        
#Class method example   

# class Myclass:
#     class_attribute = "Class attribute"
    
#     @classmethod
#     def class_method(cls):
#         return f'Class method called with value :{cls.class_attribute}'
    
# print(Myclass.class_method())
        
#Static method example 

# class Myclass:
#     @staticmethod
#     def static_method(value):
#         return f"Static method called with value :{value}"
    
# print(Myclass.static_method(20))        

# class Myclass:
#     @staticmethod
#     def static_method(value):
#         return f"Static method called with value: {value}"
    
# print(Myclass.static_method(22))

# Decorator function example 

# def log_function(func):
#     def wrapper(*args,**kwargs):
#         print(f'Calling {func.__name__} with args:{args},kwargs:{kwargs}')
        
#         result = func(*args,*kwargs)
        
#         print(f'{func.__name__} returned:{result}')
        
#         return result
#     return wrapper

# @log_function
# def add(a,b):
#     return a+b

# result = add(3,5)
# print("Result",result)

# Constructor and its methods

# Constructors are implemented using special methods called __init__ method.
#Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. 

#These methods are automatically created when new instance of a class is created.

# Default Constructor : Python provides a default constructor that doesn't take any parameters. It initializes the object with default values.

# Default Constructor Example 

# class Myclass:
#     def __init__(self): # default constructor 
#         self.my_var = 0
        
# obj = Myclass()

# # Parameterized Constructor : This constructor takes one or more parameters to initialize the object with specific values.
# # You can define a constructor that takes parameters to initialize the object with specific values.

# class Myclass:
#     def __init__(self,initial_value):
#         self.my_var = initial_value
        
# obj = Myclass()

# #Constructor Overloading : Constructors can be overloaded, meaning you can define multiple constructors within a class, as long as they have different parameter lists.

# class Myclass:
#     def __init__(self,value1=0,value2=0):
#         self.var1 =value1
#         self.var2=value2
        
# # Constructor overloading using default parameter values        

# # Creating objects of MyClass with different number of parameters

# obj1 = Myclass()                           # Uses default values for both parameters
# obj2 = Myclass(10)                         # Sets value1 to 10, uses default for value2
# obj3 = Myclass(10,20)                      # Sets both value1 and value2

#Copy Constructor: This constructor initializes an object as a copy of another object of the same class.

class Myclass:
    def __init__(self,value):
        self.value = value
    
    def copy(self):
        return Myclass(self.value)
    
obj1 = Myclass(100)

obj2 = obj1.copy()

obj1.value = 88

print("Object1 value :",obj1.value)

print("Object2 value :",obj2.value)
            
#Inheritance : Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or subclass) to inherit attributes and methods from another class.

#Inheritance example

# class Animal:
#     def __init__(self,name):
#         self.name = name
        
#     def speak(self):
#         raise NotImplementedError("Subclasses must implement this method")
    
# class Dog(Animal):
#     def speak(self):
#         return f'{self.name} says Bow!'
    
# class Cat(Animal):
#     def speak(self):
#         return f'{self.name} says Meow'
    
# dog = Dog("Jammy")
# cat = Cat("Timothy")

# print(dog.speak())
# print(cat.speak())
        
#Polymorphism : Polymorphism is another key concept in object-oriented programming (OOP), which allows objects of different classes to be treated as objects of a common superclass.

# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclasses must implement this method")
    
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
    
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
    
# def make_sound(animal):              # Function to demonstrate polymorphism
#     return animal.speak()
    
    
# dog1 = Dog()
# cat1 = Cat()
        
# print(make_sound(dog1))
# print(make_sound(cat1))
        
# Abstraction : Abstraction is a concept in object-oriented programming that involves hiding the complex implementation details and showing only the essential features of an object.

# from abc import ABC, abstractmethod

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
    

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14*self.radius*self.radius
    
#     def perimeter(self):
#         return 2*3.14*self.radius
    
# rectangle = Rectangle(10,20)
# circle = Circle(6)    

# print("Rectangle Area:",rectangle.area())
# print("Rectange perimeter:",rectangle.perimeter())

# print("Circle Area:",circle.area())
# print('Circle perimeter:',circle.perimeter())

#Encapsulation : It involves bundling the data (attributes) and methods (functions) that operate on the data into a single unit, typically referred to as a class.
# The key idea behind encapsulation is to hide the internal state of an object and only expose a controlled interface to interact with it.

# class Car:
#     def __init__(self, make, model, year):
#         self._make = make   # Using underscore to indicate it's a protected attribute
#         self._model = model
#         self._year = year
#         self._odometer_reading = 0   # Encapsulated attribute
        
#     def get_make(self):
#         return self._make
    
#     def get_model(self):
#         return self._model
    
#     def get_year(self):
#         return self._year
    
#     def get_odometer_reading(self):
#         return self._odometer_reading
    
#     def update_odometer(self,mileage):
#         if mileage>=self._odometer_reading:
#             self._odometer_reading = mileage
#         else:
#             print("You can't rollback an odometer")
    
#     def increment_odometer(self,miles):
#         self._odometer_reading+=miles
        
# my_car = Car("Toyota","Camry",2022)

# print("Make:",my_car.get_make())
# print("Model:",my_car.get_model())
# print("Year:",my_car.get_year())

# print("Odometer reading:",my_car.get_odometer_reading())

# my_car.update_odometer(100)
# print("Updated Odometer reading:",my_car.get_odometer_reading())

# my_car.increment_odometer(50)
# print("Incremented Odometer reading:",my_car.get_odometer_reading())

# class BankAccount():
#     def __init__(self,account_number,balance):
#         self._account_number = account_number
#         self._balance = balance
        
#     def get_account_number(self):
#         return self._account_number
    
#     def get_balance(self):
#         return self._balance
    
#     def deposit(self,amount):
#         if amount>0:
#             self._balance+=amount
#             print(f'Deposited ${amount}. New balance is {self._balance}')
#         else:
#             print("Invalid Deposit Amount")
            
#     def withdraw(self,amount):
#         if 0<amount<=self._balance:
#             self._balance-=amount
#             print(f'Withdrew ${amount}. New balance is {self._balance}')
#         else:
#             print("Insufficient funds or invalid withdrawal amount") 
               
# my_account = BankAccount("123456789",1000)   

# print("Account Number:",my_account.get_account_number())
# print("Current Balance:", my_account.get_balance())     

# my_account.deposit(500)
# my_account.withdraw(200)

# my_account.withdraw(1500) #Attempting to withdraw more than balance.

# class Student:
#     def __init__(self,name,age,roll_number):
#         self._name = name
#         self._age = age
#         self._roll_number = roll_number
#         self._grades = {}
    
#     def get_name(self):
#         return self._name
    
#     def get_age(self):
#         return self._age
    
#     def get_roll_number(self):
#         return self._roll_number
    
#     def set_grade(self,subject,grade):
#         if 0<=grade<=100:
#             self._grades[subject] = grade
#             print(f"Grade for {subject} set to {grade} for {self._name}.")
#         else:
#             print("Invalid grade.")

#     def get_grade(self,subject):
#         return self._grades.get(subject,"Grade not available for this subject.")    
    
    
# student1 = Student("Alice",18,"S001")

# print("Student Name:", student1.get_name())
# print("Student Age:",student1.get_age())
# print("Student Roll Number:",student1.get_roll_number())

# student1.set_grade("Math",90)
# student1.set_grade("Science",85)
# student1.set_grade("History",100)

# print("Math Grade:",student1.get_grade("Math"))
# print("Science Grade:",student1.get_grade("Science"))
# print("History Grade:",student1.get_grade("History"))

# class Student:
#     def __init__(self,name,age,roll_number):
#         self._name = name
#         self._age = age
#         self._roll_number = roll_number
#         self._grades = {}
        
#     def get_name(self):
#         return self._name
    
#     def get_age(self):
#         return self._age
    
#     def get_roll_number(self):
#         return self._roll_number
    
#     def set_grade(self,subject,grade):
#         if 0<=grade<=100:
#             self._grades[subject] = grade
#             print(f'Grade for {subject} set to {grade} for {self._name}')
#         else:
#             print("Invalid grade")
            
#     def get_grade(self,subject):
#         return self._grades.get(subject,"Grade not available for this subject")
    

# student1 = Student("Saad",17,"S001")

# print("Student Name:",student1.get_name())
# print("Student Age:",student1.get_age())
# print("Student Roll Number",student1.get_roll_number())

# student1.set_grade("Math",90)
# student1.set_grade("Science",80)

# print("Math grade:",student1.get_grade("Math"))
# print("Science grade:",student1.get_grade("Science"))
# print("History grade:",student1.get_grade("History"))

# class Person:
#     def __init__(self,name,age,email):
#         self._name = name
#         self._age = age
#         self._email = email
#         self._is_verified = False
        
#     def get_name(self):
#         return self._name
    
#     def get_age(self):
#         return self._age
    
#     def get_email(self):
#         return self._email
    
#     def verify_email(self):
#         self._is_verified = True
#         print(f'Email for {self._name} has been verified.')
        
#     def is_email_verified(self):
#         return self._is_verified
    
# person1 = Person("Mike",35,"mike123@example.com")

# print("Person name :",person1.get_name())
# print("Person age :",person1.get_age())
# print("Person email :",person1.get_email())

# print("Is Email Verified?",person1.is_email_verified())

# person1.verify_email()

# print("Is Email Verified?",person1.is_email_verified())

# class Product:
#     def __init__(self,name,price,quantity):
#         self._name = name
#         self._price = price
#         self._quantity = quantity
        
#     def get_name(self):
#         return self._name 
    
#     def get_price(self):
#         return self._price
    
#     def get_quantity(self):
#         return self._quantity
    
#     def update_price(self,new_price):
#         if new_price>=0:
#             self._price = new_price
#             print(f'Price updated for {self._name}. New price : ${self._price}')
#         else:
#             print("Invalid price.")
        
#     def update_quantity(self,new_quantity):
#         if new_quantity>=0:
#             self._quantity=new_quantity
#             print(f'Quantity updated for {self._name}. New quantity : {self._quantity}')
#         else:
#             print("Invalid quantity.")
            
# product1 = Product("Laptop",1200,10)

# print("Product Name :",product1.get_name())
# print("Product Price :",product1.get_price())
# print("Product Quantity:",product1.get_quantity())

# product1.update_price(1300)
# product1.update_quantity(15)        

