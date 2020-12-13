string = input()

while True:
    command_raw = input()

    if command_raw == "Complete":
        break

    command = command_raw.split()

    if command[0] == "Make" and command[1] == "Lower":
        string = string.lower()
        print(string)
    elif command[0] == "Make" and command[1] == "Upper":
        string = string.upper()
        print(string)

    elif command[0] == "GetDomain":
        index = int(command[1])
        print(string[-index::])

    elif command[0] == "Replace":
        string = string.replace(str(command[1]), "-")
        print(string)

    elif command[0] == "GetUsername":
        if "@" in string:
            pos = int(string.find("@"))
            print(string[:pos])
        else:
            print(f"The email {string} doesn't contain the @ symbol.")

    elif command[0] == "Encrypt":
        for x in string:
            print(ord(x), end=" ")