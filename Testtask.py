# # # Calculating Exponential Function:
# # Write a lambda function to calculate the exponential of a number. The function should take two arguments: the base a and the exponent b, and return a raised to the power of b.

# # x = lambda a,b:a**b
# # print(x(2,4))

# #Creating a Simple Calculator:
# # Write a Python program that prompts the user to enter two numbers and an operation (addition, subtraction, multiplication, or division). Use lambda functions to perform the selected operation on the given numbers.  

# # Define lambda functions for each operation
# add = lambda x, y: x + y
# subtract = lambda x, y: x - y
# multiply = lambda x, y: x * y
# divide = lambda x, y: x / y if y != 0 else "Cannot divide by zero"

# # Function to prompt user for numbers and operation
# def calculator():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     operation = input("Enter the operation (add/subtract/multiply/divide): ").lower()

#     # Perform the selected operation using lambda functions
#     if operation == "add":
#         result = add(num1, num2)
#     elif operation == "subtract":
#         result = subtract(num1, num2)
#     elif operation == "multiply":
#         result = multiply(num1, num2)
#     elif operation == "divide":
#         result = divide(num1, num2)
#     else:
#         result = "Invalid operation"

#     print("Result:", result)

# # Call the calculator function
# calculator()


    
# # Sample list of strings
# strings = ["apple", "banana", "orange", "kiwi", "pear", "grape"]

# # Sort the list based on length and alphabetically
# sorted_strings = sorted(strings, key=lambda x: (len(x), x))

people = [{"name":"John", "age":25},{"name":"Jane", "age":35},{"name":"Jack", "age":40},{"name":"John", "age":30},{"name":"James", "age":45}]

# filtered_people = filter(lambda person: person['age'] > 30 and person['name'].startswith('J'), people)
# filtered_people_list = list(filtered_people)

# print("Filtered list:")
# for person in filtered_people_list:
#     print(person)
    
filtered_people = filter(lambda person:person['age']<30 and person['age']>25 and person['name'].startswith('J'),people)
filtered_people_list = list(filtered_people)

print("Filtered list:")

for person in filtered_people_list:
    print(person)