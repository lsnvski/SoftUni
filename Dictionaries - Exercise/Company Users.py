comp_emp = {}

while True:
    command = input()

    if command == "End":
        break

    command = command.split(" -> ")

    company = command[0]
    employee = command[1]

    if company in comp_emp:

        if comp_emp[company][0] == employee:
            continue

        comp_emp[company].append(employee)

    else:
        comp_emp[company] = [employee]

comp_emp = dict(sorted(comp_emp.items(), key=lambda x: x[0]))
comp_emp = dict(sorted(comp_emp.items(), key=lambda x: x[1]))


spc = '\n-- '

for key, value in comp_emp.items():
    print(f'{key}\n-- {spc.join(x for x in value)}')
