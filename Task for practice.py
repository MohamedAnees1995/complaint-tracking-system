n = int(input("Enter the no of rows:"))
pattern = lambda n:'\n'.join(['*' * i for i in range(1,n+1)]) 

print(pattern(n))







    