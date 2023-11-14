# %%
# Import pandas module
import pandas as pd
import yaml

# Reading CSV Data 
# For example, to read data from a CSV file, you can use the read_csv method. 
# To read data from an Excel file, you can use the read_excel method. 
# To read data from an XML file, you can use the read_xml method. And so on.

# df_csv = pd.read_csv('aiCoreDemo\Pandas\Salaries.csv')

# Note that there is a column called Id in the data with the same numbers as the index given by pandas.
df_csv = pd.read_csv('Salaries.csv', index_col="Id")
# %%
# Display short description of data contained in dataframe
df_csv.head()


# %%
# Display short description of data contained in dataframe
df_csv.describe()
# print(df_csv.head())


# %%
# Reading JSON Data 
df_json = pd.read_json('employees.json')

# %%
# Display short description of data contained in dataframe
df_json.head()
# %%
# Read second Json file
df_json_2 = pd.read_json('employees_2.json')
df_json_2.head()
# %%
# The JSON file has a nested structure in coloumn three
# It doesn't create a DataFrame with the nested structure
employees_df = pd.json_normalize(df_json_2['Employees'])
employees_df.head()

# %%
# Reading YAML Data 
# Pandas doesn't have a method to read data from a YAML file. 
# However, you can use the safe_load method from the yaml package to read data from a YAML file. 
# This is how to read data from a YAML file.



with open('animals.yaml', 'r') as f:
    animals = yaml.safe_load(f)

print(animals)

# %%
# Note that the animals variable is a dictionary whose key is the word "Animals" 
# and the value is a list of dictionaries. 
# Each dictionary in the list represents an animal with its name and species. 
# Create a DataFrame with the data.
df_yaml = pd.DataFrame(animals['Animals'])
df_yaml.head()

# %%
# WRITING DATA
# Create a sample DataFrame with some data and write it to a CSV file.

sample_df = pd.DataFrame({'column_1': [1, 2, 3, 4, 5], 'column_2': [6, 7, 8, 9, 10], 'column_3': [11, 12, 13, 14, 15]})
sample_df.head()

# display(sample_df.head())


# %%
# we can use the to_csv method to write the data to a CSV file. 
sample_df.to_csv('sample.csv',
                 index=False)  # index=False is used to avoid saving the index column. Try removing it and see what happens.

# %%
# Create a sample DataFrame with some data and write it to a JSON file.
# Use the to_json method to write data to a JSON file
sample_df.to_json('sample.json')

# %%
# The same way pandas doesn't have a way to read yaml files
# First, convert the dataframe to a dictionary

sample_dict = sample_df.to_dict()

# Then,  convert the dictionary to a yaml file

with open('sample.yaml', 'w') as f:
    yaml.dump(sample_dict, f)
# %%
