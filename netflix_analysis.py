# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# STEP 1: LOAD DATASET
df = pd.read_csv('netflix_titles.csv')

print("Dataset Loaded Successfully!")
print(df.head())

# STEP 2: DATA CLEANING

# Remove Duplicate Rows
df.drop_duplicates(inplace=True)

# Fill Missing Values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')

# Convert Date Column into Datetime
df['date_added'] = pd.to_datetime(
    df['date_added'].str.strip(),
    errors='coerce'
)

# Extract Year
df['year_added'] = df['date_added'].dt.year

print("Data Cleaning Done!")

# STEP 3: MOVIES VS TV SHOWS

plt.figure(figsize=(7, 5))

sns.countplot(
    x='type',
    data=df,
    hue='type',
    palette='viridis',
    legend=False
)

plt.title('Movies vs TV Shows on Netflix',
          fontsize=15, fontweight='bold')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

print(df['type'].value_counts())

# STEP 4: CONTENT RELEASED PER YEAR

plt.figure(figsize=(12, 6))

year_count = df['release_year'].value_counts().sort_index()

plt.plot(
    year_count.index,
    year_count.values,
    marker='o',
    color='red',
    linewidth=2
)

plt.title('Content Released Per Year',
          fontsize=15, fontweight='bold')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.xlim(2000, 2021)
plt.grid(True)
plt.tight_layout()
plt.show()

# STEP 5: TOP 10 COUNTRIES

plt.figure(figsize=(10, 6))

top_country = (
    df[df['country'] != 'Unknown']['country']
    .str.split(',')
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
)

sns.barplot(
    x=top_country.values,
    y=top_country.index,
    hue=top_country.index,
    palette='magma',
    legend=False
)

plt.title('Top 10 Countries With Most Content',
          fontsize=15, fontweight='bold')
plt.xlabel('Count')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

# STEP 6: RATINGS ANALYSIS

plt.figure(figsize=(10, 6))

rating_order = df['rating'].value_counts().index

sns.countplot(
    y='rating',
    data=df,
    order=rating_order,
    hue='rating',
    palette='coolwarm',
    legend=False
)

plt.title('Most Common Ratings on Netflix',
          fontsize=15, fontweight='bold')
plt.xlabel('Count')
plt.ylabel('Rating')
plt.tight_layout()
plt.show()

# STEP 7: TOP 10 GENRES

genre_series = df['listed_in'].dropna().str.split(',')

all_genres = []

for genres in genre_series:
    for genre in genres:
        all_genres.append(genre.strip())

genre_series = pd.Series(all_genres)

genre_counts = genre_series.value_counts().head(10)

genre_df = pd.DataFrame({
    'Genre': genre_counts.index,
    'Count': genre_counts.values
})

plt.figure(figsize=(10, 6))

sns.barplot(
    x='Count',
    y='Genre',
    data=genre_df,
    hue='Genre',
    palette='Set2',
    legend=False
)

plt.title('Top 10 Popular Genres on Netflix',
          fontsize=15, fontweight='bold')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.tight_layout()
plt.show()

print(genre_df)

# STEP 8: TOP 10 DIRECTORS

director_series = (
    df[df['director'] != 'Unknown']['director']
    .str.split(',')
    .explode()
    .str.strip()
)

top_director = director_series.value_counts().head(10)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_director.values,
    y=top_director.index,
    hue=top_director.index,
    palette='Blues_r',
    legend=False
)

plt.title('Top 10 Directors With Most Titles',
          fontsize=15, fontweight='bold')
plt.xlabel('Count')
plt.ylabel('Director')
plt.tight_layout()
plt.show()

# STEP 9: FINAL SUMMARY

total_movies = (df['type'] == 'Movie').sum()
total_shows = (df['type'] == 'TV Show').sum()

avg_year = df['release_year'].mean()

print("\n========== FINAL SUMMARY ==========")

print("Total Movies:", total_movies)
print("Total TV Shows:", total_shows)
print("Average Release Year:", round(avg_year, 2))

print("Most Common Country:",
      top_country.index[0] if not top_country.empty else 'Unknown')

print("Most Common Rating:",
      df['rating'].mode().iloc[0] if not df['rating'].mode().empty else 'Unknown')

print("Most Popular Genre:",
      genre_df.iloc[0]['Genre'] if not genre_df.empty else 'Unknown')

print("\nProject Completed Successfully!")