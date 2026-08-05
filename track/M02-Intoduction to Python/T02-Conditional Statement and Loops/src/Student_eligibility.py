# Read marks, attendance and project completion status
Marks = int(input())
Attendance = int(input())
project_completion = input()
# Check the academic requirements
if Marks >= 60 and Attendance >= 75:
    if project_completion == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
   print("Not Eligible")