# Nested for loops are commonly used when you need to iterate over multiple dimensions of data, such as nested lists, matrices, or when dealing with combinations of elements.

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# # Finding transpose of matrix
# transpose = []
# for i in range(len(matrix[0])): #the outer loop iterates over the columns of the matrix
#     transpose_row = []
#     for row in matrix:
#         transpose_row.append(row[i])
#     transpose.append(transpose_row)
# print(transpose)

#Generating combinations of list and numbers.

# list1 = ['a', 'b']
# list2 = [1, 2]

# # Generating combinations
# combinations = []
# for letter in list1:
#     for number in list2:
#         combinations.append((letter,number))
# print(combinations)        
 
#2D list manipulation

# grid= [[1,2,3],
#        [4,5,6],
#        [7,8,9]] 

# #Summing all elements
# total = 0
# for row in grid:  #Iterate each row in grid
#     for element in row: # Iterate each element in the row from the grid
#         total = total + element # Sum the elements to get the total
# print(total)  

# Pattern printing

size = 5

for i in range(size):
    for j in range(i+1):
        print("*",end=" ")
    print()    

#Finding prime nos in a range

# start = 10
# end = 50

#Finding prime nos between start and end



# for num in range(start,end+1):
#     if num>1:
#         is_prime = True
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 is_prime = False
#                 break
#             if is_prime:
#                 print(num)
            
        
# Matrix Multiplication

# matrix1 = [[1, 2],
#            [3, 4]]
# matrix2 = [[5, 6],
#            [7, 8]]

# Matrix multiplication
# result = [[0, 0],
#           [0, 0]]
# for i in range(len(matrix1)): #Iterate over rows of matrix 1
#     for j in range(len(matrix2[0])): #Iterate over columns of matrix 2
#         for k in range(len(matrix2)): #Iterate over rows of matrix 2
#             result[i][j] += matrix1[i][k] * matrix2[k][j] # We multiply i and j with k for matrix multiplication
# print(result)
        
        
