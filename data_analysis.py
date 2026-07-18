import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("database/movies.sqlite")

# Read the complete movies table
df = pd.read_sql("SELECT * FROM movies", conn)

conn.close()

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())