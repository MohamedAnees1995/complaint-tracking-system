# "r": Read mode (default). Opens a file for reading.
# "w": Write mode. Opens a file for writing. If the file exists, it truncates the file. If the file does not exist, it creates a new file.
# "a": Append mode. Opens a file for appending. If the file does not exist, it creates a new file.
# "b": Binary mode. Opens a file in binary mode (e.g., "rb", "wb", etc.).
# "+": Read and write mode.


# Beginner Methods 

# with open("text3.txt","w+") as file:
#     text = '''hello one point one
#     what are you doing right now
#     this is the end of the world
#     '''
#     file.write(text)
    
#     file.seek(5)
    
#     data = file.read()
#     print(data)
    
 
# data = file.read()  # return all data in a string type

# data = file.readline() #return first line of the file

# data = file.readlines() # return list object each element of the list is file data

# print(data)

# file.close()

# with open("example.txt","r") as file:
#     data = file.readlines()

# print(data)


# with open("example.txt", "a") as file:

#    text = "Hello how are you"

# text = "\ni am fine what about you"

# file.write(text)



# r+ (Read + write)



#   read and write 



#   Set cursor position
# file.seek(3)

#   # write
# text = "python"
# file.write(text)

# with open('example.txt", "w+") as file:

#  # write

#   text = "hello one point one"
#   file.write(text)

#   # set position
#     file.seek(1)


#   # read 

#    data = file.read()
#    print(data)

# f = open("demofile.txt", "r")
# print(f.read())

# print(f)

# File Handling Examples

# # Creating a file
# with open("example.txt", "w") as file:
#     file.write("This is an example file.\n")
#     file.write("It contains some text.")
    
# # Reading from a file
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# # Writing to a file
# with open("example.txt", "w") as file:
#     file.write("This is the new content of the file.")
    
# # Appending to a file
# with open("example.txt", "a") as file:
#     file.write("\nThis is appended content.")
    
# 1) r+ (Read and Write): Opens a file for both reading and writing. 
# The file pointer is placed at the beginning of the file.

# Using r+ mode to read and write
with open("example.txt", "r+") as file:
    content = file.read()  # Read existing content
    print("Current content:", content)
    
# Move the file pointer to the beginning
    file.seek(0)
    
     # Write new content at the beginning
    file.write("New content added.\n" + content)
    
# 2) w+ (Write and Read): Opens a file for reading and writing. If the file doesn't exist, 
# it creates a new file. If the file exists, it truncates it.
    
# Using w+ mode to write and read
# with open("example.txt", "w+") as file:
#     file.write("This is new content.\n")  # Write new content
    
#     # Move the file pointer to the beginning
#     file.seek(0)
    
#     # Read the content written
#     content = file.read()
#     print("Content:", content)
    
# 3) a (Append): Opens a file for appending. The file pointer is at the end of the file if the file exists. 
# That is, the file is in the append mode.

# Using 'a' mode to append
# with open("example.txt", "a") as file:
#     file.write("This is appended content.")

# 4) r (Read): Opens a file for reading only. 
# The file pointer is placed at the beginning of the file.

# Using 'r' mode to read
# with open("example.txt", "r") as file:
#     content = file.read()
#     print("Content:", content)
    
# 5) w (Write): Opens a file for writing only. Overwrites the file if the file exists. 
# If the file does not exist, creates a new file for writing.

# Using 'w' mode to write
# with open("example.txt", "w") as file:
#     file.write("This is new content.")
    
# 6) a+ (Append and Read): Opens a file for reading and appending. The file pointer is at the end of the file if the file exists. 
# The file opens in the append mode.

# Using 'a+' mode to append and read
# with open("example.txt", "a+") as file:
#     # Move the file pointer to the beginning
#     file.seek(0)
    
#     # Read the content
#     content = file.read()
#     print("Content:", content)
    
#     # Append new content
#     file.write("\nThis is appended content.")



    








    



    