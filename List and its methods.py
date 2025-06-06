#list = ['apple','orange','banana']
#print(list)

#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.

#Allow Duplicates
#Since lists are indexed, lists can have items with the same value:

# A list can contain different data types
# A list with strings, integers and boolean values:
# list1 = ["abc", 34, True, 40, "male"]

# list1 = list(('apple','banana','cherry','mango','pineapple'))# Note the double round brackets
# list1.remove("banana") # Removes first instance of the "banana"
# print(list1)


# list1  = ['India','Pakistan','Srilanka','Bangladesh']
# list1.pop(2)  #If no index is specified it will pop out the last item in the list
# print(list1)

# list1  = ['India','Pakistan','Srilanka','Bangladesh']
# del list1[0]

# print(list1)

# list1.append("India")

# list1.clear()
# print(list1)

# list1= ['apple','banana','orange','mango']
# for i in list1:
#     print(i)

# list1= ['apple','banana','orange','mango'] for loop through index nos
# for i in range(len(list1)):
#     print(list1[i])

#Using a While Loop

# list = ['apple','banana','cherry']
# i=0
# while i < len(list):
#     print(list[i])
#     i = i + 1

# Looping using List Comprehension

# list = ['apple','banana','cherry']
# [print(x) for x in list ]

# fruits = ['apple','orange','pineapple','mango']
# new_list = []

# for x in fruits:
#     if 'a' in x:
#         new_list.append(x)
# print(new_list)

# fruits = ['apple','orange','pineapple','mango']
# new_list=[]

# for x in fruits:
#     if 'a' in x:
#         new_list.append(x)
# print(new_list)

# fruits = ['apple','orange','pineapple','mango']
# ruits = ['apple','orange','pineapple','mango']
# print(new_list)

# fruits = ['apple','orange','pineapple','mango']
# new_list=[x for x in fruits if x!= 'apple'] #Output + condition 
# print(new_list) 

#Accept only numbers lower than 5:

# newlist = [x for x in range(10) if x<5]
# print(newlist)


# thislist = [100, 50, 65, 82, 23] 
# thislist.sort(reverse=True)
# print(thislist) # sort() method is used to sort the list in ascending order by default 
# for descending order write list.sort(reverse = True)

#Sort the list based on how close the number is 50

# def my_func(n):
#     return abs(n-50)

# thislist = [100,50,65,82,23]
# thislist.sort(key=my_func) 
# #You can also customize your own function by using the keyword argument key = function.
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key=str.lower)
# print(thislist)
#sort() function by default sorts all capital letters first before sorting lower case letters
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# mylist = thislist.copy()
# print(mylist)

#Join Lists

list1 = ['a','b','c']
list2 = [1,2,3]

for x in list2:
    list1.append(x)
print(list1)
