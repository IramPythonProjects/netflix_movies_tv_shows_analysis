# 🎬 Netflix Data Analysis Using Python

## 📌 Project Overview
This project analyzes real Netflix data to understand content trends,
popular genres, top countries, ratings, and directors.

Netflix is one of the world's largest streaming platforms. This analysis
shows what type of content Netflix focuses on and how its content has
grown over the years.

Dataset contains **8800+ Movies and TV Shows**.

---

## 📁 Dataset
**File Name:** `netflix_titles.csv`  
**Source:** Kaggle - Netflix Shows Dataset

**Columns:**
- show_id
- type - Movie / TV Show
- title
- director
- cast
- country
- date_added
- release_year
- rating
- duration
- listed_in - Genre
- description

---

## 🛠️ Libraries Used
- **Pandas** - For Data Handling and Cleaning
- **NumPy** - For Numerical Calculations
- **Matplotlib** - For Data Visualization
- **Seaborn** - For Beautiful Statistical Graphs

No other library is used.

---

## 📊 Analysis Performed

### 1. Movies vs TV Shows
Found out how many Movies and TV Shows are on Netflix.

### 2. Content Released Per Year
Analyzed content growth from 2000 to 2021. Content increased
rapidly after 2016 and peaked in 2019-2020.

### 3. Top 10 Countries
Found which countries produce the most content for Netflix.
United States is on top.

### 4. Ratings Analysis
Found which ratings are most common. TV-MA and TV-14 are the
most common ratings.

### 5. Top 10 Genres
Found the most popular genres. International Movies, Dramas
and Comedies are most popular.

### 6. Top 10 Directors
Found directors with the most titles on Netflix.

---

## 🔑 Key Insights
- Netflix has more **Movies** than **TV Shows**.
- Maximum content was released between **2017 to 2020**.
- **United States** is the top content producing country.
- **International Movies and Dramas** are the most popular genres.
- **TV-MA** is the most common rating, showing adult audience is the main target.

---

## 🚀 How To Run This Project

### Option 1: Google Colab
1. Open Google Colab
2. Upload `netflix_titles.csv`
3. Copy code from `netflix_analysis.py`
4. Run it - All graphs will appear

### Option 2: VS Code / Jupyter
1. Download this repository
2. Install libraries:
```bash
pip install pandas numpy matplotlib seaborn
