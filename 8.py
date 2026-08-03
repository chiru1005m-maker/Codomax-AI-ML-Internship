import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

print("--- Day 8: Building the Machine Learning Model ---")
print("Focus: Training a Linear Regression Algorithm\n")

print("Loading 'cleaned_scores.csv' and splitting data...")
df = pd.read_csv('cleaned_scores.csv')
X = df[['Study_Hours']]
y = df['Score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Initializing the Linear Regression model...")
model = LinearRegression()

print("Training the model on the 80% training dataset...")
model.fit(X_train, y_train)

print("\n[SUCCESS] Linear Regression model trained perfectly!")

weight = model.coef_[0]
bias = model.intercept_

print("\n--- Model Parameters (The Math Behind the ML) ---")
print(f"Coefficient (Weight / m): {weight:.2f}")
print(f"Intercept (Bias / c):     {bias:.2f}")

print("\n--- Interpretation of Results ---")
print(f"-> Base Score: If a student studies for 0 hours, the model predicts a baseline score of {bias:.2f}.")
print(f"-> Impact per Hour: For every additional 1 hour of studying, the score is predicted to increase by {weight:.2f} points.")
print(f"-> Model Equation: Predicted_Score = ({weight:.2f} * Study_Hours) + {bias:.2f}")
