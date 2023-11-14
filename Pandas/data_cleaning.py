# %%
import pandas as pd
import numpy as np
from dateutil.parser import parse

pd.set_option('display.max_columns', None) # You can use this setting display all the columns in your dataframe
flights_df = pd.read_csv("C:\\Users\\abrah\\OneDrive\\projects\\aiCoreDemo\\Pandas\\flights_sample.csv") 
flights_df.head(5)
print(flights_df.head(5))

# %%
# Checking data type
# The .dtypes attribute only returns the data type of each column
flights_df.dtypes
# %%
# Checking data type
# The .info() method returns both the data type and some additional information: 
# the number of rows and the memory usage of the dataframe, 
# as well as the number of non-null values in each column. 
flights_df.info()

# %% [markdown]
# Below is a table that shows various Pandas data types, their corresponding Python data types, and a brief description of each.
# Pandas Dtype	Python Dtype	    Description
# object	    str	                Used for text or mixed types of data
# int64	        int	                Integer numbers
# float64	    float	            Floating-point numbers
# bool	        bool	            Boolean values (True/False)
# datetime64	datetime.datetime	Date and time values
# timedelta64	datetime.timedelta	Differences between two datetimes
# category	    (special type)	    Finite list of text values
# period	    pd.Period	        Periods of time, useful for time-series data
# sparse	    (special type)	    Sparse array to contain mostly NaN values
# string	    str	                Text
# Note that:
# 
# The int64 and float64 data types indicate 64-bit storage for integer and floating-point numbers, respectively. 
# Pandas also supports other sizes (like int32 and float32) to save memory when the larger sizes are not necessary.
# The _category_ dtype is not a native Python data type but is provided by Pandas to optimize memory usage and performance 
# for data with a small number of distinct values
# The sparse dtype is used for data that is mostly missing to save memory by only storing the non-missing values
# The period dtype is specific to Pandas and is used for handling period data, 
# which is not directly analogous to a native Python type		
# %%
# Create a simple dataframe of names and ages
data = {'Name': ['Alice', 'Bashar', 'Carlos', 'Diana', "Ephraim", "Frank", "Gina"],
        'Age': [21, 22, 'n/a', 24, 25, 'missing', 27]}
age_df = pd.DataFrame(data)
age_df.info()
# %%
# Looking at the output of info(), both columns have defaulted to the Object datatype. We can easily change the Name column to the string
age_df.Name = age_df.Name.astype('string')
age_df.info()
# %%
# Try to cast the Age column as int64, the method throws a ValueError, because it encountered some values (missing and n/a)
age_df.Age = age_df.Age.astype('int64')
# %%
# By default, the astype() method throws an error when it encounters a non-convertible value, 
# as this prevents accidental data loss. We can override this behaviour by setting the errors flag to ignore rather than raise:
age_df.Age = age_df.Age.astype('int64', errors='ignore')
age_df.info()
# %%
# But this actually fails to alter the datatype, as it leaves the unconvertible values unchanged, as can be seen in the output below.
age_df.head(10)
# %%
#  use a separate function, pd.to_numeric(), use with the errors parameter set to coerce to force the conversion:
age_df.Age = pd.to_numeric(age_df.Age, errors='coerce')
age_df.info()
# %%
age_df.head(10)
# %%
age_df.Age = age_df.Age.astype('int64', errors='ignore')
age_df.info()

# %%
# The datetime64 Data Type
# The pd.to_datetime function can be used to cast a column to datetime64
# consider the format that the date/time values are in.

data = {
    'date_strings': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01']
}
date_df = pd.DataFrame(data)

date_df.info()


# %%
date_df.date_strings = pd.to_datetime(date_df.date_strings)
date_df.info()
# %%
date_df.head()
# %% [markdown]
# Common Issues: Epoch Time

# %%
# The epoch is set at 00:00:00 UTC on Thursday, January 1, 1970
# and the count of seconds (or milliseconds in some applications) from this point is used to represent subsequent points in time

flights_df['FLIGHTDATE'].head(5)
# %%
# Pandas has detected the dtype of the FLIGHTDATE column as int64, 
# whereas it would be more helpful to have it as datetime64, so that it can be used in time-series analysis.

pd.to_datetime(flights_df['FLIGHTDATE']).head(5)
# It looks like the first few values of the column are in January, 1970. 
# This should arouse suspicion, given what we know about Epoch time.
# The function has interpreted the integer values in FLIGHTDATE as a number of seconds after the Epoch, 
# when actually it should be a date in the formatYYYmmdd.
# %%
# To work around this, specify a format as an argument to the to_datetime function, as follows:
date_format = "%Y%m%d"
pd.to_datetime(flights_df["FLIGHTDATE"], format=date_format)

# %% [markdown]
# Common Issues: Mixed Date Formats
# %%
# Handling multiple date formats in a single column can be a bit tricky, 
# but pd.to_datetime is quite flexible and can infer different formats automatically in most cases

# Create a sample dataframe with multiple date formats
data = {
    'mixed_dates': ['01/02/2023', '2023-03-01', '04-Apr-2023', '20230505']
}
mixed_date_df = pd.DataFrame(data)

# Displaying the original dataframe
print("Original Dataframe:")
print(mixed_date_df)
print("\nData types:")
print(mixed_date_df.dtypes)
# %%
# Converting the 'mixed_dates' column to datetime
# Note: infer_datetime_format=True can help to infer different formats, but might not handle all cases
mixed_date_df['dates'] = pd.to_datetime(mixed_date_df['mixed_dates'], infer_datetime_format=True, errors='coerce')

# Displaying the modified dataframe
print("\nModified dataframe:")
print(mixed_date_df)
print("\nData types:")
print(mixed_date_df.dtypes)
# automatic conversion has not been very effective, and  multiple values have been returned as NaT (Not a Time).
# %%
# A more effective approach is to use the parse function from the dateutil library, in conjunction with the .apply method:
# from dateutil.parser import parse
mixed_date_df['dates'] = mixed_date_df['mixed_dates'].apply(parse)
mixed_date_df['dates'] = pd.to_datetime(mixed_date_df['dates'], errors='coerce')
print("\nModified dataframe:\n")
print(mixed_date_df)
print("\nData types:\n")
print(mixed_date_df.dtypes)

# %% [markdown]
# The timedelta64 Data Type
# %%
# The timedelta64 data type is used to represent differences in datetime64 objects. While a datetime64 object represents a specific point in time, with a defined year, month, day, hour, minute, and so on, 
# a timedelta64 object represents a duration that is not anchored to a specific start or end point. 
# It tells how much time is between two points, without specifying what those points are.

# When you perform arithmetic with two datetime64 objects, the result is a timedelta64 object because subtracting one point in time from another gives you a duration
# Conversely, when you add or subtract a timedelta64 from a datetime64 object, you get another datetime64 object because you're shifting a point in time by a certain duration

# Subtracting a single date from the 'dates' column
single_date = pd.Timestamp('2023-01-01')  # Creating a Timestamp object
mixed_date_df['date_difference'] = mixed_date_df['dates'] - single_date  # Subtracting the single date

# Displaying the modified dataframe
print("\nModified dataframe:")
print(mixed_date_df)

# %% [markdown]
# Selecting a Subset of Data

# Creating a sample dataframe
data = {
    'Name': ['Alansana', 'Briana', 'Chanmony', 'Dietrich', 'Eva'],
    'Age': [23, 34, 45, 36, 50],
    'Country': ['USA', 'Switzerland', 'UK', 'Switzerland', 'Canada']
}
customers = pd.DataFrame(data)

# Displaying the original dataframe
print("Original dataframe:")
print(customers)

# Using `loc` to select rows based on a logical expression
swiss_customers = customers.loc[customers['Country'] == 'Switzerland']

# Displaying the dataframe with only Swiss customers
print("\nSwiss Customers:")
print(swiss_customers)

# %%
# elect multiple values from your column for a subset of the data, you can use the .isin() method 

# Selecting rows where 'Country' is either 'USA' or 'UK'
selected_countries = ['USA', 'UK']
mask = customers['Country'].isin(selected_countries)

# Using the mask to get the subset of the DataFrame
subset_df = customers[mask]

# Displaying the subset of the DataFrame
print("\nSubset DataFrame (Countries: USA, UK):")
print(subset_df)


# %%
# Logical indexing can also be used in conjunction with other methods, 
# such as dropping values. In many cases this requires the creation of a logical mask, 
# which is a Boolean data series of the same length as the number of rows in the dataframe. 
# Creating a logical mask for ages between 30 and 40
age_mask = (customers['Age'] >= 30) & (customers['Age'] < 40)

print(age_mask)
# %%
# Using the logical mask to create a new column 'marketing_email'
# Set to True where the condition is met, and False otherwise
customers['marketing_email'] = False  # Initialize column with False
customers.loc[age_mask, 'marketing_email'] = True  # Apply mask to set True where condition is met

# Displaying the dataframe with the new column
print("\ndataframe with 'marketing_email' Column:")
print(customers)


# %% [markdown]
# Handling Missing and Incorrect Values
# Missing Values and NaNs
age_df.head(10)
# %%
# There are two NaN values in the column, and we have the choice to either drop of impute the values to resolve this.
# It is not certain the ages of Frank and Carlos
# If analysis depends on the Age column, it might be better to drop the missing values. 
# This can be achieved with the .dropna() method.

age_df.dropna()  # Drop rows with any column having NA/null data. 
# If we wanted to apply this result permanently, we would need to assign it to a new dataframe or use the `inplace=True`` argument


# %%
# Alternatively, we might know in advance that all of the students are between the ages of 20 and 30, 
# and so it might be acceptable to replace the missing values with the mean or median average. 
# This can be achieved with the fillna() method:

value_to_impute = age_df.Age.mean().round()  # Calculate the mean of the Age column and round it to the nearest integer

age_df.fillna(value_to_impute, inplace = True)  # Fill NaNs with the value we calculated

# %%
age_df.Age = age_df.Age.astype('int')  # Round the Age column and convert it to an integer
age_df.info()
# %%
age_df
# %% [markdown]
# Detecting and Fixing Incorrect Values
# %%
# flights_df contain two columns that appear to be intended as Boolean values: CANCELLED and DIVERTED.
flights_df.head(3)
flights_df['CANCELLED'].value_counts()
# %%
# There are a couple of techniques to fix this situation. The first is to use the .replace() method to replace one value with another. 
flights_df['CANCELLED'].replace({'0': False}, inplace=True)
flights_df['CANCELLED'].value_counts()
# Note that False appears twice in the value_counts result. 
# This is because Pandas is distinguishing between the string "False" and the Boolean value False. 
# %%
# df.replace({'0': False, '1' : True}) to replace all instances of 0 or 1 with False and True respectively
# This can also be achieved using the map function, which can apply a mapping (or even a function) to all the elements in a column or series.

mapping_dictionary = {'0': False, '1': True, 'F': False, 'T': True, 'True': True, 'False': False}
flights_df['CANCELLED'].replace(mapping_dictionary, inplace=True)
flights_df['CANCELLED'].value_counts()

# %%
# Now that column contains just True and False values, convert it to bool type:
# Now that our column contains just True and False values, convert it to bool type:

flights_df['CANCELLED'] = flights_df['CANCELLED'].astype('bool')

print('datatype of flights_df["CANCELLED"]:')
print(flights_df['CANCELLED'].dtype)

flights_df['CANCELLED'].value_counts() # note that the result of value_counts will always show the data type as an integer, as it is a count.
# %% [markdown]
# Forcing Values to Adhere to a Pattern
# A regular expression, often abbreviated as regex, 
# is a sequence of characters that defines a search pattern that can be used 
# for matching, allowing for complex search, replace, and validation operations.
# %%
# Searching regexlib for UK Phone Number provides this option:
# ^((\(?0\d{4}\)?\s?\d{3}\s?\d{3})|(\(?0\d{3}\)?\s?\d{3}\s?\d{4})|(\(?0\d{2}\)?\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$

# Creating a sample dataframe
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Phone': ['0123456789', '01234 567890', '+441234567890', '0123-456-789',
              '(0123) 456789', '1234567890', '0123456789a', '01234-567-890',
              '+44 1234 567890', '01234']
}

phone_df = pd.DataFrame(data)

phone_df.head(10)
# %%
# import numpy as np # We will need the `nan` constant from the numpy library to apply to missing values

regex_expression = '^(?:(?:\(?(?:0(?:0|11)\)?[\s-]?\(?|\+)44\)?[\s-]?(?:\(?0\)?[\s-]?)?)|(?:\(?0))(?:(?:\d{5}\)?[\s-]?\d{4,5})|(?:\d{4}\)?[\s-]?(?:\d{5}|\d{3}[\s-]?\d{3}))|(?:\d{3}\)?[\s-]?\d{3}[\s-]?\d{3,4})|(?:\d{2}\)?[\s-]?\d{4}[\s-]?\d{4}))(?:[\s-]?(?:x|ext\.?|\#)\d{3,4})?$' #Our regular expression to match
phone_df.loc[~phone_df['Phone'].str.match(regex_expression), 'Phone'] = np.nan # For every row  where the Phone column does not match our regular expression, replace the value with NaN
phone_df.head(10)
# %% [markdown]
# Cleaning Numeric Columns with .replace()

# Replace any instances of +44 with 0, as this is how to write the number for calling within the UK
# Replace the ( and - characters with nothing (i.e. remove them)
# Remove all spaces
# %%
# You can do each step one by one, for example with the following syntax for the `+44`: 0 replacement:

phone_df['Phone'] = phone_df['Phone'].str.replace('+44', '0', regex=False)
phone_df

# Or by setting `regex=True`, you can do it all in one step:

phone_df['Phone'] = phone_df['Phone'].replace({r'\+44': '0', r'\(': '', r'\)': '', r'-': '', r' ': ''}, regex=True)
phone_df
# %% [markdown]
# Unique Values
# The unique method returns all the unique (i.e. distinct) values in the data series. For example from a series of [ 1, 1, 2, 3, 4] it would return [1, 2, 3, 4]
# The nunique method returns the count of unique values in the series. For example from a series of [ 1, 1, 2, 3, 4] it would return 4.
# %%
# Creating a sample dataframe with a column of product IDs
data = {'product_ids': ['P001', 'P002', 'P003', 'P001', 'P004', 'P005', 'P003', 'P006', 'P002']}
products_df = pd.DataFrame(data)

# Using `unique` to get unique product IDs
unique_ids = products_df['product_ids'].unique()

# Using `nunique` to get the number of unique product IDs
num_unique_ids = products_df['product_ids'].nunique()

# Displaying the original dataframe
print("Original dataframe:")
print(products_df)

# Displaying the unique product IDs
print("\nUnique product IDs:")
print(unique_ids)

# Displaying the number of unique product IDs
print("\nNumber of unique product IDs:")
print(num_unique_ids)

# Display the total number of rows in the dataframe
print("\nTotal number of rows in the dataframe:")
print(len(products_df))
# %%
# Duplicates in data refer to two or more rows that are identical across all columns, or, depending on the context, identical in a subset of columns, 
# which can lead to redundancy and inaccuracies in data analysis and interpretation. 
# Exact duplicates are trivial to handle in Pandas. 
# Find all the duplicated rows in a dataframe using the .duplicated() method, or drop them using the drop_duplicates() method. 
import pandas as pd

# Creating a sample dataframe
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Eva', 'Charlie'],
    'Age': [28, 34, 45, 28, 23, 45],
    'Phone': ['123-456', '456-789', '789-012', '123-456', '345-678', '789-012'],
    'Email': ['alice@email.com', 'bob@email.com', 'charlie@email.com',
              'alice@email.com', 'eva@email.com', 'charlie@email.com']
}
duplicate_df = pd.DataFrame(data)
duplicate_df

# %%
# Identifying and dropping exact duplicates
df_no_duplicates = duplicate_df.drop_duplicates()

# Displaying the dataframe after removing duplicates
print("\ndataframe After Removing Duplicates:")
print(df_no_duplicates)
# %%
# fuzzy duplicates
data = {
    'First_Name': ['Alice', 'Alice', 'Alice',  'Alice'],
    'Last_Name': ['Smith', 'Smith', 'Smith', 'Smith'],
    'Age': [28, 34, 45, 45],
    'Phone': ['123-456', '456-789', '123-456', '123-456'],
    'Email': ['alice@email.com', 'alice@smith.com',
              'alice@theinternet.com',  'Alice@theinternet.com']
}

fuzzy_duplicates_df = pd.DataFrame(data)
fuzzy_duplicates_df

# Generally, the more columns you have for reference, the easier it is to determine 
# whether a partial match is a duplicate. There are also software tools to help you, 
# for example this python library: https://pypi.org/project/fuzzywuzzy/ that uses the Levenshtein Distance 
# to calculate the differences between strings.


# %% [markdown]

# Categorical Data
# Categorical columns are those in which the values are drawn from a predefined set of categories.

# Creating a sample dataframe
data = {
    'Customer Name': ['Amina', 'Bahru', 'Charlie', 'Dion', 'Ebo', 'Frank', 'Giana'],
    'Postal Region': ['UK', 'England', 'Wales', 'Cymru', 'Scotland', 'USA', 'Canada']
}
df = pd.DataFrame(data)

# Displaying the original dataframe
print("Original dataframe:")
print(df)
# %%
# Creating a mapping dictionary to unify the country names
country_mapping = {
    'UK': 'United Kingdom',
    'England': 'United Kingdom',
    'Wales': 'United Kingdom',
    'Cymru': 'United Kingdom',
    'Scotland': 'United Kingdom'
}

# Replacing the country names in the 'Postal Country' column
df['Postal Region'] = df['Postal Region'].replace(country_mapping)

# Displaying the DataFrame after cleaning the 'Postal Country' column
print("\nDataFrame After Cleaning 'Postal Country' Column:")
print(df)
# %% [markdown]

# Creating Categorical Columns from Continuous Data
#  You might meet instances in your dataset where you might want to generate new categories based on continuous data. This can be achieved through a process called binning, which means dividing the spectrum of possible values into regions, known as bins.
# Creating a sample dataframe
data = {
    'Route': ['NYC-LON', 'LON-PAR', 'NYC-TOK', 'LON-SYD', 'PAR-BER'],
    'Distance': [3461, 214, 6749, 10562, 546]
}
flights = pd.DataFrame(data)

# Displaying the original dataframe
print("Original dataframe:")
print(flights)

# Defining the bin edges and labels
bin_edges = [0, 1500, 4000, 12000]  # in miles
bin_labels = ['short haul', 'medium haul', 'long haul']

# Creating a new categorical column 'Flight Type' by binning the 'Distance' column
flights['Flight Type'] = pd.cut(flights['Distance'], bins=bin_edges, labels=bin_labels, right=False)

# Displaying the dataframe with the new 'Flight Type' column
print("\ndataframe with 'Flight Type' Column:")
print(flights)

# Note - We create a dataframe flights with columns Route and Distance, 
# containing various flight routes and their distances in miles
# We define the bin edges bin_edges and labels bin_labels to specify the ranges 
# and labels for our new categorical data. 
# Note that there is one more element in the bin edges list than the number of bins 
# The bin edges define the lower and upper bounds of each bin. 
# So a short haul flight will be from 0 to 1500 miles in this case.
# We use pd.cut() to create a new column Flight Type by binning the Distance column 
# based on the defined bins and labels. 
# The argument right = False is used to specify that the bins are left-closed, 
# meaning that the left bin edge is included in the bin, 
# but the right bin edge is not.
# Finally, we display the original and modified dataframes to observe the changes
# %%
