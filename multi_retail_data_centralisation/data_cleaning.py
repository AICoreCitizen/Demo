# Import the required modules
import pandas as pd
import numpy as np
import re

# Define the DataCleaning class
class DataCleaning:
    # Initialize the class with the data sources
    def __init__(self, data_sources):
        self.data_sources = data_sources # A list of file names or URLs
        self.dataframes = [] # A list of pandas dataframes
    
    # Load the data from the sources
    def load_data(self):
        for source in self.data_sources:
            try:
                # Read the data as a pandas dataframe
                df = pd.read_csv(source)
                # Append the dataframe to the list
                self.dataframes.append(df)
            except Exception as e:
                # Print the error message
                print(f"Error loading data from {source}: {e}")
    
    # Clean the data from each source
    def clean_data(self):
        for i, df in enumerate(self.dataframes):
            # Get the source name
            source = self.data_sources[i]
            # Apply different cleaning methods based on the source
            if source == "sales.csv":
                self.clean_sales_data(df)
            elif source == "customers.csv":
                self.clean_customers_data(df)
            elif source == "products.csv":
                self.clean_products_data(df)
            else:
                print(f"Unknown data source: {source}")
    
    # Clean the sales data
    def clean_sales_data(self, df):
        # Drop the unnecessary columns
        df.drop(["order_id", "order_date"], axis=1, inplace=True)
        # Convert the price column to numeric
        df["price"] = pd.to_numeric(df["price"], errors="coerce")
        # Fill the missing values with the mean
        df["price"].fillna(df["price"].mean(), inplace=True)
        # Remove the outliers
        df = df[df["price"] < df["price"].quantile(0.99)]
    
    # Clean the customers data
    def clean_customers_data(self, df):
        # Drop the duplicates
        df.drop_duplicates(subset=["customer_id"], inplace=True)
        # Split the name column into first_name and last_name
        df[["first_name", "last_name"]] = df["name"].str.split(" ", expand=True)
        # Drop the name column
        df.drop(["name"], axis=1, inplace=True)
        # Extract the email domain
        df["email_domain"] = df["email"].str.extract("(@\w+.\w+)")
        # Replace the invalid phone numbers with NaN
        df["phone"] = df["phone"].apply(lambda x: x if re.match("\d{3}-\d{3}-\d{4}", x) else np.nan)
    
    # Clean the products data
    def clean_products_data(self, df):
        # Drop the rows with missing values
        df.dropna(inplace=True)
        # Convert the category column to lowercase
        df["category"] = df["category"].str.lower()
        # Replace the spaces with underscores
        df["category"] = df["category"].str.replace(" ", "_")
        # Remove the special characters
        df["category"] = df["category"].str.replace("[^a-z_]", "")