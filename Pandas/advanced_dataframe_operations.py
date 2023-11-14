# %%
# Distinguish between None, 0 and NaN
type(None)

# %%
type(0)

#%%
import numpy as np

type(np.nan)
np.nan + float("inf")
# %%
# Adding and Removing Columns
import pandas as pd
# Read CSV and get salary dataset
sf_sal = pd.read_csv('https://aicore-files.s3.amazonaws.com/Foundations/Data_Formats/Salaries.csv', index_col='Id')
sf_sal
# This will create a new column with a single value inc. integer/string/NoneType
# Note: If the name of the column exists, it will overwrite the whole column

sf_sal["new col"] = None

sf_sal.head() # shows the first 5 entries (the head) of the dataframe

# %%
#  To remove rows or columns, use the drop method

sf_sal.drop("AB").head(5)
# %%
# To remove "AB", "AC", and "AD"
sf_sal.drop(["AB", "AC", "AD"]).head()
# %%
# Drop COLUMNS
# By default, drop will remove rows based on the argument you passed.
# Drop a column - need to change the axis argument to 1
#sf_sal.drop("Status") # will generate error
sf_sal.drop("Status", axis=1).head(3)

# %%
# To make a change to the content of the original dataframe.
# Use the inplace argument and set it to True.

sf_sal.drop("Status", axis=1, inplace=True)


# %%
# ADDING ROWS
# To add a new row to a Pandas DataFrame, create a second DataFrame from the data you wish to append
#  use the pd.concat() method 

# Create a new row to add
new_row = pd.DataFrame({
    'EmployeeName': ['JOHN DOE'],
    'JobTitle': ['MANAGER'],
    'BasePay': [100000.00],
    'OvertimePay': [5000.00],
    'OtherPay': [2500.00],
    'Benefits': [float('nan')],
    'TotalPay': [107500.00],
    'TotalPayBenefits': [107500.00],
    'Year': [2011],
    'Notes': [float('nan')],
    'Agency': ['San Francisco']
})

# Append the row to the dataframe
sf_sal = pd.concat((sf_sal, new_row), ignore_index=True)

# Note that the old df.append() method is deprecated as of Pandas v2.0.

# %%
# Read CSV and get salary dataset
sf_sal = pd.read_csv('https://aicore-files.s3.amazonaws.com/Foundations/Data_Formats/Salaries.csv', index_col='Id')
sf_sal
# This will create a new column with a single value inc. integer/string/NoneType
# Note: If the name of the column exists, it will overwrite the whole column
sf_sal.head() # shows the first 5 entries (the head) of the dataframe

# %%
# copy() method
# In many programming languages, when you assign a value to a variable, 
# that variable is going to point to a new space in memory. 
# Remember that assigning a list to a new variable will make the new variable point to 
# the same space in memory that the original list was pointing to.
# When dealing with dataframes, it's quite common that you have to 
# create new dataframes based onAnd if you change the value of the new dataframe, 
# the original dataframe will be affected.

#In order to avoid it, you can use the copy() method that will create a copy of the original dataframe:

sf_copy = sf_sal.copy()
# %%


# Now, remove the "Status" column with no consequences on sf_sal
sf_copy.drop("Status", axis=1, inplace=True)
sf_copy.head()


# %%
# .loc and .iloc
# .loc will select rows or columns based on their names. 
# # For example, row "AB" can be accessed using loc["AB"]. 
# # However, if you want to get an entire column, for example "JobTitle", 
# # you can't use loc["JobTitle"]. 

# use .loc[] to select rows by row names and columns by column names
print(sf_sal.loc["AB"])
sf_sal.loc[:, "JobTitle"].head(3)


# %%
#  Combine them using ["row name", "column name"]
sf_sal.loc["FG", "JobTitle"]


# %%
# iloc will perform the same operation using numerical indices.
print(sf_sal.iloc[0])
print(sf_sal.iloc[0, 1])


# %%
# For subset of rows and columns, use lists of each within .loc[]
# can index out of order

sf_sal.loc[["AC", "CV", "BK"],["BasePay", "Year"]]
# This is a common error that occurs when you try to use .loc or [] 
# # to select rows or columns that are not present in the dataframe. 
# A possible solution is to use .reindex instead, which will align the dataframe 
# with the new labels and fill in any missing values with NaN.
sf_sal.reindex(index=["AC", "CV", "BK"], columns=["BasePay","Surname", "Year"])


# %%
# Comparing Dates in ISO format
# ISO 8601 is an internationally recognised way to compare dates and times
later_date_non_ISO = "February 17th 2021"
earlier_date_non_ISO = "January 16th 2000"

print(later_date_non_ISO < earlier_date_non_ISO)
print(later_date_non_ISO > earlier_date_non_ISO)

# Better using ISO 8601 format

later_date_ISO_format = "2021-02-17"
earlier_date_ISO_format = "2021-02-16"

print(later_date_ISO_format < earlier_date_ISO_format)
print(later_date_ISO_format > earlier_date_ISO_format)

# %%
# 
# And comparing times on the same day only a millisecond apart:
later_date_ISO_format = "2021-02-16 11:01:11:10"
earlier_date_ISO_format = "2021-02-16 11:01:11:09"
print(later_date_ISO_format < earlier_date_ISO_format)
print(later_date_ISO_format > earlier_date_ISO_format)



# %%
# Alternatively use Python's built-in library datetime
# The strptime method takes two arguments:
#  - The string to convert to datetime
#  - The format code

from datetime import datetime

non_ISO_datestring_one = "17 February, 1999"
non_ISO_datestring_two = "17/02/1999 18:40:02"
print(type(non_ISO_datestring_one))

datestring_one_ISO_format = datetime.strptime(non_ISO_datestring_one, "%d %B, %Y")
datestring_two_ISO_format = datetime.strptime(non_ISO_datestring_two, "%d/%m/%Y %H:%M:%S")
print(type(datestring_one_ISO_format))

print(datestring_one_ISO_format)
print(datestring_two_ISO_format)

print(datestring_one_ISO_format < datestring_two_ISO_format)



# %%
# When cleaning data using Pandas you might run into this issue where the dates in your dataframe are in non-ISO format.
# Creating our dataframe

data = {"Date" : ["17 February, 2021", "21 September, 2000", "18 August, 1956"],
        "DOB" : ["17/02/2021", "21/09/2000", "18/08/1956"],
        "Flight_Departure" : ["17/02/2021 18:02:01", "10/02/2010 19:01:11", "01/07/1998 11:02:56"]}

df = pd.DataFrame(data)
df
# %%
#
# Convert the dates to ISO format

df["Date"] = pd.to_datetime(df["Date"], format="%d %B, %Y")
df["DOB"] = pd.to_datetime(df["DOB"], format="%d/%m/%Y")
df["Flight_Departure"] = pd.to_datetime(df["Flight_Departure"], format="%d/%m/%Y %H:%M:%S")
df
# %%
# Conditional Selection

# boolean condition like this returns boolean applied to each value in the column (like NumPy)
# For example, how many people have a "TotalPay" greater than 30000.
sf_sal["TotalPay"] > 300000
# The output of the comparison is also named mask


# %%
# use a mask to filter dataframes just by indexing that mask to the dataframe.

mask = sf_sal["TotalPay"] > 300000

sf_sal_mask = sf_sal[mask]
sf_sal_mask

#Alternatively can be written like this to save lines of code:

sf_sal[sf_sal["TotalPay"] > 300000]


# %%
#
# Use conditional selection to find the following:
# A dataframe containing the Name, Total Pay (with Benefits), Job Title and Base Pay of the employee named 'Albert Pardini'.


albert_dataframe = sf_sal.loc[sf_sal["EmployeeName"] == 'ALBERT PARDINI']
albert_dataframe = albert_dataframe.loc[["AC"],["EmployeeName","TotalPayBenefits","JobTitle", "BasePay"]]
albert_dataframe


# %%
# The highest paid person in terms of Base Pay. (look up the .max() method) max(sf_sal["BasePay"])
highest_paid_person = sf_sal.loc[sf_sal["BasePay"] == max(sf_sal["BasePay"])]
highest_paid_person


# %%
# Set and Reset Index
#
#
# use .reset_index() to revert to original numerical index (must specify inplace=True)

sf_sal.reset_index()

# %%
sf_sal.reset_index(inplace=True)
sf_sal
# %%


#
# Use .set_index() to change the index to a column

sf_sal.set_index("Id")
# %%
