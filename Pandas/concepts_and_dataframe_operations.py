#%%
# Import pandas module
import pandas as pd
# Import string module
import string
#%%
# Read CSV and get salary dataset
sf_sal = pd.read_csv('https://aicore-files.s3.amazonaws.com/Foundations/Data_Formats/Salaries.csv')
sf_sal

# Get alpahbets in uppercase and store in varaible called alphabet
alphabet = string.ascii_uppercase
alphabet
# create an empty list
index_list = []
# creating a list of 2-letter alphabetical codes
for first in alphabet:
    for second in alphabet:
            index_list.append(first + second)

print(index_list)

#%%
# use these letters as the indices for the salaries dataset
sf_sal["Id"] = index_list
sf_sal.set_index("Id", inplace=True)
sf_sal
sf_sal.to_csv('data.csv')


# %%
# Just reading in a dataset to demonstrate operations.
sf_sal = pd.read_csv('https://aicore-files.s3.amazonaws.com/Foundations/Data_Formats/Salaries.csv', index_col='Id')
# Index set to be the 'Id' column. Try to remove that argument and see what happens!
sf_sal
# %%
# Selection and Indexing
# Single bracket notation returns a Pandas series
type(sf_sal["BasePay"])

#%%
# Double bracket returns a Pandas dataframe.
type(sf_sal[["BasePay"]])


# %%
sf_sal["BasePay"]
# %%
sf_sal[["BasePay"]]

# %%
# selecting multiple columns requires double brackets
sf_sal[["BasePay","TotalPay"]]

# %%
# info() and describe() gives a brief summary of the dataframe we are handling
sf_sal.info()

sf_sal.describe()


# %% [markdown]
# Lambda/Anonymous Expressions with .apply() method
# lambda input : output (in terms of input)
# e.g. to square --> lambda x : x**2

# %%
sf_sal["Surname"] = sf_sal["EmployeeName"].apply(lambda x: x.split()[1])
sf_sal.head()
# %%
# Alternatively
def find_surname(x):
    return x.split()[1]

sf_sal["Surname"] = sf_sal["EmployeeName"].apply(find_surname)

# check head to see if it worked
sf_sal.head()
# %%
# Create other columns based on different conditions. 
# For example, check samples that have the word "POLICE" in their JobTitle.

# define function to find 'police' first

def find_police(x):
    return "POLICE" in x


# use apply to search for it in JobTitle
sf_sal["isPolice"] = sf_sal["JobTitle"].apply(find_police)

sf_sal[["JobTitle", "isPolice"]]
# %%
# check how many "POLICE" there are in the dataframe
# sum
sf_sal["isPolice"].sum()
# %%
#
# Use the Salaries.csv file calculate:
# What is the ratio between people in the fire department over people in the police department
# What is the mean salary of the police department? Use the BasePay column.
# What is the mean salary of the fire department? Use the BasePay column.
sf_sal["isPolice"] = sf_sal["JobTitle"].apply(lambda x:"POLICE" in x)
sf_sal.head()
sf_sal["isFire"] = sf_sal["JobTitle"].apply(lambda x:"FIRE" in x)
sf_sal.head()

# %%
# check how many "POLICE" Dept staff there are in the dataframe
# sum
total_Police = sf_sal["isPolice"].sum()
# check how many "FIRE" Dept staff there are in the dataframe
# sum
total_Fire = sf_sal["isFire"].sum()
# %%
# Ratio: Fire/Poilce
ratio_fire_to_police = total_Fire/total_Police
print(ratio_fire_to_police)
# %%
#filter dataframe for when isPolice is True
df_police = sf_sal[sf_sal["isPolice"]==True]
mean_police_base_pay = df_police["BasePay"].mean()
# %%
#calculate mean salary of Police department
total_base_police_pay = df_police["BasePay"].sum()
mean_police_base_pay = total_base_police_pay/total_Police
# apply the lambda function to calculate the mean salary of Police department
mean_police_base_pay = df_police["BasePay"].apply(lambda x: x/total_Police).sum()
#mean_police_base_pay = df_police.apply(lambda x: x["BasePay"].mean())
print(mean_police_base_pay)

# %%
#check mean values for Police Staff
df_police.describe()

# %%
#filter dataframe for when isFire is True
df_fire = sf_sal[sf_sal["isFire"]==True]
mean_fire_base_pay = df_fire["BasePay"].mean()
print(mean_fire_base_pay)

# %%
#filter dataframe for when isPolice is True
df_fire.describe()

# %%
# Testing Lambda method - create a sample DataFrame with occupation and salary columns
df = pd.DataFrame({
    "occupation": ["teacher", "doctor", "lawyer", "doctor", "nurse"],
    "salary": [50000, 80000, 90000, 120000, 60000]
})

# group the DataFrame by occupation and apply the lambda function to calculate the mean salary
mean_salary = df.groupby("occupation").apply(lambda x: x["salary"].mean())

# print the result
print(mean_salary)
# %%
