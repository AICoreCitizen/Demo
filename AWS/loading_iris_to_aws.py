from sqlalchemy import create_engine

# Connect to PostgreSQL Amazon RDS with psycopg2
# Database connection details
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = "first-database.cuewdxmg0moe.eu-west-1.rds.amazonaws.com"
USER = 'postgres'
PASSWORD = "Kenshin1ce"
PORT = 5432
DATABASE = 'testnumberone'
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")

engine.connect()


# Load the iris Dataset
# !pip install scikit-learn
# !pip install pandas

from sklearn.datasets import load_iris
import pandas as pd
data = load_iris()
iris = pd.DataFrame(data['data'], columns=data['feature_names'])
iris.head()

# Insert Data into the Database
# Using the to_sql() Pandas method, you can insert the data from the DataFrame into a table named iris_dataset in your PostgreSQL Amazon RDS instance.
iris.to_sql('iris_dataset', engine, if_exists='replace')

# NOTE: Unfortunately, AWS RDS does not allow you to view the tables you created. However, you can still access them using pgAdmin or SQLAlchemy.
df = pd.read_sql_table('iris_dataset', engine)
df.head()
