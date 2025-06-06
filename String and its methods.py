### Strings in python are surrounded by either single quotation marks('), or double quotation marks('').

#print("Hello my name is Johnny")

#Assign String to a variable

#Strings are Arrays

#a = "Hello World"
#print(a[1])

##Looping Through a string

#for x in "banana":

##String Length : The len() function returns the length of the string

#a = "Hello World"
#print(len(a))    

##Check String : To check if a certain phrase or character is present in a string *keyword(in)* can be used

##Lets check 'free' in the following text 

#txt = "The best things in life are free"
#if 'expensive' not in txt:
   #print("No, Expensive is not present in txt")

#b = "Hello World!" #(Slice from the Start)
#print(b[:5])

#b = "Hello World!" #(Slice to the End)(By leaving out the end index, the range will go to the end.)
#print(b[2:])

#Negative indexing

#b = "Hello World!"
#print(b[-5:-2])    # No change in start index but when we take end index we take 1 position before the index

#a= "Hello World!" # upper for converting string to caps and lower to convert string to lower case
#print(a.upper())

#The Strip Method ("The strip() method removes any whitespace from the beginning or the end:")

#a= "Hello World!"
#print(a.strip("!"))

## Concatenate the strings

#a = "Hello"
#b = "World"

#c = a + " " +  b
#print(c)

#Format - Strings: (We can combine strings and numbers by using f-strings or the format() method!)
#Simply put an "f" in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

#Name = "Shavukath Ali"
#Age = "57"

#txt = f"My name is {Name} and My Age is {Age}"
#print(txt)

#Place holder and modifiers(A placeholder can contain variables, operations, functions, and modifiers to format the value.)

#price = 99
#txt = f"The price is {price} in dollars"
#print(txt)

#Modifier : A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

#price = 98.2
#txt = f'The price is {price:.2f} in dollars'
#print(txt)

# (Escape Characters) To insert illegal characters in a list we use backslash \ followed by the character you want to insert

#\'	Single Quote	
#\\	Backslash	     - This will return 1 backslash
#\n	New Line	        - This will take the string to new line
#\r	Carriage Return  - Same as new line	
#\t	Tab	           - Adds space to the string txt = "Hello\tWorld!"  Hello World
#\b	Backspace	     - erases one character (backspace):
#\f	Form Feed	     - No example
#\ooo	Octal value	     - A backslash followed by three integers will result in a octal value:
#\xhh	Hex value        - A backslash followed by an 'x' and a hex number represents a hex value:
#print(a.capitalize())    # First letter of the string to uppercase 
#print(a.casefold())      # Entire string to lowercase
#print(a.center(20, "-")) # Returns a centered string
#print(a.count("l"))      # Counts the number of instance of that letter in the string
#print(a.encode())        # Returns encoded version of the string
#print(a.endswith('d'))   # Returns true if the string ends with that character
#print(a.expandtabs(5))   # Sets the tab size of the string. put \t in the string to create tab size
#print(a.find("d"))       # find(): Searches the string for a specified value and returns the position of where it was found.
#print('My name is {} and my age is {}.'.format(name,Age)) # formats specified values in a string

#my_dict = {'name' : 'Anees', "age" : "28" }
#print('My name is {name} and I am {age} years old.'.format_map(my_dict)) 

#print(name.index('h'))   Index method : returns index as well as the index no

my_list=['Hello','World']
print(" ".join(my_list))   # Joins the elements of an iterable to the end of the string.

string = 'Hello'
print(string.ljust(10,"-"))