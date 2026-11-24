import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("customer_churn.csv")

# Step 2: Display first five records
print("First five records:")
print(df.head())

# Step 3: Display dataset information
print("\nDataset Information:")
print(df.info())

# Step 4: Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Step 5: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 6: Handle missing values
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Step 7: Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Step 8: Calculate Mean, Median and Mode
print("\nMean:")
print(df.select_dtypes(include=np.number).mean())

print("\nMedian:")
print(df.select_dtypes(include=np.number).median())

print("\nMode:")
print(df.mode().iloc[0])

# Step 9: Visualize numerical data using histogram
df.select_dtypes(include=np.number).hist(figsize=(12, 8))
plt.tight_layout()
plt.show()

# Step 10: Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include=np.number).corr(),
            annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Step 11: Detect Outliers using Boxplot
for col in df.select_dtypes(include=np.number).columns:
    plt.figure(figsize=(6, 3))
    sns.boxplot(x=df[col])
    plt.title("Outliers in " + col)
    plt.show()

# Step 12: Handle Outliers using IQR
for col in df.select_dtypes(include=np.number).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[col] = df[col].clip(lower, upper)

# Step 13: Customer Churn Visualization
if 'Churn' in df.columns:
    sns.countplot(x='Churn', data=df)
    plt.title("Customer Churn Distribution")
    plt.show()

# Step 14: Final cleaned dataset
print("\nFinal Cleaned Dataset:")
print(df.head())

print("\nEDA Completed Successfully!")