import numpy as np
student_matrix = np.array([
    [4.5, 85.0, 78.0],
    [2.0, 60.5, 55.0],
    [8.5, 95.0, 92.0],
    [6.0, 88.0, 81.0],
    [3.5, 75.0, 65.0],
    [9.0, 98.0, 88.5]
])

print("--- Original 2D Student Matrix ---")
print(student_matrix)

study_hours = student_matrix[:, 0]
attendance = student_matrix[:, 1]
previous_scores = student_matrix[:, 2]

print("\n--- Array Slicing ---")
print(f"Study Hours Vector: {study_hours}")

calculated_scores = previous_scores + (study_hours * 2.5) + (attendance * 0.15)

final_scores = np.clip(calculated_scores, 0, 100)

print("\n--- Vectorized Calculations ---")
print(f"Calculated Final Scores: {np.round(final_scores, 2)}")

mean_score = np.mean(final_scores)
std_dev = np.std(final_scores)

print("\n--- Descriptive Statistics ---")
print(f"Mean Class Score: {mean_score:.2f}")
print(f"Score Standard Deviation: {std_dev:.2f}")

top_performers_mask = final_scores > 85.0
top_scores = final_scores[top_performers_mask]

print("\n--- Boolean Indexing (Filtering) ---")
print(f"Mask array for scores > 85: {top_performers_mask}")
print(f"Filtered Top Scores: {np.round(top_scores, 2)}")
