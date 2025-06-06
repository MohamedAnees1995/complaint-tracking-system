a = 5  # Binary representation: 101
b = 3  # Binary representation: 011

result_and = a & b  # Result: 1 (Binary representation: 001); if both bits are 1 result is 1 else it is 0
print("Bitwise AND:", result_and)

a = 5  # Binary representation: 101
b = 3  # Binary representation: 011

result_or = a | b  # Result: 7 (Binary representation: 111); If either bit is 1, the result is 1; otherwise, it's 0.
print("Bitwise OR:", result_or)

a = 5  # Binary representation: 101
b = 3  # Binary representation: 011

result_xor = a ^ b  # Result: 6 (Binary representation: 110);  If the bits are different, the result is 1; otherwise, it's 0.
print("Bitwise XOR:", result_xor)

a = 5  # Binary representation: 101

result_not = ~a  # Result: -6 (Binary representation: 11111111111111111111111111111010); It inverts all bits of the operand
print("Bitwise NOT:", result_not)
