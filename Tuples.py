#Tuple items are ordered, unchangeable, and allow duplicate values.

#Ordered and unchangeable
#Since tuples are indexed they can have items with the same value

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# thistuple = ("apple",) # To create a tuple with only 1 item
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple")

# if 'apple' in thistuple:
#     print('Yes')

#Changing Tuple values
# x= ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

#Add items to a tuple convert to list use append and convert it back to a tuple
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# You are allowed to add items to a tuple

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple = thistuple + y

# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y= list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)

# y=list(thistuple)
# y.remove("apple")
# thistuple=tuple(y)

#The del keyword can delete the tuple completely

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)

#This will raise an error because this tuple no longer exists

#in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

# fruits = ('apple','banana','cherry')

# (green,yellow,red) = fruits

# print(green)
# print(yellow)
# print(red)

#Using Asterisk
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green,yellow,*red) = fruits

# print(green)
# print(yellow)
# print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


