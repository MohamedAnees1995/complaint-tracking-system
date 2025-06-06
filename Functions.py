# Lambda Function

#lambda arguments : expression

# x = lambda a,b, : a**a + 2*a*b + b**b
# print(x(4,2))

# The power of lambda is better shown when you use them as an anonymous function inside another function.

# def myfunc(n):
#     return lambda a : a*n

# mydoubler = myfunc(2)

# print(mydoubler(22))

# def myfunc(n):
#     return lambda a : a*n

# mytripler = myfunc(3)

# print(mytripler(44))

# def myfunc(n):
#     return lambda a : a*n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))

#Use lambda functions when an anonymous function is required for a short period of time.

# def my_multiplier():
#     return lambda x,y: x*y

# multiplier = my_multiplier()

# result = multiplier(10,100)
# print(result)


##Arguments

# def my_function(fname):
#     print(fname + ":Indian Cricketer")
    
# my_function("Virat Kohli")
# my_function("Rohit Sharma")
# my_function("Hardik Pandya")
# my_function("MS Dhoni")

# def my_function(fname,lname):
#     print(fname + " " + lname)
    
# my_function('Rohit','Sharma')

#To call a function use the function name followed by parenthesis:

# def area_of_triangle(len,wid):
#     return 0.5*len*wid

# result = area_of_triangle(10,5)

# print(result)
    
# area_of_triangle = lambda base,height : 0.5*base*height  
# result = area_of_triangle(20,40)
# print(result)   

# import math
# pi_value = math.pi
# area_of_circle = lambda radius: pi_value*radius*radius

# result = area_of_circle(20)
# print(result)

#Default parameter

#Default parameters allow you to specify a default value for a function argument. When the function is called, if the caller doesn't provide a value for that argument, the default value is used instead. 

# With default parameter we can specify a value for a function argument

# def greet(name, greeting="Hello"): 
#     print(greeting, name) 
    
# greet("Bob")


# def cricketer(name, nation = " : India"):
#     print(name,nation)
    
# cricketer("Virat Kohli ")

# def my_func(country = 'Norway'):
#     print("I am from:",country)
    
# my_func("India")  #Calling the function with an argument
# my_func("SriLanka")
# my_func()     # Calling the function with default argument
# my_func("Pakistan")

#*args(Arbitrary Arguments)

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# def my_func(*kids):
#     print("The youngest child is " + kids[1])
    
# my_func("Jack","Jimmy","John")

# def my_func(*batsmen):
#     print("The most prolific batsmen for India is:" + batsmen[1])
    
# my_func("Sachin Tendulkar","Virat Kohli","Rohit Sharma")
    
#*kwargs = Keyword arguments = If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# def my_func(**kid):
#     print("His first name is " + kid["fname"])
    
# my_func(fname = "Virat", lname = "Kohli")


# def my_func(**People):
#     print("His Father name is " + People["fathername"])
    
# my_func(fname = "Virat", fathername = "Prem Kohli")    

#*args stores the result in the form of a tuple inside a variable.

# def add(*args):
#     result = 0
#     for num in args:
#         result+=num
#     return result

# print(add(1224,2222))
        
# def div(*args):
#     result = args[0]   # Taking the first element
#     for num in args[1:]: # Skipping the first element and iterating over the rest of the elements
#         result/=num
#     return result

# print(div(555,11))
        
# def example_function(*args, **kwargs):
#     # Use args like a tuple
#     for arg in args:
#         print(arg)
    
#     # Use kwargs like a dictionary
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# example_function(1, 2, 3, name="John", age=30)


# def example_function(*args, **kwargs):
#     # Use args like a tuple
#     for arg in args:
#         print(arg)
        
#     # Use kwargs like a dictionary
    
#     for key,value in kwargs.items():
#         print(f'{key}:{value}')
        
# example_function(1,2,3, name = "Anees" , Age = "28")        
        
# def example_function(*args,**kwargs):
#     for arg in args:
#         print(arg)
        
#     for key,value in kwargs.items():
#         print(f'{key}',{value})
        
# example_function(22,24,26, name='Virat',Age = 36)       

# def print_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key}',{value})
        
# print_info(name ="Alice",Age = 30,city ='Wonderland')


# def player_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key}',{value})
        
# player_info(name = "Virat Kohli",Age = 36,Year = 1988)

# def div(*args):
#     result = args[0]
#     for num in args[1:]:
#         result/=num
#     return result

# print(div(221,5))    
        
        
# def player_stat(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key}',{value})
        
# player_stat(Batsmen = "Heinrich Klaasen", StrikeRate = 200,Nationality = "South Africa")

dict_team = {"Virat":700,'Head':500,'Rohit':200,'MSD':300,'KL Rahul':550}
for player,score in dict_team.items():
    if score <700:
        print("The player is not from RCB")
    else:
        print("He is Virat Kohli from RCB")
        

