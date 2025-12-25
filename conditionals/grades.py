percentage = int(input('Enter percentage to get grade : '))
if(percentage>=90 and percentage<=100):
    print(f"GRADE: Ex")
elif(percentage>=80 and percentage<=90):
    print(f"GRADE: A")
elif(percentage>=70 and percentage<=80):
    print(f"GRADE: B")
elif(percentage>=60 and percentage<=70):
    print(f"GRADE: C")
elif(percentage>=50 and percentage<=60):
    print(f"GRADE: D")
else:
    print(f"GRADE: F")

'''
grade_scheme = {
    'Ex': [90, 100],
    'A' : [80, 90],
    'B' : [70, 80],
    'C' : [60, 70],
    'D' : [50, 60]
}

percentage = float(input('Enter percentage: '))
assigned_grade = "F"

for grade, bounds in grade_scheme.items():
    # Check if: min <= percentage < max
    if bounds[0] <= percentage <= bounds[1]:
        assigned_grade = grade
        break

print(f"GRADE: {assigned_grade}")
'''