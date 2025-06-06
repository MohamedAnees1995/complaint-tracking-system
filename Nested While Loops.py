#Printing a multiplication tablle

# row = 1
# while row<=10:
#     col = 1
#     while col<=10:
#         print(row*col, end = "\t")
#         col+=1
#     print() # Move to the next line
#     row+=1    


#Printing a pattern

# size = 5
# row = 1

# while row<=size:
#     col = 1
#     while col<=row:
#         print("*",end=" ")
#         col+=1
#     print()
#     row+=1
    
# items = ['A', 'B', 'C']
# for i in range(len(items)):
#     for j in range(i, len(items)):
#         print(items[i], items[j])
    
# Example dictionary
# student_grades = {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 65}

# # Initialize variables
# keys = list(student_grades.keys())
# index = 0

# # Outer loop to iterate over dictionary keys
# while index < len(keys):
#     student_name = keys[index]
#     grade = student_grades[student_name]
    
#     # Inner loop to perform some operation based on the grade
#     threshold = 80
#     while grade < threshold:
#         print(f"{student_name}'s grade is below {threshold}.")
#         grade += 5  # Increment the grade for demonstration purposes
    
#     print(f"{student_name}'s grade is {grade}.")
    
#     index += 1
                
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()

# student_grades = {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 65}

# for student,grade in student_grades.items():
#     if grade>80:
#         print(f'The student who scored above 80 are {student} with {grade}% marks.')

# def myfunc(x,y,func):
#     return func(x,y)
# result =myfunc(4,5, lambda x,y:x*y)
# print(result)

people = {
    'Alice': {'age': 30, 'occupation': 'Engineer'},
    'Bob': {'age': 25, 'occupation': 'Artist'},
    'Charlie': {'age': 35, 'occupation': 'Doctor'}
}

# Outer loop to iterate over each person
# people_names = list(people.keys())  # Get a list of people's names
# i = 0
# while i < len(people_names):
#     person_name = people_names[i]
#     person_info = people[person_name]

#     print(f"Name: {person_name}")
    
#     # Inner loop to iterate over each piece of information for the current person
#     info_keys = list(person_info.keys())  # Get a list of keys in the inner dictionary
#     j = 0
#     while j < len(info_keys):
#         info_key = info_keys[j]
#         info_value = person_info[info_key]
        
#         print(f"{info_key.capitalize()}: {info_value}")
        
#         j += 1
    
#     i += 1

# color_list = ["Red","Green","White" ,"Black"]

# # y = color_list[:1] + color_list[3:]
# # print(y)

# print("%s %s"%(color_list[0],color_list[-1]))
   
   
# Use triple double-quotes to create a multi-line string
# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example
# """)
   
def histogram(items):
    
    for n in items:
        output = ""
        times = n
        
        while times>0:
            output+="*"
            times-=1
            
        print(output)
        
histogram([1,2,3,4,5])
      
      
def histogram(items):
    
    for n in items:
        output = ""
        times = n
        
        while times>0:
            output+="*"
            times-=1
            
        print(output)