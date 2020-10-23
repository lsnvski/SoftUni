message = input().split(" ")
message_1 = []


def convert(s):
    new = ""
    for x in s:
        new += x
    return new


for element in message:
    chars_element = ""
    digits = ""

    for char in element:
        if char.isdigit():
            digits = digits + str(char)
        elif char.isalpha():
            chars_element = chars_element + str(char)

    message_1.append([int(digits), str(chars_element)])

for i in range(len(message_1)):
    message_1[i][0] = chr(message_1[i][0])
    message_1[i] = str(message_1[i][0]) + str(message_1[i][1])

for index, value in enumerate(message_1):
    change_lett = [x for x in value]
    change_lett[-1], change_lett[1] = change_lett[1], change_lett[-1]
    print(convert(change_lett), end=" ")
