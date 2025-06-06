def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result*i

number = 5
print("Factorial of", number, "is", factorial(number))