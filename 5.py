import pandas as pd

print("--- Day 5: Data Cleaning Task ---")

df = pd.read_csv('student_scores.csv')
print(f"Original Data Shape: {df.shape}")

null_count = df.isnull().sum().sum()
print(f"Missing values found: {null_count}")

if null_count > 0:
    df.dropna(inplace=True)
    print("-> Dropped rows with missing values.")

dup_count = df.duplicated().sum()
print(f"Duplicate rows found: {dup_count}")

if dup_count > 0:
    df.drop_duplicates(inplace=True)
    print("-> Dropped duplicate rows.")

df.reset_index(drop=True, inplace=True)

print(f"\nFinal Cleaned Data Shape: {df.shape}")

df.to_csv('cleaned_scores.csv', index=False)
print("Saved clean data to 'cleaned_scores.csv'")

print("\n--- Cleaned Data Stats ---")
print(df.describe())
