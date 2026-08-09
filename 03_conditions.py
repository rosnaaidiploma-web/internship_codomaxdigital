# 03_conditions.py
# Conditional Statements

marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Marks:", marks)
print("Grade:", grade)
