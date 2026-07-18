import sqlite3
import pandas as pd

conn = sqlite3.connect("database/movies.sqlite")

print("=" * 60)
print("🎬 MOVIE DASHBOARD")
print("=" * 60)

# Total Movies
query = "SELECT COUNT(*) AS Total_Movies FROM movies;"
df = pd.read_sql(query, conn)
print("\n📌 Total Movies")
print(df)

# Average Rating
query = """
SELECT ROUND(AVG(IMDB_Rating),2) AS Average_Rating
FROM movies;
"""
df = pd.read_sql(query, conn)
print("\n⭐ Average IMDb Rating")
print(df)

# Highest Rated Movie
query = """
SELECT Series_Title, IMDB_Rating
FROM movies
ORDER BY IMDB_Rating DESC
LIMIT 1;
"""
df = pd.read_sql(query, conn)
print("\n🏆 Highest Rated Movie")
print(df)

# Top 5 Directors
query = """
SELECT Director,
COUNT(*) AS Movies
FROM movies
GROUP BY Director
ORDER BY Movies DESC
LIMIT 5;
"""
df = pd.read_sql(query, conn)
print("\n🎥 Top Directors")
print(df)

conn.close()

print("\nDashboard Completed Successfully!")