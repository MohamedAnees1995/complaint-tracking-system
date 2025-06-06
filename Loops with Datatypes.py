#Lists

# numbers = [1,2,3,4,5,6,7,8,9,10]
# total = 0
# for num in numbers:
#     total+=num
# print("Sum of the numbers:",total)

#Finding maximum element 

# numbers = [1,2,3,4,5,6,7,8,9,10]
# max_num = numbers[0] #Assume the first element as maximum
# for num in numbers:
#     if num>max_num:
#         max_num = num
        
# print("The maximum number:",max_num)

books = {'learning python':'Mark Lutz','think python':'Allen B Downey','Fluent Python':"Luciana Ramalho"}
key = list(books)
i = 0
while i<len(key):
    if i==2:
        break
    print(key[i],":",books[key[i]])
    i+=1
    
print(key)