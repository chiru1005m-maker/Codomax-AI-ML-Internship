import pandas as pd
import numpy as np

mock_data = pd.DataFrame({
    'Study_Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7, np.nan],
    'Score': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25, 85]
})
mock_data.loc[11] = [5.1, 47] 
mock_data.to_csv('student_scores.csv', index=False)

print("Loading dataset 'student_scores.csv'...")
df = pd.read_csv('student_scores.csv')

print("\n" + "="*40)
print(" 📊 DATASET OVERVIEW ")
print("="*40)
print(f"Total Rows (Records): {df.shape[0]}")
print(f"Total Columns (Features): {df.shape[1]}")
print(f"Column Names: {list(df.columns)}")

print("\n" + "="*40)
print(" 🛠️ STRUCTURAL INFORMATION ")
print("="*40)
df.info()

print("\n" + "="*40)
print(" 📈 STATISTICAL SUMMARY ")
print("="*40)
print(df.describe().T) 

print("\n" + "="*40)
print(" ⚠️ DATA QUALITY CHECK (Setting up Day 5) ")
print("="*40)
print("Missing Values per Column:")
print(df.isnull().sum())
print(f"\nTotal Duplicate Rows Detected: {df.duplicated().sum()}")

print("\n" + "="*40)
print(" 🔍 DATA PREVIEW (First 5 Records) ")
print("="*40)
print(df.head())
