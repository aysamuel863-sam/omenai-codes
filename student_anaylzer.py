import numpy as np

# PART 1 - CREATE DATASET

students = np.array([
    [80, 75, 90],
    [65, 70, 60],
    [95, 90, 88],
    [55, 60, 58],
    [85, 80, 92]
])

print("Students scores:")
print(students)

# PART 2 - STUDENT AVERAGES

averages = np.mean(students, axis=1)

print("\nStudent averages:")
print(averages)

# HIGHEST AND LOWEST 

highest_score = np.max(students)
lowest_score = np.min(students)

print(f"\nHighest score: {highest_score}")
print(f"Lowest score: {lowest_score}")

highest_average = np.max(averages)
lowest_average = np.min(averages)

print(f"\nHighest average: {highest_average}")
print(f"Lowest average: {lowest_average}")

# PART 4 - SUBJECT AVERAGES 

subject_averages = np.mean(students, axis=0)

print("\nSubject averages:")
print(subject_averages)

# PART 5 - PASSING STUDENTS

passing_students = averages >= 75

print("\nPassing students:")
print(passing_students)

print("Passing averages:")
print(averages[passing_students])

# PART 6 - CLASS PERFORMANCE

class_average = np.mean(students)

print(f"\nOverall class average: {class_average}")

number_passed = np.sum(passing_students)
print(f"Number of students passed: {number_passed}")

# PART 7 - FINAL ANALYSIS

if class_average >= 75:
    print("Class performance: Good")
else:
    print("Class performance: Need improvement")

best_subject = np.argmax(subject_averages)

print(f"Best subject: Subject {best_subject + 1}")