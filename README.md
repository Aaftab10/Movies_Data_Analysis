# 🎬 Movie Data Analysis & Power BI Dashboard

An end-to-end movie data analysis project using Python, Pandas, SQLite, SQL, Matplotlib, and Power BI.

## 📌 Project Overview

This project analyzes the IMDb Top 1000 Movies dataset to explore movie ratings, genres, directors, release years, runtime, and gross revenue.

The project combines Python-based data analysis with an interactive Power BI dashboard to turn raw movie data into meaningful insights.

## Features

- Read movie dataset using Pandas
- Convert CSV dataset into SQLite database
- Execute SQL queries for analysis
- Data cleaning and preprocessing
- Filter movies based on ratings and release year
- Analyze directors and movie counts
- Visualize data using Matplotlib
- Build a simple analytics dashboard
- Create Power BI Dashboard



## Technologies Used

- Python 
- Pandas
- SQLite
- SQL
- Matplotlib
- Power BI Desktop
- Power Query
- DAX


## Project Structure

```
Movie_Data_Analysis/
│
├── dataset/
│   └── movies.csv
│
├── database/
│   └── movies.sqlite
├── powerbi/powerbi report
│   └── Movies_Analytics_Dashboard.pbix and jpg file
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

## Power BI Dashboard
The interactive dashboard that include

- Total Movies
- Top Rated Movies
- Movies Released by Year
- Total Directors
- Highest-rated Movies
- Average IMDb Rating
- Average runtime
- Movies Count by Genre
- Movies by Certeficate
- Top 10 director by movie count
- Release Year and Genre Slicer
- Reset Filters button using bookmarks

## Dashboard Preview
  Uploaded a clean Dashboard for preview
  [powerbi/Movies_Analytics_Dashboard.jpg](https://github.com/Aaftab10/Movies_Data_Analysis/blob/main/powerbi/Movies_Analytics_Dashboard.jpg))

---

## Skills Demonstrated

- Python Programming
- Pandas Data Analysis
- SQLite Database
- SQL Queries
- Data Cleaning
- Data Visualization
- Power BI Dashboard Development
- Data Storytelling

---

## Future Improvements

- Interactive Dashboard using Streamlit
- PostgreSQL Integration
- Advanced Data Analytics
- Machine Learning based Movie Rating Prediction

---

## Author

Aaftab Husain

LinkedIn: https://linkedin.com/in/aaftab.07

GitHub: https://github.com/aaftab10
