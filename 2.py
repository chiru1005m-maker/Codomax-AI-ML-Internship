def analyze_student_data(student_records):
    """Processes a list of student records to calculate averages and identify top performers."""
    
    total_score = 0
    top_student = ""
    highest_score = -1
    
    for student in student_records:
        name = student["name"]      
        score = student["score"]     
        is_active = student["active"] 
        
        if not is_active:
            continue
            
        total_score += score
        
        if score > highest_score:
            highest_score = score
            top_student = name
            
    active_count = sum(1 for s in student_records if s["active"])
    
    average_score = total_score / active_count if active_count > 0 else 0
    
    return average_score, top_student, highest_score

students = [
    {"name": "Alex", "score": 85.5, "active": True},
    {"name": "Jordan", "score": 92.0, "active": True},
    {"name": "Taylor", "score": 78.5, "active": False},
    {"name": "Morgan", "score": 88.0, "active": True},
    {"name": "Casey", "score": 95.5, "active": True}
]

avg, top_name, top_score = analyze_student_data(students)

print("--- Day 2: Python Basics Execution ---")
print(f"Total Active Students Processed: {sum(1 for s in students if s['active'])}")
print(f"Class Average Score: {avg:.2f}")
print(f"Top Performing Student: {top_name} with a score of {top_score}")
