# Program to input student marks, calculate average and assign grade

# Input number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Initialize total marks
total_marks = 0

# Loop to take marks input
for i in range(1, num_subjects + 1):
    mark = float(input(f"Enter mark for subject {i}: "))
    total_marks += mark

# Calculate average
average = total_marks / num_subjects

# Determine grade using if-else
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Output results
print("\n--- Result ---")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
