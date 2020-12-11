course_students = {}

while True:
    command = input()

    if command == "end":
        break

    command = command.split(" : ")

    course_key = command[0]
    student_value = command[1]

    if course_key in course_students.keys():
        course_students[course_key].append(student_value)
    else:
        course_students[course_key] = [student_value]

course_students = dict(sorted(course_students.items(), key=lambda x: len(x[1]), reverse=True))
for value in course_students.keys():
    course_students[value].sort()

for key, value in course_students.items():
    print(f'{key}: {len(value)}')
    for x in course_students[key]:
        print(f'-- {x}')