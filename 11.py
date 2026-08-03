import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import warnings

# Suppress the feature name warning for clean terminal output
warnings.filterwarnings("ignore", category=UserWarning)

def train_model():
    """Loads the clean data and returns a trained Linear Regression model."""
    try:
        df = pd.read_csv('cleaned_scores.csv')
        X = df[['Study_Hours']]
        y = df['Score']
        
        model = LinearRegression()
        model.fit(X, y)
        return model
    except FileNotFoundError:
        print("[ERROR] 'cleaned_scores.csv' not found. Please run the Day 5 cleaning script first.")
        return None

def main():
    print("="*40)
    print(" STUDENT SCORE PREDICTOR APP ")
    print("="*40)
    
    model = train_model()
    if model is None:
        return

    print("Model loaded successfully! Ready for predictions.\n")
    print("Type 'quit' or 'exit' at any time to stop the program.\n")

    while True:
        user_input = input("Enter the number of study hours: ")
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit']:
            print("\nExiting the predictor. Have a great day!")
            break
            
        try:
            # Convert input to float and predict
            hours = float(user_input)
            if hours < 0:
                print("-> Please enter a positive number for study hours.\n")
                continue
                
            prediction = model.predict(pd.DataFrame({'Study_Hours': [hours]}))
            
            # Cap the score at 100%
            final_score = min(prediction[0], 100.0)
            
            print(f"-> Predicted Score: {final_score:.2f} points\n")
            
        except ValueError:
            print("-> [INVALID INPUT] Please enter a valid number (e.g., 5.5).\n")

if __name__ == "__main__":
    main()
