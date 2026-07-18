import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect Database
conn = sqlite3.connect("database/movies.sqlite")

# -------------------------------
# Top 10 Rated Movies
# -------------------------------
top_movies = pd.read_sql("""
SELECT Series_Title, IMDB_Rating
FROM movies
ORDER BY IMDB_Rating DESC
LIMIT 10;
""", conn)

# -------------------------------
# Top Directors
# -------------------------------
top_directors = pd.read_sql("""
SELECT Director, COUNT(*) AS Movies
FROM movies
GROUP BY Director
ORDER BY Movies DESC
LIMIT 10;
""", conn)

# -------------------------------
# Movies Per Year
# -------------------------------
movies_year = pd.read_sql("""
SELECT Released_Year, COUNT(*) AS Total
FROM movies
GROUP BY Released_Year
ORDER BY Released_Year;
""", conn)

conn.close()

# Create Dashboard
plt.figure(figsize=(15,10))

# -------------------------------
# Chart 1
# -------------------------------
plt.subplot(2,2,1)
plt.bar(top_movies["Series_Title"], top_movies["IMDB_Rating"])
plt.xticks(rotation=90)
plt.title("Top Rated Movies")

# -------------------------------
# Chart 2
# -------------------------------
plt.subplot(2,2,2)
plt.bar(top_directors["Director"], top_directors["Movies"])
plt.xticks(rotation=90)
plt.title("Top Directors")

# -------------------------------
# Chart 3
# -------------------------------
plt.subplot(2,2,3)
plt.plot(movies_year["Released_Year"], movies_year["Total"])
plt.xticks(rotation=90)
plt.title("Movies Released Per Year")

# -------------------------------
# Chart 4
# -------------------------------
plt.subplot(2,2,4)
plt.hist(top_movies["IMDB_Rating"], bins=5)
plt.title("IMDb Rating Distribution")

plt.tight_layout()

plt.show()