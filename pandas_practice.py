import pandas as pd

scores = pd.Series(
    [80, 75, 90, 65],
    index = ["Samuel", "David", "John", "Peter"]
) 

print(scores)
print(scores["Samuel"])
 
data = {
    "Name": ["Samuel", "David", "John", "Peter"],
    "Age": [14, 15, 14, 16],
    "Score": [80, 65, 90, 75]
}
# Intro
students = pd.DataFrame(data)
print("\n", students)
print("\n", students["Name"])
print("\n", students["Score"])
print("\n", students.loc[0, "Name"])  
print("\n", students.loc[1, "Name"])
print("\n", students.loc[2, "Score"])
print("\n", students.loc[3, "Score"])
print("\n", students.iloc[2, 2])
# Filtering
passed = students[students["Score"] >= 75]
print("\n", passed)
young_students = students[students["Age"] < 16]
print("\nYs", young_students)
print("\nl", students[students["Age"] == 14])
print("\nn", students[students["Score"] >= 80])
result = students[(students["Age"] == 14) & (students["Score"] > 80)]
print(result)
r"""# Sorting
print("\n", students.sort_values("Score"))
print("\n", students.sort_values("Score", ascending=False))
print("\n", students.sort_values(["Age", "Score"], ascending=[True, False]))
students["passed"] = students["Score"] >= 75
students["Double_Score"] = students["Score"] * 2
print("\n", students)
students = students.drop("Double_Score", axis=1)
print(students)
# Missing values
students = pd.DataFrame({
    "Name": ["Samuel", "David", "John", "Peter"],
    "Age": [14, 15, 14, 16],
    "Score": [80, None, 90, None]
})

print(students)
print("\nMissing values:")
print(students.isna())
print("\nCount missing values:")
print(students.isna().sum())
print("\nRow with scores:")
print(students[students["Score"].notna()])
print("\n",students.dropna())
students_filled = students.copy()
students_filled["Score"] = students_filled["Score"].fillna(50)
print(students_filled)
# Duplicates
students = pd.DataFrame({
    "Name": ["Samuel", "David", "John", "Samuel", "Peter", "John"],
    "Age": [14, 15, 14, 14, 16, 14],
    "Score": [80, 65, 95, 80, 75, 95]
})

print("Original DataFrame:")
print(students)

# Find duplicate rows
print("\nDuplicate rows:")
print(students.duplicated())

# Count duplicate rows
print("\nNumber of duplicated rows:")
print(students.duplicated().sum())

# Remove duplicate rows
students_clean = students.drop_duplicates()
print("\nAfter removing duplicates:")
print(students_clean)
# Cleaning text
students = pd.DataFrame({
    "Name": [" Samuel ", "DAVID", "john", "Peter ", " SAMUEL"],
    "Score": [80, 65, 95, 75, 88]
})
print("Original:")
print(students)

# Remove extra spaces
students["Name"] = students["Name"].str.strip()

# Convert names to lowercase
students["Name"] = students["Name"].str.lower()

print("\nCleaned:")
print(students)
# Incorrect 
students = pd.DataFrame({
    "Name": ["Samuel", "David", "John", "Peter"],
    "Age": [14, 15, 14, 16],
    "Score": [80, 65, 950, 75]
})

print("Before cleaning:")
print(students)

# Fix the incorrect score
students["Score"] = students["Score"].replace(950, 95)

print("\nAfter fixing the score:")
print(students)
"""
# Check data types
print("\nData types:")
print(students.dtypes)
r"""
students = pd.DataFrame({
    " Student Name ": ["Samuel", "David", "John"],
    " Age ": [14, 15, 14],
    " Test Score ": [80, 75, 90]
})

print("Before cleaning:")
print(students.columns)

students.columns = students.columns.str.strip().str.lower().str.replace(" ", "_")

print("\nAfter cleaning:")
print(students.columns)

students = pd.read_csv(r"C:\Users\Admin\Documents\pandas_practice.csv")
print(students.isna())
"""