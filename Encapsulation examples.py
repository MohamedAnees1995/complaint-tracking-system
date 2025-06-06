#Using Private Attributes and Getter/Setter Methods:

# class Person():
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age
        
#     def get_name(self):
#         return self._name
    
#     def set_name(self,name):
#         self._name = name
    
#     def get_age(self):
#         return self._age
    
#     def set_age(self,age):
#         try:
#             age = int(age)
#             if age >=0:
#                 self._age = age
#             else:
#                 print("Age cannot be negative.")
#         except ValueError:
#             print("Age must be a valid integer")
            
# person = Person("Alice",30)

# print("Name:",person.get_name())
# print("Age:",person.get_age())

# person.set_name("Bob")
# person.set_age(22)
    
# print("Name:",person.get_name())
# print("Age:",person.get_age())

# Using Properties   
    
# class Car:
#     def __init__(self,make,model):
#         self._make = make
#         self._model = model
        
#     @property
#     def make(self):
#         return self._make
    
#     @make.setter
#     def make(self,make):
#         self._make = make
        
#     @property
#     def model(self):
#         return self._model
    
#     @model.setter
#     def model(self,model):
#         self._model = model
        
# car = Car("Toyota","Camry")

# print("Make:",car.make)
# print("Model:",car.model)    

# car.make = "Honda"
# car.model = "Accord"

# print("Make:",car.make)
# print("Model:",car.model)

# 1. Public Encapsulation

# class PublicEncapsulation:
#     def __init__(self):
#         self.public_attribute = "I am a public attribute"
        
#     def public_method(self):
#         return "I am a public method"
    
# obj = PublicEncapsulation()

# print(obj.public_attribute)
# print(obj.public_method())

# 2. Private Encapsulation

# class PrivateEncapsulation:
#     def __init__(self):
#         self.__private_attribute = "I am a private attribute"
        
#     def __private_method(self):
#         return "I am a private method"
    
# obj = PrivateEncapsulation()

#We can still access private members using name mangling

# print(obj._PrivateEncapsulation__private_attribute)
# print(obj._PrivateEncapsulation__private_method())

# 3. Protected Encapsulation:

# class ProtectedEncapsulation:
#     def __init__(self):
#         self._protected_attribute = "I am a protected attribute"
        
#     def _protected_method(self):
#         return "I am a protected method"

# class Subclassprotected(ProtectedEncapsulation):
#     def __init__(self):
#         super().__init__()
#         print(self._protected_attribute)
#         print(self._protected_method())
        
# obj = Subclassprotected()

# class BankAccount:
#     def __init__(self,account_number,initial_balance =0):
#         self._account_number =account_number #Protected attribute
#         self.__balance = initial_balance     #Private attribute
#         self.__transaction_history = []
        
#     def deposit(self,amount):
#         self.__balance += amount
#         self.__transaction_history.append(("Deposit",amount))
        
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
    
    
# account = BankAccount("12345678",2000)

# account.deposit(1500)
# account.withdraw(400)

# print("Current Balance:",account.get_balance())
# print("Transaction History:",account.get_transaction_history())
        
def random(func):
    def wrapper():
        print("Author:XYZ")
        func()
    return wrapper


@random
def book():
    print("Title : Decorators in Python")
    
book()
            
        