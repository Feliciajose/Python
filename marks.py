num_students = int(input("Enter the number of students: "))

total_marks = 0
for i in range(num_students):
    marks = int(input(f"Enter marks for student {i+1}: "))
    total_marks += marks

average = total_marks / num_students
print("The average marks are:", average)