# # Break statement
# # for i in range(10):
# #     if i ==5:
# #         break
# #     print(i)  # This will print numbers from 0 to 4

# # # Continue statement
# # for i in range(5):
# #     if i == 2:
# #         continue
# #     print(i)  # This will print numbers from 0 to 4, skipping 2
    
# # Find the first even number in a list

# # numbers = [1, 3, 5, 7, 8, 9, 10, 12]
# # for num in numbers:
# #     if num%2==0:
# #         print("First even number found:",num)
# #         break
    
# # Print only odd numbers from 1 to 10

# # for num in range(1,11):
# #     if num%2==0:
# #         continue # It skips the condition in which the number is even and prints the odd no
# #     print(num)

# #Count down number from 10 to 1

# # num = 15
# # while num>=1:
# #     print(num)
# #     num=num-1

# # Calculate factorial of a number


# # num=int(input("Enter the number:"))
# # factorial = 1

# # while num>0:
# #     factorial = factorial*num
# #     num=num-1
# # print("Factorial of the number :", factorial)

# #Password with maximum attempts

# # password = "secret"
# # max_attempts = 3
# # attempts = 0

# # while attempts<max_attempts:
# #      user_input = input("Enter the password")
# #      if user_input == password:
# #          print('Access Granted')
# #          break
# #      else:
# #          print("You have entered incorrect password!Try Again")
# #          attempts+=1
# # else:
# #     print('You have reached maximum attempts!Access Denied')           

# # Calculate the sum of digits of a number

# num = int(input("Enter a number"))
# sum_of_digits = 0
# while num>0:
#     digit = num%10   #Modulo operator by 10 to get the last digit
#     sum_of_digits+=digit
#     num//=10        #Integer operator by 10 to remove the last digit
    
# print('Sum of digits',sum_of_digits)

#Print fibonnacci series
 
# a,b = 0,1
# n = int(input("Enter the number of terms:"))
# count = 0
# while count<n:
#     print(a,end=" ")
#     c = a + b
#     a = b
#     b = c
#     count+=1

#Guessing Game 

# import random
# target = random.randint(1,100)
# guess = None
# while guess!=target:
#     guess = int(input("Enter your guess(between 1 and 100):"))
#     if guess<target:
#         print("Too Low!Try again.")
#     elif guess>target:
#         print("Too High!Try again.")
        
# print("Congratulations, you guessed the number correctly",target)

# num = int(input("Enter the digits:"))
# sum_of_digits = 0
# while num>0:
#     digit = num%10
#     sum_of_digits+=digit
#     num//10

# print("Sum of the digits:",sum_of_digits)

# count = 10
# while count>0:
#     print(count)
#     count-=1
    
#Sum of natural numbers  num(1 to 10) 

# limit = 12
# sum = 0
# num =1

# while num<=limit:
#     sum+=num
#     num+=1
    
# print("The sum of natural numbers upto",limit, "is" ,sum)
       
       
password = "secret"
max_attempts = 3
attempts = 0

while attempts<max_attempts:
    user_input = input("Enter your password")
    if user_input == password:
        print('Access Granted')
        break
    else:
        print("Incorrect password!Try Again")
        attempts+=1
else:
    print("You have reached the maximum attempts!Access Denied")        
        