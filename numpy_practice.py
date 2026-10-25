import numpy as np

# 1. CREATING ARRAYS
 
numbers = np.array([10, 20, 30, 40, 50])
print("1. Array:")
print(numbers)

# 2. ARRAY DIMENSIONS  

print("\n2. Dimensions:")
print(f"ndim: {numbers.ndim}")
print(f"shape: {numbers.shape}")
print(f"size: {numbers.size}")
print(f"dtype: {numbers.dtype}")

# 3. INDEXING

print("\n3. Indexing:") 
print(f"First: {numbers[0]}")
print(f"Second: {numbers[1]}")
print(f"Last: {numbers[-1]}")

# 4. SLICING

print("\n4. Slicing:")
print(f"First three: {numbers[0:3]}")
print(f"Last three: {numbers[2:5]}")
print(f"Every second value: {numbers[::2]}")

# 5. ARRAY MATH

print("\n5. Array mathematics:")
print(f"Add 5: {numbers + 5}")
print(f"Substract 5: {numbers - 5}")
print(f"Multiply by 2: {numbers * 2}")
print(f"Divide by 2: {numbers / 2}")

# 6. OPERATIONS BETWEEN ARRAYS

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("\n6. Operations betweem arrays:")
print(f"a + b: {a + b}")
print(f"a - b: {a - b}")
print(f"a * b: {a * b}")

# 7. STATISTICS

scores = np.array([60, 75, 90, 65])

print("\n7. Statistics:")
print(f"Mean: {np.mean(scores)}")
print(f"Maximum: {np.max(scores)}")
print(f"Minimum: {np.min(scores)}")
print(f"Sum: {np.sum(scores)}")
print(f"Standard deviation: {np.std(scores)}")

# 8. 2D ARRAYS

students = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])

print("\n8. 2D Array:")
print(students)

print(f"Shape: {students.shape}")

# 9. 2D INDEXING

print("\n9. 2D Indexing:")

print(f"First student's first score: {students[0, 0]}")
print(f"Second student's third score: {students[1, 2]}")
print(f"Third student's second score: {students[2, 1]}")

# 10. ROWS AND COLUMNS

print("\n10. Rows and columns:")

print(f"First row: {students[0]}")
print(f"Second row: {students[1]}")

print(f"First column: {students[:, 0]}")
print(f"Second column: {students[:, 1]}")
print(f"Third column: {students[:, 2]}")

# 11. FILTERING

print("\n11. Filtering:")

passed = scores >= 75

print(f"Scores: {scores}")
print(f"Passed condition: {passed}")
print(f"Passing scores: {scores[passed]}")

# 12. SHORTER FILTERING

print("\n12. Shorter filtering:")

print(f"Scores above 80: {scores[scores > 80]}")

# 13. ARRAY CREATION FUNCTIONS

print("\n13. Array creation:")

print("Zeros:")
print(np.zeros(5))

print("Ones:")
print(np.ones(5))

print("Range:")
print(np.arange(0, 10, 2))

# 14. RESHAPING

numbers_2 = np.arange(1, 13)
matrix = numbers_2.reshape(3, 4)

print("\n14. Reshaping:")
print(matrix)

# 15. RANDOM NUMBERS

random_numbers = np.random.randint(1, 101, 5)

print("\n15. Random numbers:")
print(random_numbers)