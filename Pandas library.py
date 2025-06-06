# Pandas is a powerful and widely-used open-source Python library for data manipulation and analysis.

# 1) Create DataFrame with a Dictionary:

import pandas as pd

data_dict = {
        'Name' : ['Alice','Bob','Charlie','David'],
        'Age' : [25,30,35,40],
        'City' : ['New York','Los Angeles','Chicago','Houston']
}

df = pd.DataFrame(data_dict)
print(df)

# # 2) Create DataFrame with a list:

import pandas as pd

data_list = [['Alice',25,'New York'],['Bob',30,'Los Angeles'],['Charlie',35,'Chicago'],['David',40,'Houston']]

columns = ['Name','Age','City']

df = pd.DataFrame(data_list,columns = columns)
print(df)

# 3) Create DataFrame with a tuple:

data_tuples = [('Alice',25,'New York'),('Bob',30,'Los Angeles'),('Charlie',35,'Chicago'),('David',40,'Houston')]

columns = ['Name','Age','City']

df = pd.DataFrame(data_tuples,columns=columns)

# print(df)

srow = df.loc[0,'Name']  # Extract single values using row and column label loc[row name,column name]
print(srow)

mrow = df.loc[0:3,['Name','City']]# Extract multiple values using row and column labels loc[rowname[index],[column names]
print(mrow)

# Extracting single columns and multiple columns

# [] allows you to specify column names directly to extract single or multiple columns.
# loc[] accessor allows you to specify row and column labels to extract data.
# iloc[] accessor allows you to specify integer-based indices to extract data.

# Series is a one dimensional array that can hold data of anytype

import pandas as pd

a = [1,7,2]

myvar = pd.Series(a)

print(myvar)

data = {
    'Name': ['Virat Kohli','Kane Williamson','Joe Root','Steve Smith'],
    'Age': [33,30,31,32],
    'Country':['India','NewZealand','England','Australia'],
    'Runs':[13000,10000,12000,9000]
}

# # Create a dataframe 

df = pd.DataFrame(data)
df = df.rename_axis('ID')

df.reset_index(inplace=False)
print(df)

print()

# Extract Kohli country and runs also name

srow = df.loc[[1,2],:]

print(srow)

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

# print(df) 

print(df.loc[[0,1,2]])

df.corr()

import pandas as pd

products = {
    'Name': ['Laptop','Mobile','Television','Computer'],
    'Brand': ['Dell','Samsung','Onida','Intel Corei5'],
    'Price': [55000,25000,20000,40000]
}

products_df = pd.DataFrame(products)

print(products_df)

products_df.rename(index = "Serial no",inplace=True)

print(products_df)


