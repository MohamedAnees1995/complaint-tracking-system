# # 2
    
#     # Input from the user for the number of rows
# num_rows = int(input("Enter the number of rows: "))

# # Lambda function to print the star pattern
# print_pattern = lambda n: '\n'.join(['* ' * i for i in range(1, n + 1)])

# # Print the pattern using the lambda function
# print(print_pattern(num_rows))


# Prompting the user for input
rows = int(input("Enter the number of rows for the pattern: "))

# Generating the pattern
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

print(" " * (rows - i) + "*" * i )
