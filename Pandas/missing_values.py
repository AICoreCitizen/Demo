# %%
#Import Python Modules
import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from plotly.subplots import make_subplots
# %%
# From the data documentatiobn:
names = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
auto_df = pd.read_csv("imports-85.data", header=None, names=names)
auto_df
# %%
# Describe Data
auto_df.info()
# %%
# Let's look at missing values for stroke
np.sort(auto_df["stroke"].unique())
# %%
# see a "?" which is an indication of a missing value. Check a couple of other columns to ensure this value is consistent throughout the dataframe.
print("Unique values in price:", np.sort(auto_df["price"].unique()))
print("Unique values in normalized losses:", np.sort(auto_df["normalized-losses"].unique()))
# %%
# From the result of the .info() method above, note that although we would expect stroke to be of type float, Pandas is indicating to us that it is of type object. 
#The na_values flag looks at the string we've provided as the argument, and replaces that string with a nan value.

auto_df = pd.read_csv("imports-85.data", header=None, names=names, na_values="?")
auto_df.info()
# %%
# stroke, and some other columns have been converted to correct datatypes.
#  Recently they have introduced the Int64 (capital I) type which does have support for a first party null type: pd.NA. You can read more here: https://pandas.pydata.org/pandas-docs/stable/user_guide/integer_na.html
pima_df = pd.read_csv("datasets_228_482_diabetes.csv")
print(pima_df.info())
pima_df
# %%
# Describe data
pima_df.describe()
# %% [markdown]

# Is there any row which particularly stands out to you as questionable?

# The min row is particularly interesting because many of the values there are 0. 
# Do you know any alive person who has a BloodPressure of 0? Or Glucose, SkinThickness, Insulin or BMI for that matter. 
# It is obviously possible to have 0 Pregnancies though, so that value of 0 could be considered correct. 
# For the questionable columns we identified, let's check how many 0 values are present.

# %%
questionable_columns = ["BloodPressure", "Glucose", "SkinThickness", "Insulin", "BMI"]
# This line creates a list called questionable_columns containing the names of certain columns in a DataFrame. These columns are "BloodPressure," "Glucose," "SkinThickness," "Insulin," and "BMI."
zero_counts = {col: 0 for col in questionable_columns}
# This line creates a dictionary called zero_counts with column names from questionable_columns as keys, and initializes each key with a value of 0. This dictionary will be used to store the count of zero values for each column.
for col in questionable_columns:
    zero_counts[col] = pima_df[col][pima_df[col] == 0].count()
# Here, a for loop iterates through each column name in questionable_columns. For each column, it calculates the count of zero values in that column using boolean indexing (pima_df[col] == 0) and then counting the number of True values with .count(). The result is stored in the corresponding key in the zero_counts dictionary.
print(zero_counts)
# Finally, it prints the zero_counts dictionary, which now contains the count of zero values for each of the specified columns in the DataFrame pima_df.
# %% [markdown]
# If we had performed visualisation on our data, identifying this would have been easier. 
# Let's plot a histogram (which will be formally introduced later) and use BloodPressure as an example. 
# Note that Plotly Express handles a LOT of things under the hood - and 'binning' float values is one of these things. 
# We need to keep such things in mind when using high level libraries as otherwise we may make incorrect assumptions about our data

# %%

fig = px.histogram(pima_df, "BloodPressure")
fig.show()
# %% [markdown]
# we can't pass "0" as an argument to na_values .read_csv() like we did previously 
# because some of our 0 values are legitimate. 
# Instead, we'll have to 'manually' replace these values with np.nan
pima_df[questionable_columns] = pima_df[questionable_columns].replace(0, np.nan)

# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

# %%
print(pima_df.info())

# %% [markdown]
### The amount of missingness
# It can be valuable to know how much of our data is actually missing - in terms of absolute values or percentages. 
# Doing so is a relatively straightforward process which I will demonstrate on our auto_df.
# %%
auto_df_null = auto_df.isnull() # .isna() is the same as .isnull()
auto_df_null
# %%
# We've now obtained a dataframe with True/False values - True indicating where there is a missing/null value, and False otherwise. 
# To see the absolute amount of missing values, we can .sum() the dataframe. 
# To obtain the percentages, we can simply do a .mean() * 100

# %%
## Using one line only, work out the total percentage of missing values from the pima dataframe
pima_df.isnull().mean()*100

# %% [markdown]
# Visualising missing Data
# There is a very useful package called missingno which allows us to easily visualise our 
# data and identify rows where our data is missing. Doing this allows you to graphically visualise 
# which rows have missing data, and can help us to determine whether data has gone missing because 
# of a random error or because of something a bit more systematic.

# %%
# missing data for Auto_DF
msno.matrix(auto_df)
# %%

#Missing Data for pima_df
# msno.bar(pima_df)
msno.matrix(pima_df)
# %% [markdown]
# When (and how) to delete data
# There are two types of deletion we can consider:

# Pairwise Deletion
# Listwise Deletion


# %%

### When (and how) to delete data

# There are two types of deletion we can consider:

# 1. Pairwise Deletion
# 2. Listwise Deletion

# **Pairwise deletion** is when missing values are skipped during the calculation of some statistic. This is almost a non-factor with Pandas because when we compute a statistic, missing values aren't considered:
print("Mean of Glucose using native mean method:", pima_df["Glucose"].mean())
print("Mean of Glucose via manual calculation  :", pima_df["Glucose"].sum() / pima_df["Glucose"].count())


# %% [markdown]

# Listwise deletion is when we drop the whole row of data because of a missing value. 
# This is completely valid to do but should only be done when the amount of rows you are dropping is insignificant when compared to the rest of the dataset. 
# From our counts of nullity that we did previously, and working under the knowledge that Glucose and BMI are MCAR, we are safe to drop the rows where these missing values are present.

# %%
## Drop the rows in Glucose and BMI for which there are missing values
pima_clean = pima_df.dropna(subset=["Glucose", "BMI"])
pima_clean.info()
## Plot a missingno matrix of the dataframe
msno.matrix(pima_clean)
plt.show()
# %% [markdown]
### Imputing using averages
# Imputation is the act of predicting the missing data, and can be applied to any of the 
# missing data classifications we are working with. 
# In this section, we will look at imputing data using central tendancy measures. 
# We will show why this may not be a great idea, and then introduce ML imputing techniques. Recall the three types of average: Mean, Median and Mode.

# The values of these types of imputations are trivial to calculate and 
# we could easily do it ourselves if we wanted to. 
# However, for the sake of introducing you to the API, 
# we will be using skleanr's SimpleImputer.
# %%
pima_cols = pima_df.columns
pima_cols
# %%
mode_imputer = SimpleImputer(strategy="most_frequent")
pima_mode_arr = mode_imputer.fit_transform(pima_df)
pima_mode_df = pd.DataFrame(data=pima_mode_arr, columns=pima_cols)
pima_mode_df
# %%
## Impute and assign dataframes for strategies of mean and median
median_imputer = SimpleImputer(strategy="median")
pima_median_arr = median_imputer.fit_transform(pima_df)
pima_median_df = pd.DataFrame(data=pima_median_arr, columns=pima_cols)
pima_median_df 
# %%
### Your Code Here, do the same using the mean strategy
mean_imputer = SimpleImputer(strategy="mean")
pima_mean_arr = mean_imputer.fit_transform(pima_df)
pima_mean_df = pd.DataFrame(data=pima_mean_arr, columns=pima_cols)
pima_mean_df 
# %% [markdown]
# So why is this bad?
# Central tendancy imputations should be avoided because they reduce the variance of the data, leading to a higher bias in the data. 
# Perhaps more intuitively, these types of imputations will not consider any of the other variable relationships in your data. 
# We can easily see this with visualisations
# %%
nulls = (pima_df["SkinThickness"].isnull() + pima_df["BMI"].isnull()).astype("int")
px.scatter(pima_mean_df, x="SkinThickness", y="BMI", title="SkinThickness vs BMI (Mean Imputation)",
           color=nulls)
# %%
# Visualising the different imputations through subplots


fig_mean = px.scatter(pima_mean_df, x="SkinThickness", y="BMI", color=nulls)

fig_median = px.scatter(pima_median_df, x="SkinThickness", y="BMI", color=nulls)

fig_mode = px.scatter(pima_mode_df, x="SkinThickness", y="BMI", color=nulls)

fig = make_subplots(rows=1, cols=3, shared_xaxes=False, subplot_titles=("Mean Imputation","Median Imputation", "Mode Imputation"))
fig.add_trace(fig_mean['data'][0], row=1, col=1)
fig.add_trace(fig_median['data'][0], row=1, col=2)
fig.add_trace(fig_mode['data'][0], row=1, col=3)
fig.update_layout(title="SkinThickness vs BMI (Imputations)")
fig.show()
# %%[markdown]

### ML based imputation techniques
# The alternative to using central tendencies or constant values for imputations is to use ML based imputation methods. We will cover three types algorithms here which have popular use: Nearest neighbours imputation, tree based imputation and regression based imputation. These methods work by building models for a feature based on the other features of the data.

# We'll start with KNN imputation. Here, the algorithm selects the K nearest/most similar datapoints to a datapoint with a missing value. The missing value is then either populated with an average from the K neighbours, or a weighted average. This argument can be specified by weights flag in sklearn's KNNImputer class.
# %%
from sklearn.impute import KNNImputer

# default arguments are:
# n_neighbors = 5
# weights = "uniform"
knn_impute = KNNImputer(n_neighbors=3, weights="distance")
pima_knn_arr = knn_impute.fit_transform(pima_df)
pima_knn_df = pd.DataFrame(data=pima_knn_arr, columns=pima_cols)

fig_knn = px.scatter(pima_knn_df, x="SkinThickness", y="BMI", title="SkinThickness vs BMI (KNN Imputation)",
           color=nulls)
fig_knn
# %%
# When researching imputation techniques, one common method you'll come across is something known as MICE - Multivariate Imputation by Chained Equations. 
# This algorithm performs multiple regressions of a random sample of data, and uses the average of these multiple regressions to impute the missing value. 
# With the sklearn API, the appropiate method to use is the IterativeImputer class, passing sample_posterior=True (source)
# IterativeImputer is an experimental feature in sklearn, so we need to enable it prior to using it


regression_impute = IterativeImputer(sample_posterior=True)
pima_regression_arr = regression_impute.fit_transform(pima_df)
pima_regression_df = pd.DataFrame(data=pima_regression_arr, columns=pima_cols)

fig_br = px.scatter(pima_regression_df, x="SkinThickness", y="BMI", title="SkinThickness vs BMI (Regression Imputation)",
           color=nulls)
fig_br
# %%[markdown]
# The IterativeImputer class is highly flexible and allows us to use any estimator object to perform our imputation (instead of just regression). 
# The default estimator that it uses isn't actually vanilla linear regression - it's something known as Bayesian Ridge regression. 
# We won't cover the details here as the important thing to know is that it is just a linear regression variant. 
# If you are curious about a fuller understanding, more details can be found at: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge.

# Another, more recent, trend in imputation is using tree based ensembles. 
# Here we will use the RandomForestRegressor estimator to impute the missing values:
# %%


## Impute the missing values using RandomForestRegressor and IterativeImputer
rf_impute = IterativeImputer(estimator=RandomForestRegressor(), random_state=42)
pima_rf_arr = rf_impute.fit_transform(pima_df)
pima_rf_df = pd.DataFrame(data=pima_rf_arr, columns=pima_cols)

# Create a scatter plot for SkinThickness vs BMI after imputation
fig_rf = px.scatter(pima_rf_df, x="SkinThickness", y="BMI", title="SkinThickness vs BMI (RandomForest Imputation)", color=nulls)
fig_rf

# %%
fig = make_subplots(rows=1, cols=3, shared_xaxes=False, subplot_titles=("KNN Imputation", "BR Regression Imputation", "RF Regression Imputation"))
fig.add_trace(fig_knn['data'][0], row=1, col=1)
fig.add_trace(fig_br['data'][0], row=1, col=2)
fig.add_trace(fig_rf['data'][0], row=1, col=3)
fig.update_layout(title="SkinThickness vs BMI (Regression Imputations)")
fig.show()
# %% [markdown]
# Time Series Imputation
# Time series data referes to data that has been collected over time, with each datapoint being indexed by a sequential datetime. 
# The most typical example is perhaps stock data. Here, we will look at the Beijing PM2.5. 
# In the .read_csv() method, we'll tell Pandas that we want to index on the Date variable

pm_df_org = pd.read_csv("Beijing_PM.csv", index_col="Date", parse_dates=True) # infer_datetime_format=True deprecated


# %%
pm_df = pm_df_org[:400000]
pm_df = pm_df.loc[~pm_df.index.duplicated(keep='last')]
pm_df = pm_df.sort_index(axis=0)
pm_df
# %%
pm_df.isnull().mean()*100
# %%
# Renaming columns so they're easier to refer to
pm_cols = ["city", "country", "season", "pm25", "dew_point", "temperature", "humidity", "pressure", "wind_direction", "wind_speed", "precipitation_hourly", "preciptiation_cum"]
pm_df.columns = pm_cols
pm_df.head()
# %% [markdown]
### Fill missing values
# We will start with the .fillna() method. The .fillna() method does what the name implies - it fills values where there is a NaN. This method has two strategies we can adopt:

# ffill
# bfill
# Which stand for "forward fill" and "backward fill" respectively. If we have a Series with some missing values in it, ffill will replace the NaNs with the last non-NaN value we've come across in the Series - until the next non-NaN value is reached. Backward fill reverses this and fills in the non-NaN values with the next non-NaN value we would observe. Seeing this in action will clarify this description:
# %%
# Let's use a range from 31230 to 31245
pm_ffill_df = pm_df.fillna(method="ffill")
pm_ffill_df["wind_speed"][31230:31245]
# %%
# Apply backward fill now
pm_bfill_df = pm_df.fillna(method="bfill")
pm_bfill_df["wind_speed"][31230:31245]
# %% [markdown]
### Interpolation

# Ok - so this works to fill NA values, but it's not really ideal. (Note that the fillna method has applications outside of time series data). 
# The next level up is the .interpolation() function https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fpandas.pydata.org%2Fpandas-docs%2Fstable%2Freference%2Fapi%2Fpandas.DataFrame.interpolate.html. 
# Interpolation is art of finding a transition from one point to the other. .interpolation() has many useful techniques to interpolate datapoints, but we will focus on the following 3. Refer to the documentation for a more comprehensive list, and the recommended place for when to use the method:

# Linear
# Quadratic
# Nearest
# %% [markdown]
### Linear
# Linear interpolation simply fills values with equidistant points from the first non-NaN value to the next. Visually: 

# It would be trivial to calculate what this 'equidistant' value actually is - we take the first non-NaN value and the following non-NaN value, subtract the two together, and divide it by the number of NaNs between the two points. With the wind_speed data we were looking at, this would be  (2.4−1.3)/6=0.183 .
# %%
pm_linear_df = pm_df.interpolate(method="linear")
pm_linear_df["wind_speed"][31230:31245]
# %%[markdown]
# Nearest
# The nearest strategy is very similar to that of .fillna() in that it fills the values. However, this method simply fills in the NaNs with the closest non-NaN value to the current NaN we're looping over.
# %%
### Apply the nearest method now
pm_nearest_df = pm_df.interpolate(method="nearest")
pm_nearest_df["wind_speed"][31230:31245]
# %% [markdown]
### Quadratic
# Quadratic interpolation attempts to fit a quadratic/parabolic curve between the two non-NaN values. Later in this notebook we will show plots of the different interpolation methods and 
# you'll be able to get a better sense of understanding how and where each of the interpolation methods we are presenting would be useful. 
# We won't be diving into the methodology behind quadratic interpolation, but you can find a brilliant walkthrough here: https://www.youtube.com/watch?v=ifS8LL3qT2g
# %%
# Apply the quadratic strategy now
pm_quad_df = pm_df.interpolate(method="quadratic")
pm_quad_df["wind_speed"][31230:31245]
# %% [markdown]
### Visualising Time-series data

# %%
pm_df["wind_speed"][31230:31245]
# %%
pd.options.plotting.backend = 'plotly'

fig = make_subplots(rows=6, cols=1, shared_xaxes=False, subplot_titles=("None", "Ffill Interpoloation", "Bfill Interpoloation", "Linear Interpoloation", "Nearest Interpoloation", "Quadratic Interpoloation"))

default = pm_df["wind_speed"][31230:31245]

fig_none = default.plot()
fig.add_trace(fig_none["data"][0], row=1, col=1)

figs_list = [pm_ffill_df, pm_bfill_df, pm_linear_df, pm_nearest_df, pm_quad_df]
for i, to_fig in enumerate(figs_list):
    fig_ = to_fig["wind_speed"][31230:31245].plot(color_discrete_sequence=["red"])
    fig_.add_trace(px.line(pm_df["wind_speed"][31230:31245]).data[0])

    fig.add_trace(fig_["data"][0], row=i+2, col=1)
    fig.add_trace(fig_["data"][1], row=i+2, col=1)

fig.update_layout(title="Wind Speed Interpolations", width=np.inf, height=1600, showlegend=False)
fig.update_traces(mode='markers+lines')
fig.show()

# fig = pm_df.interpolate(method="quadratic")["wind_speed"][31230:31245].plot()
# fig.add_trace(px.line(pm_df["wind_speed"][31230:31245], color_discrete_sequence=["red"]).data[0])
# fig.show()
# %% [markdown]
### Imputing Categorical Variables
# A naive approach to impute categorical data is to either use the most frequent/mode method or the .fillna() strategy that we looked at earlier. However, it is possible to impute categorical variables as we would a typical continuous variable. We cannot directly perform the imputation as straightforwardly as before because the categorical variables are usually encoded as strings (and therefore we can not perform any mathematical operations on them). To impute these kinds of variables, we must first encode them them as numeric values. 
# %%
from sklearn.preprocessing import OrdinalEncoder
knn_impute = KNNImputer(n_neighbors=3, weights="distance")

# We will drop city and country because these are categorical variables which have all their values present
# We will keep season even though it has all the values present (just to demonstrate the process over multiple categorical variables)
# We will drop humidity and precipitation_cum as these features are fully NaN
pm_to_impute_cols = ["season", "pm25", "dew_point", "temperature", "pressure", "wind_direction", "wind_speed", "precipitation_hourly"]
pm_to_impute_df = pm_df[pm_to_impute_cols]
cat_cols = ["season", "wind_direction"]

# key: col, value: list of tuples
category_dict_encode = {}
category_dict_decode = {}
for col in cat_cols:
    pm_to_impute_df[col] = pm_to_impute_df[col].astype("category")
    categories = pm_to_impute_df[col].cat.categories

    col_cat_dict = dict(enumerate(categories))
    print("Column, Category dict:", col_cat_dict)
    category_dict_decode[col] = col_cat_dict

    col_cat_dict = {v:k for k,v in col_cat_dict.items()}
    print("Inverted Column, Category dict:", col_cat_dict)
    category_dict_encode[col] = col_cat_dict

print()
print("Category dict ENCODE:", category_dict_encode)
print("Category dict DECODE:", category_dict_decode)
pm_to_impute_df.replace(category_dict_encode, inplace=True)
pm_to_impute_df
# %%
knn_pm_arr = knn_impute.fit_transform(pm_to_impute_df)
knn_pm_df = pd.DataFrame(knn_pm_arr, columns = pm_to_impute_cols)
knn_pm_df[31230:31245]
# %%
for col in cat_cols:
    knn_pm_df[col] = knn_pm_df[col].round()
knn_pm_df.index = pm_df.index
knn_pm_df[31230:31245]
# %%
# In the original dataframe we will only replace the values for the categorical cols we imputed
# We need to map the columns back to their codes
knn_pm_df.replace(category_dict_decode, inplace=True)
knn_pm_df[31230:31245]
# %%
imputed_cols_df = knn_pm_df[cat_cols]
imputed_cols_df
# %%
pm_imputed_df = pm_df.copy(deep=True)
pm_imputed_df.update(knn_pm_df, overwrite=False)
pm_imputed_df[31230:31245]
# %%
nulls = pm_df["wind_speed"][31230:31245].isnull()
print(nulls)

fig = pm_imputed_df["wind_speed"][31230:31245].plot(color_discrete_sequence=["red"])
fig.add_trace(px.line(pm_df["wind_speed"][31230:31245]).data[0])
fig.update_traces(mode='markers+lines')
fig.update_layout(title="Wind Speed Interpolation (KNN Full DF imputation)")
fig["data"][0]["name"] = "Interpolated"
fig["data"][1]["name"] = "Orignal"
fig.show()
# %%
