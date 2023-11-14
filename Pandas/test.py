# %%
import pandas as pd
import numpy as np

# From the data documentatiobn:
names = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
auto_df = pd.read_csv("imports-85.data", header=None, names=names)
auto_df
# %%
auto_df.info()
# %%
# Let's look at missing values for stroke
np.sort(auto_df["stroke"].unique())
# %%
print("Unique values in price:", np.sort(auto_df["price"].unique()))
print("Unique values in normalized losses:", np.sort(auto_df["normalized-losses"].unique()))
# %%
auto_df = pd.read_csv("imports-85.data", header=None, names=names, na_values="?")
auto_df.info()
# %%
pima_df = pd.read_csv("datasets_228_482_diabetes.csv")
print(pima_df.info())
pima_df
# %%
pima_df.describe()
# %%
questionable_columns = ["BloodPressure", "Glucose", "SkinThickness", "Insulin", "BMI"]
zero_counts = {col: 0 for col in questionable_columns}
for col in questionable_columns:
    zero_counts[col] = pima_df[col][pima_df[col] == 0].count()

print(zero_counts)
# %%
import plotly.express as px
fig = px.histogram(pima_df, "BloodPressure")
fig.show()
# %%
pima_df[questionable_columns] = pima_df[questionable_columns].replace(0, np.nan)
# %%
print(pima_df.info())
# %%
auto_df_null = auto_df.isnull() # .isna() is the same as .isnull()
auto_df_null
# %%
auto_df_null.sum()
# %%
## Using one line only, work out the total percentage of missing values from the pima dataframe
pima_df.isnull().mean()*100
# %%
!pip install missingno
# %%
import missingno as msno

msno.matrix(auto_df)
# %%
