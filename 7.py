import pandas as pd
from sklearn.model_selection import train_test_split

print("--- Day 7: Machine Learning Basics ---")
print("Focus: Supervised Learning & Train-Test Split\n")

df = pd.read_csv('cleaned_scores.csv')
print(f"Total Dataset Size: {df.shape[0]} records")

X = df[['Study_Hours']] 
y = df['Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\n--- Split Results ---")
print(f"Training Data (X_train, y_train): {X_train.shape[0]} samples ({len(X_train)/len(df)*100:.0f}%)")
print(f"Testing Data (X_test, y_test): {X_test.shape[0]} samples ({len(X_test)/len(df)*100:.0f}%)")

print("\n--- Distribution Verification ---")
print("Average Study Hours:")
print(f"  -> Full Dataset: {X['Study_Hours'].mean():.2f}")
print(f"  -> Training Set: {X_train['Study_Hours'].mean():.2f}")
print(f"  -> Testing Set:  {X_test['Study_Hours'].mean():.2f}")

print("\nAverage Scores:")
print(f"  -> Full Dataset: {y.mean():.2f}")
print(f"  -> Training Set: {y_train.mean():.2f}")
print(f"  -> Testing Set:  {y_test.mean():.2f}")

print("\nStatus: Data is prepped. Ready to build the Linear Regression model on Day 8!")
