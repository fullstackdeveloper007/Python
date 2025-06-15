# 📊 Pandas API Reference which are used in below


| #  | Pandas API                   | Description                                                                 |
|----|------------------------------|-----------------------------------------------------------------------------|
| 1  | `pd.read_csv()`              | Read a CSV file into a DataFrame                                           |
| 2  | `skiprows`, `header`        | Skip initial rows / specify header row during CSV read                     |
| 3  | `names`                     | Set custom column names while reading CSV                                  |
| 4  | `nrows`                     | Read a limited number of rows from CSV                                     |
| 5  | `na_values`                 | Replace specific values with `NaN` during import                           |
| 6  | `df['column']`              | Access / create DataFrame column                                           |
| 7  | `df.to_csv()`               | Write DataFrame to a CSV file                                              |
| 8  | `index`, `header` params    | Control inclusion of index/header in file write                            |
| 9  | `pd.read_excel()`           | Read an Excel file into a DataFrame                                        |
| 10 | `sheet_name`                | Choose sheet to read from Excel                                            |
| 11 | `converters`                | Use a function to convert values while reading Excel                       |
| 12 | `df.head()`                 | View top N rows of a DataFrame                                             |
| 13 | `pd.merge()`                | Merge two DataFrames                                                       |
| 14 | `df.to_excel()`             | Export DataFrame to Excel                                                  |
| 15 | `pd.ExcelWriter()`          | Export multiple sheets to a single Excel file                              |
| 16 | `pd.DataFrame()`            | Create a DataFrame from dictionary                                         |

---

## 🐼 Pandas Examples with Explanations

```python
import pandas as pd

# Read CSV skipping first row
print(pd.read_csv('C:\\DevApplications\\Temp\\Learning\\Python\\PythonPractice\\pandas\\stock_data.csv', skiprows=1))

# Read CSV using a specific header row
pd.read_csv('C:\\DevApplications\\Temp\\Learning\\Python\\PythonPractice\\pandas\\stock_data.csv', header=1)

# Use custom column names
pd.read_csv('C:\\DevApplications\\Temp\\Learning\\Python\\PythonPractice\\pandas\\stock_data.csv',
            header=1, names=['StockSymbol', 'eps', 'revenue', 'Price', 'People'])

# Read limited rows
pd.read_csv('C:\\DevApplications\\Temp\\Learning\\Python\\PythonPractice\\pandas\\stock_data.csv',
            header=1, nrows=4)

# Replace specific strings with NaN by column
pd.read_csv('C:\\stock_data.csv', header=1, na_values={
    'eps': ['not available'],
    'revenue': ['-1'],
    'People': ['not available', 'n.a']
})

# Replace common NaN values across all columns
df = pd.read_csv('C:\\stock_data.csv', header=1,
                 na_values=['not available', 'n.a.', '-1'])

# Add a calculated column
df['pe'] = df['price'] / df['eps']

# Save DataFrame to CSV
df.to_csv('pe.csv')

# Save CSV without index
df.to_csv('pe1.csv', index=False)

# Save CSV without header or index
df.to_csv('pe1.csv', index=False, header=False)

# Install required Excel package if not done already
# pip install openpyxl

# Converter function for Excel import
def standard_Currency(curr):
    if curr == "$$" or curr == "Dollars":
        return "USD"
    else:
        return curr

# Read Excel file and convert currency
df_financials = pd.read_excel(
    r'C:\\DevApplications\\Temp\\Learning\\Python\\PythonPractice\\pandas\\movies_db.xlsx',
    sheet_name='financials',
    converters={'currency': standard_Currency}
)

# Show top rows
df_financials.head(5)

# Read another CSV file
df_movies = pd.read_csv("movies.csv")

# Merge the two DataFrames
df_merged = pd.merge(df_movies, df_financials, on='movie_id', how='inner')

# Export merged DataFrame to Excel
df_merged.to_excel("merged_movies.xlsx", sheet_name="Sheet1", index=False)

# Create sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df_details = pd.DataFrame(data)

# Second sample DataFrame
data2 = {
    'Name': ['Alice', 'Bob', 'David'],
    'Salary': [50000, 60000, 70000]
}

# Export both to different sheets in same Excel file
with pd.ExcelWriter('multiple_sheets.xlsx') as writer:
    df_details.to_excel(writer, sheet_name='Details', index=False)
    pd.DataFrame(data2).to_excel(writer, sheet_name='Salaries', index=False)
