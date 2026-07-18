import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("database/movies.sqlite")

# Read first 5 rows
query = "SELECT * FROM movies LIMIT 5"

df = pd.read_sql(query, conn)

print(df)

conn.close()

""" NOW wrire sql queries to answer the question at the place of query ="..."
1) total movie
SELECT COUNT(*) FROM movies;
--
2)Highest rated movie
#SELECT Series_Title, IMDB_Rating
FROM movies
ORDER BY IMDB_Rating DESC
LIMIT 10; 
--
3)Top director
SELECT Director, COUNT(*)
FROM movies
GROUP BY Director
ORDER BY COUNT(*) DESC;
--
4)Most Common Genres
SELECT Genre, COUNT(*)
FROM movies
GROUP BY Genre
ORDER BY COUNT(*) DESC;
--
5)Highest Grossing Movies
SELECT Series_Title, Gross
FROM movies
ORDER BY Gross DESC
LIMIT 10;
"""
 
