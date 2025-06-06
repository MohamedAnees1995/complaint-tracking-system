# # #1D Array (One-Dimensional Array):

# # A 1D array is a linear collection of elements stored in contiguous memory locations.
# # It consists of a single row or a single column of elements.
# # In Python, 1D arrays are commonly represented using lists.
# # Each element in a 1D array can be accessed using its index, which starts from 0 for the first element.

# # Usage:

# # 1D arrays are used to represent sequences or lists of elements where each element has a single index.
# # They are suitable for storing and accessing data in a linear manner.
# # Examples include lists of numbers, characters, or any other homogeneous data types.

# # 2D Array (Two-Dimensional Array):

# # A 2D array is a collection of elements organized in a two-dimensional grid or matrix.
# # It consists of rows and columns, where each element is identified by its row and column indices.
# # In Python, 2D arrays can be represented using lists of lists.
# # Each element in a 2D array is accessed using its row and column indices.

# # Usage:

# # 2D arrays are used to represent grids, tables, or matrices of elements where each element has two indices: row and column.
# # They are suitable for storing and accessing data arranged in rows and columns.

# #Arrays can be used to store multiple values in a single variable

# players = ["Virat","Rohit","Hardik"] 

# # x = len(players)
# # print(x)

# # for x in players:
# #     print(x)

# #players.append("MSD")

# #print(players)

# #players.pop(1) # You can use the pop() method to remove an element of an array

# #print(players)

# #Remove() to remove an element from an array

# #players.remove("Hardik")
# #print(players)

# # fruits = ["orange","apple","mango"]
# # fruits.append("pineapple")
# # print(fruits)

# # fruits = ['apple', 'banana', 'cherry']

# # fruits.insert(3, "orange")
# # print(fruits)

# #The remove() method removes the first occurrence of the element with the specified value.

# # fruits = ['apple', 'banana', 'cherry','banana']

# # fruits.sort(reverse=True)

# # print(fruits)

# # Sort the list by the length of its values

# # def myFunc(e):
# #     return len(e)

# # fruits = ['apple', 'banana', 'cherry','banana']
# # fruits.sort(reverse=True,key=myFunc)

# # print(fruits)

# # # Creating a 1D array (list)
# # arr = [1, 2, 3, 4, 5]

# # # Accessing elements of the array
# # print(arr[0])  # Output: 1
# # print(arr[2])  # Output: 3

# # # Creating a 2D array (list of lists)
# # arr_2d = [[1, 2, 3],
# #           [4, 5, 6],
# #           [7, 8, 9]]

# # # Accessing elements of the 2D array
# # print(arr_2d[0][0])  # Output: 1 (element at row 0, column 0)
# # print(arr_2d[1][2])  # Output: 6 (element at row 1, column 2)

# # Initializing an array
# arr = [1, 2, 3, 4, 5]  

# # Accessing elements
# print(arr[0])  # Output: 1 

# # Traversal
# for element in arr:
#     print(element)

# # Searching
# if 3 in arr:
#     print("3 is present in the array")

# # Sorting
# arr.sort()
# print(arr)  # Output: [1, 2, 3, 4, 5]

# # Copying
# arr_copy = arr.copy()

# # Resizing (not directly supported in Python lists, need to create a new list)
# new_arr = arr + [6, 7, 8]
# print(new_arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# # Creating an empty array
# arr = []

# # Creating an array with initial values
# arr = [1, 2,3, 4, 5]

# # Accessing elements by index
# print(arr[0])  # Output: 1
# print(arr[2])  # Output: 3

# # Inserting elements at the end
# arr.append(6)

# # Inserting elements at specific positions
# arr.insert(2, 10)

# # Deleting elements by value
# arr.remove(3)

# # Deleting elements by index
# del arr[0]

# # Traversing the array
# for element in arr:
#     print(element)

# # Searching for an element
# if 5 in arr:
#     print("5 is present in the array")

# # Sorting the array
# arr.sort()

# # Merging two arrays
# arr2 = [6, 7, 8]
# merged_arr = arr + arr2

# # Splitting the array into two parts
# split_index = 3
# arr1 = arr[:split_index] # 0 to 2
# arr2 = arr[split_index:] # 3 to last index

# # Concatenating arrays
# arr3 = [9, 10]
# concatenated_arr = arr + arr3 

# # Shallow copy of the array
# arr_copy = arr.copy()

# # Resizing the array
arr = [1,2,3,4]
arr = arr + [11, 12, 13]
print(arr)


