# While loop with a condition

# num = 1
# while num<=5:
#     print(num)
#     num+=1


# For loop with conditional statements

# num = [1,2,3,4,5,6,7,8,9,10]
# for number in num:
#     if number%2==0:
#         print(number,"is even")
#     else:
#         print(number,"is odd")
            
            
numbers_input = input("Enter the list of numbers seperated by spaces: ")
numbers = [int(num) for num in numbers_input.split()]

for number in numbers:
    if number%2==0:
        print(number,"is even")
    else:
        print(number,"is odd")    
            