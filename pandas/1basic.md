# Pandas DataFrame Operations Example

```python
import pandas as pd

# This will read a CSV file named "movies.csv" into a DataFrame
df = pd.read_csv("movies.csv")

# Display the first few rows of the DataFrame
df.head()
df.head(10)  # Display the first 10 rows
df.tail()    # Display the last few rows
df.tail(10)  # Display the last 10 rows

# Randomly sample rows from the DataFrame
df.sample(5)
df.sample(10)

# Display rows by slicing
df[2:6]  # Index 2 to 5

# Get shape and column names
df.shape
df.columns

# Print the imdb_rating column
print(df["imdb_rating"])
print(df.imdb_rating)  # Dot notation
print(type(df.imdb_rating))  # Series
print(type(df))  # DataFrame

# List available functions/properties
print(dir(df))

# Min, Max, Avg of imdb_rating column
df.imdb_rating.min()
df.imdb_rating.max()
df.imdb_rating.mean()

# Filter by industry
df_b = df[df.industry == "Bollywood"]
df_h = df[df.industry == "Hollywood"]

# Stats for Bollywood
df_b.imdb_rating.min()
df_b.imdb_rating.max()
df_b.imdb_rating.mean()

# Stats for Hollywood
df_h.imdb_rating.min()
df_h.imdb_rating.max()
df_h.imdb_rating.mean()

# Column operations
df.columns
df["Language"].unique()
df.industry.value_counts()

# Select specific columns
df_new = df[["industry", "language"]]
df[["industry", "language"]].head()

# Filter rows by release year
df[df.release_year > 2000]
df[(df.release_year > 2000) & (df.release_year <= 2010)]

# Summary statistics
df.describe()
df.describe(include="all")
df.info()

# Handling nulls
df.isnull()
df[df.imdb_rating == df.imdb_rating.max()]
df[df.imdb_rating == df.imdb_rating.max() | df.imdb_rating == df.imdb_rating.min()]
df[df.imdb_rating.isnull()]
df[df.imdb_rating.isnull() | (df.imdb_rating == df.imdb_rating.max())]

# New calculated columns
df["age3"] = df['release_year'].apply(lambda x: 2023 - x)
df["age3"].head()

df["age1"] = 2023 - df.release_year

df["Profit"] = df.apply(lambda x: x["revenue"] - x["budget"], axis=1)

# Index operations
df.index
df.set_index("title", inplace=True)
df.head(3)

# Access rows by index
df.loc["The Dark Knight"]
df.loc["Pather Panchali"]
df.loc["Pather Panchali", "Doctor Strange"]  # This seems incorrect — likely should be .loc[["Pather Panchali", "Doctor Strange"]]

# Access rows by integer position
df.iloc[0]
df.iloc[0:5]

# Reset index
df.reset_index(inplace=True)
