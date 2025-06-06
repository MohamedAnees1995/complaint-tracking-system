# with open("blahblah.txt","w") as file:
#     file.write("My name is Mohamed Anees.\n")
#     file.write("My favorite sport is cricket.\n")
#     file.write("I like to have freedom in my life.\n")
#     file.write("Why is the world very serious")
    
    
#     file.close()

# with open("blahblah.txt","r") as file:        
#     content = file.readlines()  #It reads all the lines and shows the output as a list.
#     print(content)
    
#     file.close()
    

# with open('blahblah.txt', mode='r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)


# with open("usermanual.txt","w") as file:
#     file.write("For turning ON TV press Power button\n")
#     file.write("For turning OFF TV press Power button again\n")
#     file.write("Thanks for using the TV\n")
#     file.write("See you later alligator")

# file.close() 

# with open("usermanual.txt","r") as file:
#     content = file.read()
    
#     print(content)
    
# file.close()

# with open("usermanual.txt","a") as file:
    
#     file.write("\nAppending new line")
    
# file.close()


# def delete_line(file_name,line_number):
#     with open("usermanual.txt","r") as file:
#         lines = file.readlines()
        
#     if 0<line_number<=len(lines):
#         del lines[line_number - 1]
        
#     with open("usermanual.txt","w") as file:
#         file.writelines(lines)
        
# delete_line("user_manual",1)

# with open("utf8_text.txt", "w", encoding="utf-8") as file:
#     file.write("Hello,世界!")
    
# with open("utf8_text.txt", "r",encoding="utf-8") as file:
#     content = file.read()
#     print(content)
    
# import sys

# sys.setdefaultencoding("utf-8")

# original_string = "Hello, world"
# encoded_bytes = original_string.encode("utf-8")
# print("Encoded Bytes:",encoded_bytes)
# print(type(encoded_bytes))

# decode_string = encoded_bytes.decode("utf-8")
# print("Decoded String:",decode_string)
# print(type(decode_string))

# Handling Non ASCII characters

# unicode_string = "Café"
# utf8_bytes = unicode_string.encode("utf-8")
# print("UTF-8 Bytes:",utf8_bytes)
# print(type(utf8_bytes))

# decode_string = utf8_bytes.decode("utf-8")
# print("Decoded Unicode:",decode_string)
# print(type(decode_string))

# Using open() with encoding argument

# with open("blahblah.txt","r",encoding="utf-8") as file :
#     content = file.read()
#     print(content)
    
# import os

# def create_file(filename):
# 	try:
# 		with open(filename, 'w') as f:
# 			f.write('Hello, world!\n')
# 		print("File " + filename + " created successfully.")
# 	except IOError:
# 		print("Error: could not create file " + filename)

# def read_file(filename):
# 	try:
# 		with open(filename, 'r') as f:
# 			contents = f.read()
# 			print(contents)
# 	except IOError:
# 		print("Error: could not read file " + filename)

# def append_file(filename, text):
# 	try:
# 		with open(filename, 'a') as f:
# 			f.write(text)
# 		print("Text appended to file " + filename + " successfully.")
# 	except IOError:
# 		print("Error: could not append to file " + filename)

# def rename_file(filename, new_filename):
# 	try:
# 		os.rename(filename, new_filename)
# 		print("File " + filename + " renamed to " + new_filename + " successfully.")
# 	except IOError:
# 		print("Error: could not rename file " + filename)

# def delete_file(filename):
# 	try:
# 		os.remove(filename)
# 		print("File " + filename + " deleted successfully.")
# 	except IOError:
# 		print("Error: could not delete file " + filename)


# if __name__ == '__main__':
# 	filename = "example.txt"
# 	new_filename = "new_example.txt"

# 	create_file(filename)
# 	read_file(filename)
# 	append_file(filename, "This is some additional text.\n")
# 	read_file(filename)
# 	rename_file(filename, new_filename)
# 	read_file(new_filename)
# 	delete_file(new_filename)

# import os

# def create_file(file_name):
#     try:
#         with open(file_name,"w") as f:
#             f.write("Hello, world!\n")
#         print("File " + file_name + " created successfully. ")
#     except IOError:
#         print("Error: could not create file." + file_name)
        
# def read_file(file_name):
#     try:
#         with open(file_name,"r") as f:
#             contents = f.read()
#             print(contents) 
#     except IOError:
#         print("Error: could not read the file." + file_name)
        
# def append_file(file_name,text):
#     try:
#         with open(file_name,"a") as f:
#             f.write(text)
#         print("Text appended to file " + file_name + " successfully.")
#     except IOError:
#         print("Error:could not append text to file " + file_name)
        
# def rename_file(file_name,new_filename):
#     try:
#         os.rename(file_name,new_filename)
#         print("File " + file_name + " renamed to " + new_filename + " successfully.")
#     except IOError:
#         print("Error: could not rename file " + file_name)
        
# def delete_file(file_name):
#     try:
#         os.remove(file_name)
#         print("File " + file_name + " deleted succesfully.")
#     except IOError:
#         print("Error: could not delete the file. " + file_name)
        
# if __name__ == "__main__":
#     filename = "example.txt"
#     new_filename = "new_example.txt"
    
#     create_file(filename)
#     read_file(filename)
#     append_file(filename, "This is some additional text.\n")
#     read_file(filename)
#     rename_file(filename,new_filename)
#     read_file(new_filename)
#     delete_file(new_filename)
    
# write() method example:

# with open("example.txt","w") as file:
#     file.write("Hello World!\n")
#     file.write("This is a new line.")
        
# writelines() method example:

# lines = ["First line\n" , "Second line\n", "Third line\n" , "Fourth line\n"]
# with open("example.txt" , "w") as file:
#     file.writelines(lines)
    
# file.close()

# read() method example:

# with open("example.txt", "r") as file:
#     contents = file.readlines()
#     print(contents)

# Various ways to read and write data in a file.

# file1 = open("myfile.txt",'w') 
# L = ['This is Delhi \n' , 'This is Paris \n' , 'This is London \n']

# file1.write("Hello\n")
# file1.writelines(L)
# file1.close() # close file to change access modes.

# file1 = open("myfile.txt","r+")
# print("The Output of read function :")
# print(file1.read())
# print()

# # seek(n) takes the file handle to the nth
# # byte from the beginning.

# file1.seek(0)

# print("Output of readline function is :")
# print(file1.readline())
# print()

# file1.seek(0)

# # To show difference between read and readline

# print("Output of Read() function is")
# print(file1.read())
# print()

# file1.seek(0)

# print("Output of Readline() function is")
# print(file1.readline())
# print()

# file1.seek(0)

# print('Output of Read(9) function is ')
# print(file1.read(9))
# print()

# file1.seek(0)

# print("Output of Readline(9) function is")
# print(file1.readline(9))

# file1.seek(0)

# Seek changes the position of the cursor within the file. seek(0) means move the cursor to the beginning of the file.

# #Readlines function()

# print("Output of Readlines() function is")
# print(file1.readlines())
# print()
# file1.close()

# Readline reads line 1 by 1 and Readlines reads all the lines at once.

# with open("dmo_id.txt","w") as file:
#     L = ["ID : ilovefriends2\n","pwd : andagundu\n"]
#     file.write("Digimon Masters Online Login Info\n\n")
#     file.writelines(L)
# file.close()

# with open("dmo_id.txt","r+") as file:
#     content = file.readlines()
#     print(content)
# file.close()

# with open("dmo_id.txt","r+") as file:
#  file.seek(0)
 
#  f = file.readline()
 
#  print(f)


# #Accessing Binary files

# some_bytes = b'\xC3\xA9'

# # Open in "wb" mode to
# # write a new file, or 
# # "ab" mode to append
# with open("my_file.txt", "wb") as binary_file:

# 	# Write bytes to file
# 	binary_file.write(some_bytes)

# binary_file.close()

# with open("my_file.txt","rb") as binary_file:
    
#     reader = binary_file.read()
#     print(reader)
    
# binary_file.close()
    
# l = ["Apple","Orange","Mango"]

# with open("my_file.txt","w+") as f:
    
#     #write elements of list
#     for items in l:
#         f.write("%s\n" %items)
    
#     print("Files written succesfully.")
    
# f.close()

# Working with file pointers

# import os

# file_info = os.stat("dmo_id.txt")
# print("Size of file",file_info.st_size)
# print("Last Modified",file_info.st_mtime)

# class Error(Exception):
#     def __init__(self,value):
#         self.value = value
        
#     def __str__(self):
#         return(repr(self.value))
    
# try:
#     raise(Error(3*2))
# except Error as error:
#     print("A new exception has occured: ",error.value)

# try:
#     # Some Code
# except:
#     # Executed if error in the
#     # try block


def Abs(a,b):
    try:
        c = ((a +b))//((a -b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
        
Abs(24,22)
Abs(3,5)