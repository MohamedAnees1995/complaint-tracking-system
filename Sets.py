#The values True and 1 are considered the same value in sets, and are treated as duplicates:

# [A set is a collection which is unordered, unchangeable*, and unindexed.][Sets are used to store multiple items in a single variable.

# The values False and 0 are considered the same value in sets, and are treated as duplicates:

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#     print(x)
tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# #To add items from another set into the current set, use the update() method.
# thisset.add("orange")
# print(thisset)

# #o remove an item in a set, use the remove(), or the discard() method.
# thisset.remove("orange")
# print(thisset)


# x = thisset.pop() # Pop method in sets removes a random item from the set
# print(x)

# print(thisset)

# del thisset    Delete the set permanently

# print(thisset)

# for x in thisset:
#     print(x)
    
    
#The union() method returns a new set with all items from both sets.

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}    

# set3 = set1|set2 # You can also use pipe | operator for the same result as union() method
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1 | set2 | set3 | set4
# print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)

# z = x.union(y)
# print(z)

#The update() method inserts all items from one set into another.

# The update() changes the original set, and does not return a new set.

# x.update(y)
# print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2
# print(set3)

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)

# print(set1)

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 - set2
# print(set3)

# Use symmetric_different_update to keep items that are not common in both the sets

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)

