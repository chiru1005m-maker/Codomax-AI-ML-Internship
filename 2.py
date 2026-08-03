# Variables and Data Types
study_hours = 4.5
student_name = "Alex"

# Function and Loop
def calculate_weekly_hours(daily_hours, days_studied):
    total = 0
    for i in range(days_studied):
        total += daily_hours
    return total

weekly_total = calculate_weekly_hours(study_hours, 5)
print(f"{student_name} studied {weekly_total} hours this week.")
