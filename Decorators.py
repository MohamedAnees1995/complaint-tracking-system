'''Decorators are functions that takes another function as input and return 
 a new function with extended or modified behaviour.'''
 
# Step 1: Basic Function

# def add(a,b):
#     return a + b

# result = add(3,4)
# print(result)

# Step 2: Writing a Decorator Function

# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print("Before calling the function")
#         result = func(*args,**kwargs)
#         print("After calling the function")
#         return result
#     return wrapper

# @my_decorator
# def add(a,b):
#     return a+b

# result = add(3,4)
# print(result)


# def custom_decorator(division):
#     def inner_func(a,b):
#         if b>a:
#             a,b=b,a
#         return division(a,b)
#     return inner_func


# @custom_decorator
# def division(a,b):
#     return a/b
# x1=division(5,2)
# x2=division(2,5)
# print(x1)
# print(x2)

# def custom_decorator(add):
#     def inner_func(a,b):
#         if b>a:
#             a=b
#         return add(a,b)
#     return inner_func
    

# @custom_decorator
# def add(a,b):
#     return a + b

# x1 = add(2,3)
# x2 = add(4,5)
# print(x1)
# print(x2)

# def make_pretty(func):
#     def inner_func():
#         print("I am decorated")
#         func()
#     return inner_func

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary()

# def smart_divide(func):
#     def inner(x,y):
#         print("I am going to divide",x,"and",y)
#         if y==0:
#             print("Whoops!!Cannot divide by Zero")
#             return
#         return func(x,y)
#     return inner
        
# @smart_divide
# def divide(x,y):
#     print(x/y)

# divide(22,0)
# divide(31,3)
        

# def star(func):
#     def inner(*args,**kwargs):
#         print("*"*15)
#         func(*args,**kwargs)
#         print("*"*15)
#     return inner

# def percent(func):
#     def inner(*args,**kwargs):
#         print("%"*15)
#         func(*args,**kwargs)
#         print("%"*15)
#     return inner

# @percent
# @star
# def printer(msg):
#     print(msg)
    
# printer("Hello")
        
# Timer Decorator

# import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         result = func(*args,**kwargs)
#         end_time = time.time()
#         print(f"The execution time of {func.__name__} : {end_time} - {start_time}")
#         return result
#     return wrapper

# @timer
# def some_function():
#     pass

# some_function()  
        
#Logger decorator

# def logger(func):
#     def wrapper(*args,**kwargs):
#         print(f"Calling function :{func.__name__}")
#         print(f"Arguments: {args},{kwargs}")
#         result = func(*args,**kwargs)
#         print(f"Return value = {result}")
#         return result
#     return wrapper

# @logger
# def some_function(x,y):
#     return x + y

# some_function(12,22)

# Authorization decorator

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called")
#         func()
#         print("Something is happening after the function is called")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")
    
# say_hello()

#Class decorator

# def add_attribute(cls):
#     class Newclass(cls):
#         new_attribute = "Added attribute"
#     return Newclass

# @add_attribute
# class Myclass:
#     attribute = "Original attribute"
    
# obj = Myclass()

# print(obj.attribute)
# print(obj.new_attribute)

# Decorator with arguments

# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(*args,**kwargs):
#             for _ in range(num_times):
#                 result = func(*args,**kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello {name}")

# greet("Alice")    

# Built in decorators

# class Myclass:
#     def __init__(self,x):
#         self.x = x
        
#     @staticmethod
#     def static_method():
#         print("I am a static method.")
        
#     @classmethod
#     def class_method(cls):
#         print(f"I am a class method. {cls}")
        
#     @property
#     def value(self):
#         return self.x  

# obj = Myclass(12)

# obj.static_method()
# obj.class_method()

# print(obj.value)

# Decorator stacking

# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper

# def exclamation(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result + "!"
#         return modified_result
#     return wrapper

# @exclamation
# @uppercase

# def greet():
#     return "Hello"

# print(greet())

# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(*args,**kwargs):
#             for _ in range(num_times):
#                 result = func(*args,**kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello {name}")

# greet("Alice")

# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper

# def exclamation(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result + "!"
#         return modified_result
#     return wrapper

# @uppercase
# @exclamation
# def greet():
#     return "Hey whatsup"
    
# print(greet())

# class BankAccount:
#     def __init__(self,account_number,initial_balance=0):
#         self._account_number = account_number
#         self.__balance = initial_balance
#         self.__transaction_history = []
        
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             self.__transaction_history.append(("Deposit",amount))
#         else:
#             print("Invalid amount")
            
#     def withdraw(self,amount):
#         if amount<=self.__balance:
#             self.__balance-=amount
#             self.__transaction_history.append(("Withdraw",amount))
#         else:
#             print("Insufficient funds")
            
#     def get_balance(self):
#         return self.__balance
    
#     def get_transaction_history(self):
#         return self.__transaction_history
    
# account = BankAccount("44991122",5000)

# account.deposit(4000)
# account.withdraw(5000)
# account.withdraw(5000)

# print(account.get_balance())
# print(account.get_transaction_history())
            
# def plus_one(number):
#     return number + 1

# add_one = plus_one
# print(add_one(5))

# def plus_one(number):
#     def add_one(number):
#         return number + 1
    
#     result = add_one(number)
#     return result

# print(plus_one(5))
    
# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi

# hello = hello_function()
# print(hello())
        
# Here hello_function is wrapped by function say_hi so it works as say_hi function along with its own functions.

# def upper(function):
#     def mod():
#         original_function = function()
#         modified_function = original_function.upper()
#         return modified_function
#     return mod


# @upper
# def words():
#     return f"hello bob"

# print(words())

# Basic syntax for python decorators

# def my_decorator_func(func):
#     def wrapper_func():
#          # Do something before the function.
#          func()
#          # Do something after the function.
#     return wrapper_func
    
# from abc import ABC, abstractmethod

# class Storage(ABC):
#     @abstractmethod
#     def store(self, data):
#         pass
    
#     @abstractmethod
#     def retrieve(self, key):
#         pass

# class FileStorage(Storage):
#     def __init__(self, filename):
#         self.filename = filename

#     def store(self, data):
#         with open(self.filename, 'w') as file:
#             file.write(data)

#     def retrieve(self, key):
#         with open(self.filename, 'r') as file:
#             return file.read()

# class DatabaseStorage(Storage):
#     def __init__(self, connection_string):
#         self.connection_string = connection_string

#     def store(self, data):
#         # Example implementation: connect to database and store data
#         print(f"Storing data '{data}' in database")

#     def retrieve(self, key):
#         # Example implementation: connect to database and retrieve data
#         print(f"Retrieving data for key '{key}' from database")

# # Creating objects of different storage systems
# file_storage = FileStorage('data.txt')
# db_storage = DatabaseStorage('mysql://user:password@localhost/my_database')

# # Using abstraction to store and retrieve data
# file_storage.store("Data stored in a file")
# print("Data retrieved from file:", file_storage.retrieve('data.txt'))

# db_storage.store("Data stored in a database")
# print("Data retrieved from database:", db_storage.retrieve('key'))

# from abc import ABC,abstractmethod

# class Storage(ABC):
#     @abstractmethod
#     def store(self,data):
#         pass
    
#     @abstractmethod
#     def retrieve(self,key):
#         pass
    
# class FileStorage(Storage):
#     def __init__(self,filename):
#         self.filename = filename
        
#     def store(self,data):
#         with open(self.filename,"w") as file:
#             file.write(data)
            
#     def retrieve(self, key):
#         with open(self.filename, "r") as file:
#             file.read()
            
# class DatabaseStorage(Storage):
#     def __init__(self, connection_string):
#         self.connection_string = connection_string
        
#     def store(self,data):
#         print(f'Storing data {data} in the database.')
        
#     def retrieve(self, key):
#         print(f"Retrieving data for key {key} from database.")
        
# file_storage = FileStorage("data.txt") 
# db_storage = DatabaseStorage("mysql://user:password@localhost/my_database")  

# file_storage.store("Data stored in a file")
# print("Data retrieved from file:",file_storage.retrieve("data.text"))

# db_storage.store("Data stored in a database") 
# print("Data retrieved from database:",db_storage.retrieve("key"))
    
 
def add_author(func):
    print("Author : Natalia Tsarkova")
    return func

@add_author
def decorators_article():
    print("Article: Decorators in Python")
    
decorators_article()


# Author : Natalia Tsarkova
# Article : Decorators in Python
           
# def renaissance(func):
#    def wrapper():
#        func()
#        print('Now with masterpieces!')
#    return wrapper

# class history:
#    def init(self):
#        pass
#    @renaissance
#    def whats_going_on():
#        print('As always, something is going on')
# history.whats_going_on()