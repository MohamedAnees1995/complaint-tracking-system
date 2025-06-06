# Write a Python program to determine the grading of a student based on their exam score. The grading criteria are as follows:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
# Your program should prompt the user to enter the exam score, then print out the corresponding grade.

score = int(input("Enter the exam score:")) # Ask the user for exam score

if score>=90 and score<=100:
    grade = 'A'
elif score>=80 and score<=89:
    grade = 'B'
elif score>=70 and score<=79:
    grade = 'C'
elif score>=60 and score<=69:
    grade = 'D'
else:
    grade = 'F'
    
print("Grade:",grade)    

