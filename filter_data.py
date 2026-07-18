import sqlite3
import pandas as pd

conn = sqlite3.connect("database/movies.sqlite")

df = pd.read_sql("SELECT * FROM movies", conn)

conn.close()

print("Movies with Rating >= 9")

high_rating = df[df["IMDB_Rating"] >= 9]

print(high_rating[["Series_Title","IMDB_Rating"]])