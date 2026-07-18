import sqlite3
import pandas as pd

conn = sqlite3.connect("database/movies.sqlite")

df = pd.read_sql("SELECT * FROM movies", conn)

conn.close()

print("Missing Values:")
print(df.isnull().sum())

# Remove rows with missing Gross value
df = df.dropna(subset=["Gross"])

print("\nShape After Cleaning:")
print(df.shape)

print("\nAny Missing Values?")
print(df.isnull().sum())