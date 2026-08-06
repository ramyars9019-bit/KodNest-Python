# Read the number of students
student_count = int(input())

marks = []

# Read and store all marks using append()
for i in range(1, student_count + 1):
    mark = int(input())
    marks.append(mark)

position = int(input())
corrected_marks = int(input())
passing_marks = int(input())

# Update the mark at the entered student position (1-indexed)
marks[position - 1] = corrected_marks

# Calculate the total, average, highest, and lowest marks
total_marks = sum(marks)
average_marks = total_marks / len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
passed_students = 0

# Count the students whose marks satisfy the passing condition (>= passing_marks)
for i in marks:
    if i >= passing_marks:
        passed_students += 1

# Display the updated analysis
print("Updated Marks:", marks)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Mark:", highest_marks)
print("Lowest Mark:", lowest_marks)
print("Passed Students:", passed_students)