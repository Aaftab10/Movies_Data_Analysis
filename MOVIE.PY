import pandas as pd
import sqlite3

# Read CSV
movies = pd.read_csv("dataset/movies.csv")

# Create Database
conn = sqlite3.connect("database/movies.sqlite")

# Save DataFrame as SQL Table
movies.to_sql("movies", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("Database Created Successfully!")