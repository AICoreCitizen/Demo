
#  %% 
# Import Python Modules
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
# %%
# Load data into a DataFrame
# https://aicore-files.s3.amazonaws.com/Data-Eng/Car_Insurance.csv
car_insurance_df = pd.read_csv('Car_insurance.csv', index_col='Id')
insurance_df = car_insurance_df.copy()

# %%

# How many missing values each column has?
insurance_df.info()
# Descriptive data types
insurance_df.dtypes
# shape prints insurance_df no. of rows by cols 
insurance_df.shape
# shape prints insurance_df cols names
insurance_df.columns



# %%
# Overview of Data
insurance_df.head(5)
# %%
# Check how many missing values each column has
print(insurance_df.isnull().sum())
# Drop the rows containing missing values
new_insurance_df = insurance_df.dropna()

# %%
# For the numerical values, obtain the mean average value

new_insurance_df.select_dtypes(include=np.number).mean()
# Select_dtypes method allows one to specify the data types to include or exclude from the DataFrame. 
# Use np.number to include all numeric types, ouse a list of specific numeric types, such as ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']. 
# Use exclude instead of include to filter out the data types not wanted. 

# %%
# Observe the Job column. 
new_insurance_df["Job"]
# How many categories can you find? 
# Displaying all unique ctaegories
print("\nUnique categories:")
print(new_insurance_df['Job'].unique())
# Displaying the number of unique ctaegories
print("\nNumber of unique categories:")
print(new_insurance_df['Job'].nunique())
# What is the most frequent?
print("\nCategories:")
print(new_insurance_df['Job'].value_counts())
print("\nMost frequent category?:")
print(f"Category: {new_insurance_df['Job'].value_counts().idxmax()},  Value: {new_insurance_df['Job'].value_counts().max()}")


# %%
# Create a sample DataFrame with Start and End columns
df = pd.DataFrame({
    "Start": ["13:45:20", "14:58:08", "15:11:24", "16:30:24"],
    "End": ["13:50:15", "15:10:12", "15:15:36", "16:35:18"]
})

# Convert the columns from object to time
df["Start"] = pd.to_datetime(df["Start"], format="%H:%M:%S").dt.time
df["End"] = pd.to_datetime(df["End"], format="%H:%M:%S").dt.time

# Create a new column with the duration of each call in seconds
df["Duration"] = df.apply(lambda row: (datetime.combine(datetime.min, row["End"]) - datetime.combine(datetime.min, row["Start"])).total_seconds(), axis=1)

# Print the DataFrame
print(df)

# %%

new_insurance_df.info()
# Current data type is object - change to time Epoch standard
# use origin=‘unix’, which the number of seconds since 1970-01-01 and unit=‘s’ to convert them to datetime objects.
time_format = "%H:%M:%S"
#new_insurance_df["CallStart"]
new_insurance_df.loc[:,'CallStart'] = pd.to_datetime(new_insurance_df['CallStart'], format=time_format, origin="unix")
#new_insurance_df["CallEnd"]
new_insurance_df.loc[:, 'CallEnd'] = pd.to_datetime(new_insurance_df['CallEnd'], format=time_format, origin="unix")
new_insurance_df.info()
# %%
new_insurance_df.loc[:, "Duration"] = pd.to_datetime(new_insurance_df['CallEnd'], format="%H:%M:%S", origin="unix") - pd.to_datetime(new_insurance_df['CallStart'], format="%H:%M:%S", origin="unix")
new_insurance_df
new_insurance_df.info()
#new_insurance_df["Duration"] = new_insurance_df["Duration"].astype('datetime64')
# %%
# What is the average duration of each call?
mean_duration = new_insurance_df["Duration"].mean()

# Access the hours, minutes, and seconds components
hours = mean_duration.components.hours
minutes = mean_duration.components.minutes
seconds = mean_duration.components.seconds

# Format it as a string with the HH:MM:SS format
output = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
print(output)

# %%
# For those people contacted during the first half of the year (Jan-June). 
# What is the most common way of communication (telephone, cellular...)?

# %%



