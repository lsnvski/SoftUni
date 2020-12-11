students_grades = {}

rows = int(input())

for pair in range(1, rows + 1):
    student = input()
    grade = float(input())

    if student in students_grades.keys():
        students_grades[student].append(grade)
    else:
        students_grades[student] = [grade]


for key, left in students_grades.items():
    avg = sum(left) / len(left)

    if avg >= 4.50:
        students_grades[key] = float(avg)
    else:
        students_grades[key] = 0

delete = [key for key in students_grades if students_grades[key] < 4.5]
students_grades = dict(sorted(students_grades.items(), key=lambda x: x[1], reverse=True))
for key in delete:
    del students_grades[key]

for key, value in students_grades.items():
    print(f'{key} -> {value:.2f}')
