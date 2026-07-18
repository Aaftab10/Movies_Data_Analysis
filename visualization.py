import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("database/movies.sqlite")

# SQL Query
query = """
SELECT Series_Title, IMDB_Rating
FROM movies
ORDER BY IMDB_Rating DESC
LIMIT 10;
"""

# Read SQL into DataFrame
df = pd.read_sql(query, conn)

# Close database connection
conn.close()

# Create Bar Chart
plt.figure(figsize=(12,6))
plt.bar(df["Series_Title"], df["IMDB_Rating"])

plt.title("Top 10 Highest Rated Movies")
plt.xlabel("Movie Name")
plt.ylabel("IMDb Rating")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()