# # # # # # Dictionaries are used to store data values in key:value pairs.

# # # # # # A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# thisdict = {
#   "Team": "India",
#   "Sponsor": "Byjus",
#   "Year": 2021,
#   "Coach" : "Dravid"
# }
# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # # # print(thisdict) # You can access the key using [] square brackets.

# # # # # print(type(thisdict)) # type() constructor used to check the type of the datatype.

# # # # # print(thisdict["Sponsor"])

# # # # # x  = thisdict.get("year") 
# # # # # print(x)

# # # # # The keys() method will return a list of all the keys in the dictionary.

# # # # # x = thisdict.values()
# # # # # print(x)

# # # # x = thisdict.values()

# # # # print(x) # Before the change

# # # # thisdict["Board"] = "BCCI"  Add the key to the dict using [] and the values after the "=" sign.

# # # # print(x)  # After the change

# # # # print(thisdict)

# # # x = thisdict.items() # Use items() to get the key-value pairs together

# # # print(x)

# # # print(x) # Before the change 

# # # thisdict["year"] = 2022

# # # print(x) # After the change

# # # if 'Sponsor' in thisdict:
# # #     print('Yes, Sponsor is one of the keys in this dictionary')
# # # else:
# # #     print("The following key is not present in this dictionary")

# # thisdict['year'] = 2000

# # print(thisdict)

# # The update() method will update the dictionary with the items from the given argument.

# # thisdict.update({"year":2009})
# # print(thisdict)

# #Adding an item to the dictionary is done by using a new index key and assigning a value to it:

# thisdict.update({'Coach' : "Dravid"})
# print(thisdict)

# print(thisdict)

#The pop() method removes the item with the specified key name:

# thisdict.update({"Sponsor":"Byjus"})
# print(thisdict)

# The popitem() method removes the last inserted item

# thisdict.popitem() 
# print(thisdict)

#The del keyword removes the item with the specified key name:

# thisdict["Sponsor"] = "Byjus"
# print(thisdict)

# The clear() method empties the dictionary:

# thisdict.update({"Team":"India", "Sponsor": "Byjus", "Year": 2021, "Coach":"Dravid"})
# print(thisdict)

# for x in thisdict:
#     print(thisdict[x])

# for x in thisdict.keys():
#     print(x)

# Loop through both keys and values, by using the items() method:

# for x,y in thisdict.items():
#     print(x,y)

#Make a copy of a dictionary with the copy() method:

# mydict = thisdict.copy()
# print(mydict)

# You can also make the copy of the dictionary using the dict() method.

# mydict = dict(thisdict)
# print(mydict)

# Create a dictionary that contain three dictionaries:

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily["child2"]["name"])

# # You can loop through a dictionary by using the items() method like this:

# for x,obj in myfamily.items():
#   print(x)
  
#   for y in obj:
#     print(y + ":" , obj[y])
    
    

# x = ("Sachin", "Kohli", "Ganguly")
# y = "Captained India at some point of time"

# thisdict = dict.fromkeys(x,y)
# print(thisdict)     

x = {'Sachin' : 248 , "Kohli" : 254 , "Ganguly": 239}

x.popitem()
print(x)