# # Count and Index methods in tuple

# # count()	Returns the number of times a specified value occurs in a tuple.
# # index()	Searches the tuple for a specified value and returns the position of where it was found.

# y = ("apple","apple","mango","orange","pineapple")
# x = y.index("orange")

# print(x)

# for i in range(1, 11):  
#     for j in range(1, 11): 
#         print(i * j, end="\t")
#     print()

for i in range(1,11):
    for j in range(1,11):
        print(i*j , end = "\t")
    print()