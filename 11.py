import pandas as pd
import numpy as np

# 1. Create a Pandas Series with 10 random numbers
data = np.random.randint(1, 100, 10)
s = pd.Series(data)

print("Pandas Series:")
print(s)

# 2. Access elements using indexing
print("\nFirst Element:", s[0])
print("Third Element:", s[2])

# 3. Create a DataFrame
df = pd.DataFrame({
    'Name': ['Amit', 'Riya', 'Rahul', 'Priya', 'Neha'],
    'Age': [20, 21, 19, 22, 20],
    'Marks': [85, 90, np.nan, 75, 95]
})

print("\nOriginal DataFrame:")
print(df)

# 4. Access DataFrame columns
print("\nNames:")
print(df['Name'])

# 5. Data Cleaning
print("\nDataFrame after filling missing values:")
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
print(df)

# 6. Filtering data
print("\nStudents having marks greater than 80:")
print(df[df['Marks'] > 80])

# 7. Create another DataFrame
df2 = pd.DataFrame({
    'Name': ['Amit', 'Riya', 'Rahul', 'Priya', 'Neha'],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Nashik']
})

# 8. Merge two DataFrames
merged = pd.merge(df, df2, on='Name')

print("\nMerged DataFrame:")
print(merged)

# 9. Aggregation
print("\nAverage Marks:", df['Marks'].mean())
print("Maximum Marks:", df['Marks'].max())
print("Minimum Marks:", df['Marks'].min())
print("Total Marks:", df['Marks'].sum())

# 10. Grouping and aggregation
print("\nAverage Marks by Age:")
print(df.groupby('Age')['Marks'].mean())