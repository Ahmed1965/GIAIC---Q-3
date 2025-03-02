import streamlit as st  
import pandas as pd
import numpy as np
import os
from os import path
import seaborn as sns
import io 


# setting up page config

st.set_page_config(page_title="Titanic Data Analysis", page_icon=":ship:", layout="wide")
st.title("Titanic Data Analysis")
st.write(f"Titanic was met an accident that occurred in 1912. It was a shipwreck that killed 1502 people and 750 were saved. This app is a data analysis of the Titanic data (1912) to see if it was a good or bad ship, ")

# Load the data
titanic_df = pd.read_csv("train.csv")

# Reading Data
#titanic_df = pd.read_csv("titanic.csv")

# display first 10 rows of  data
st.subheader("Displaying first 10 rows of data")

st.write(titanic_df.head(10))    

# display last 10 rows of  data
st.subheader("Displaying last 10 rows of data")

st.write(titanic_df.tail(10))

# shape of data
st.subheader("Shape of data")
st.write("Shape of data shows that there is 891 rows and 12 columns: ")

st.write(titanic_df.shape)
st.subheader("Data Overview")
buffer = io.StringIO()
titanic_df.info(buf=buffer) 
st.text(buffer.getvalue())

st.subheader("Data Description")
st.write(titanic_df.describe())
st.write(titanic_df.describe(include="object"))

st.subheader("Data Columns")
st.write(titanic_df.columns)

st.subheader("checking null and duplicate values")
null_values = titanic_df.isnull().sum()
st.write(null_values[null_values > 0])

st.subheader("Since Cabin has no value in dataset thereby it may be dropped")
titanic_df.drop("Cabin", axis=1, inplace=True)
st.write(titanic_df.describe(include="object"))
st.subheader("Converting numerical data into percentage")

# Converting numerical data into percentage
percentage=titanic_df.isnull().sum()/len(titanic_df)*100
st.write(percentage[percentage>0])

# checking Duplicates
st.subheader("Checking Duplicates")
st.write(titanic_df.duplicated().sum())

st.write("Since there is no duplicate values in the dataset, we can now handle missing values")

# handling missing values
st.subheader("Handling Missing Values")
titanic_df["Age"].fillna(titanic_df["Age"].mean(), inplace=True)
titanic_df["Embarked"].fillna(titanic_df["Embarked"].mode()[0], inplace=True)
titanic_df["Fare"].fillna(titanic_df["Fare"].median(), inplace=True)
st.write(titanic_df.isnull().sum())

st.title("Data Visualization")
st.subheader("EDA")
# converting columns into lower case

titanic_df.columns = titanic_df.columns.str.lower()
st.write("Converting df columns into lower case")
# creating for loop for unique values

for column in titanic_df.columns:
    unique_values = titanic_df[column].unique()
