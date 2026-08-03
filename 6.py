import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned_scores.csv')

plt.figure(figsize=(15, 4))

# Scatter Plot
plt.subplot(1, 3, 1)
plt.scatter(df['Study_Hours'], df['Score'], color='blue', alpha=0.7)
plt.title('Study Hours vs Score (Scatter)')
plt.xlabel('Hours')
plt.ylabel('Score')

# Bar Chart 
plt.subplot(1, 3, 2)
plt.bar(range(len(df)), df['Score'], color='green', alpha=0.7)
plt.title('Student Scores (Bar)')
plt.xlabel('Student Index')
plt.ylabel('Score')

# Line Chart 
plt.subplot(1, 3, 3)
sorted_df = df.sort_values(by='Study_Hours')
plt.plot(sorted_df['Study_Hours'], sorted_df['Score'], color='red', marker='o')
plt.title('Trend: Hours vs Score (Line)')
plt.xlabel('Hours')
plt.ylabel('Score')

plt.tight_layout()
plt.show()
