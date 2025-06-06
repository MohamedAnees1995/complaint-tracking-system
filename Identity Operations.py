x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  # Result: False, because x and y reference different objects with the same values
print(x is z)  # Result: True, because x and z reference the same object

a = "hello"
b = "hello"

print(a is not b)  # Result: False, because a and b reference the same object (due to string interning)
