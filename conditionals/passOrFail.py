marks_list = {}
for i in range(3):
    subject = input(f"Enter Subject {i+1} name: ")
    percentage = int(input(f"Percentage in {subject}: "))
    marks_list[subject] = percentage

# Calculate the actual average percentage
avg_percentage = sum(marks_list.values()) / 3
passed_all_subjects = True

# Check individual subject requirement
for subject, percentage in marks_list.items():
    if percentage < 33:
        print(f"FAILED: Scored only {percentage}% in {subject} (Required: 33%)")
        passed_all_subjects = False
        break

# Check total percentage requirement only if they passed individual subjects
if passed_all_subjects:
    if avg_percentage >= 40:
        print(f"PASSED: Total percentage is {avg_percentage:.2f}%")
    else:
        print(f"FAILED: Total percentage is {avg_percentage:.2f}% (Required: 40%)")