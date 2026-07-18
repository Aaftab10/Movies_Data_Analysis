# 🎬 Movie Data Analysis using Python, SQL & SQLite

## 📌 Project Overview

This project analyzes IMDb Top 1000 Movies using Python, Pandas, SQLite, SQL, and Matplotlib. The CSV dataset is converted into a SQLite database, and SQL queries are used to extract meaningful insights. Visualizations are created to better understand movie trends and ratings.


## Features

- Read movie dataset using Pandas
- Convert CSV dataset into SQLite database
- Execute SQL queries for analysis
- Data cleaning and preprocessing
- Filter movies based on ratings and release year
- Analyze directors and movie counts
- Visualize data using Matplotlib
- Build a simple analytics dashboard



## Technologies Used

- Python 3
- Pandas
- SQLite
- SQL
- Matplotlib


## Project Structure

```
Movie_Data_Analysis/
│
├── dataset/
│   └── movies.csv
│
├── database/
│   └── movies.sqlite
│
├── create_database.py
├── movie_analysis.py
├── data_analysis.py
├── data_cleaning.py
├── filter_data.py
├── visualization.py
├── dashboard.py
├── final_dashboard.py
├── requirements.txt
└── README.md
```

## Dataset Information

- **Dataset:** IMDb Top 1000 Movies
- **Rows:** 1000
- **Columns:** 16

Main Columns:

- Series_Title
- Released_Year
- Genre
- Director
- IMDB_Rating
- Gross
- No_of_Votes
- Runtime
- Meta_score


## SQL Analysis Performed

- Total Movies
- Top Rated Movies
- Movies Released Per Year
- Top Directors
- Highest Gross Movies
- Average IMDb Rating
- Movie Count by Director



## Visualizations

- Bar Chart
- Line Chart
- Histogram
- Dashboard with Multiple Charts



## ▶Installation

Clone the repository

```bash
git clone https://github.com/aaftab10/Movie_Data_Analysis.git
```

Move into the project directory

```bash
cd Movie_Data_Analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```


## Run the Project

### Step 1

Create SQLite Database

```bash
python create_database.py
```

### Step 2

Run Movie Analysis

```bash
python movie_analysis.py
```

### Step 3

Run Dashboard

```bash
python final_dashboard.py
```

---

## Skills Demonstrated

- Python Programming
- Pandas Data Analysis
- SQLite Database
- SQL Queries
- Data Cleaning
- Data Visualization
- Dashboard Development

---

## Future Improvements

- Interactive Dashboard using Streamlit
- Power BI Dashboard
- PostgreSQL Integration
- Advanced Data Analytics
- Machine Learning based Movie Rating Prediction

---

## Author

Aaftab Husain

LinkedIn: https://linkedin.com/in/aaftab.07

GitHub: https://github.com/aaftab10