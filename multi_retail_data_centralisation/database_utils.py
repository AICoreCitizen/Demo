# Import the required modules
import sqlite3
import pandas as pd

# Define the DatabaseConnector class
class DatabaseConnector:
    # Initialize the class with the database name
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None # Connection object
        self.cursor = None # Cursor object
    
    # Connect to the database
    def connect(self):
        try:
            # Create or open the database file
            self.conn = sqlite3.connect(self.db_name)
            # Create a cursor object
            self.cursor = self.conn.cursor()
            # Return True if successful
            return True
        except Exception as e:
            # Print the error message
            print(f"Error connecting to {self.db_name}: {e}")
            # Return False if failed
            return False
    
    # Close the connection
    def close(self):
        if self.conn:
            # Commit any changes
            self.conn.commit()
            # Close the connection
            self.conn.close()
            # Set the connection and cursor objects to None
            self.conn = None
            self.cursor = None
    
    # Execute a SQL query
    def execute(self, query):
        if self.cursor:
            try:
                # Execute the query
                self.cursor.execute(query)
                # Return the result as a list of tuples
                return self.cursor.fetchall()
            except Exception as e:
                # Print the error message
                print(f"Error executing query: {e}")
                # Return None if failed
                return None
        else:
            # Print a message if not connected
            print("Not connected to the database")
            # Return None if not connected
            return None
    
    # Upload a pandas dataframe to the database
    def upload(self, df, table_name):
        if self.conn:
            try:
                # Convert the dataframe to a SQL table
                df.to_sql(table_name, self.conn, if_exists="replace", index=False)
                # Return True if successful
                return True
            except Exception as e:
                # Print the error message
                print(f"Error uploading dataframe: {e}")
                # Return False if failed
                return False
        else:
            # Print a message if not connected
            print("Not connected to the database")
            # Return False if not connected
            return False