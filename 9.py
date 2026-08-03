import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

print("--- Day 9: Generating Model Predictions ---")
print("Focus: Testing the model on unseen data\n")

df = pd.read_csv('cleaned_scores.csv')
X_train, X_test, y_train, y_test = train_test_split(df[['Study_Hours']], df['Score'], test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
print("Model successfully trained on the training set.")

print("Running predictions on the test dataset...\n")
y_pred = model.predict(X_test)

predictions_df = pd.DataFrame({
    'Study Hours': X_test['Study_Hours'].values,
    'Actual Score': y_test.values,
    'Predicted Score': np.round(y_pred, 1) 
})

predictions_df['Difference (Error)'] = np.round(np.abs(predictions_df['Actual Score'] - predictions_df['Predicted Score']), 1)

print("--- Actual vs. Predicted Scores ---")
print(predictions_df.to_string(index=False)) 

print("\n--- Real-World Scenario Test ---")
sample_hours = 7.5

custom_prediction = model.predict([[sample_hours]])

print(f"Question: What if a student studies for {sample_hours} hours?")
print(f"Answer:   The model predicts they will score roughly {custom_prediction[0]:.1f} points.")
