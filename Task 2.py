name = "MohamedAnees"
reverse_name = " "

i = len(name) - 1 # This will start with the last character in the string

# Iterate over the characters of the string in reverse order using a while loop

while i>=0:
    reverse_name = reverse_name + name[i]
    i = i - 1 # The index moves the next character in reverse in the string

print("Original Name:", name)
print("Reversed Name:", reverse_name)    
    

