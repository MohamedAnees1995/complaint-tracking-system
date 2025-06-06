# Outer loop
# x = 1
# while x <= 3:
#     print("Outer loop iteration:", x)
    
#     # Inner loop
#     y = 1
#     while y <= 2:
#         print("Inner loop iteration:", y)
#         y += 1
    
#     x += 1

i = 1                 # We create the first no to multiply for
while i<=10:          # We set the limit to 10
    j=1               # We create the first multiplicand for the no i 
    while j<=10:      # We set value to 10 to create a 10x10 multiplication table
        print(f'{i}*{j}= {i*j}')  #We set them to multiply followed by the result
        j+=1 # We increment the multiplicand by 1 and continue for first iteration of i and so on until i<=10
    print()   # Moves to the next line
    i+=1      # After completing first iteration of outer while loop it moves to 2nd iteration of outer while loop
    