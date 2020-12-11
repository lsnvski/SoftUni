
class GenKeys:

    def __init__(self, activation_key):
        self.activ_key = str(activation_key)

    def contains(self, substring):
        if substring in self.activ_key:
            return f"{self.activ_key} contains {substring}"
        else:
            return f"Substring not found!"

    def flip(self, case: str, start: int, end: int):
        if case == "Upper":
            self.activ_key = self.activ_key.replace(self.activ_key[start:end], self.activ_key[start:end].upper())
            return self.activ_key
        else:
            self.activ_key = self.activ_key.replace(self.activ_key[start:end], self.activ_key[start:end].lower())
            return self.activ_key

    def slice(self, start: int, end: int):
        self.activ_key = self.activ_key.replace(self.activ_key[start:end], "")
        return self.activ_key

    def __repr__(self):
        return f"Your activation key is: {self.activ_key}"


key_str = input()
final = GenKeys(key_str)

while True:
    command = input()
    if command == "Generate":
        break

    command = command.split(">>>")
    check_command = command[0]

    if check_command == "Slice":
        print(final.slice(int(command[1]), int(command[2])))

    elif check_command == "Flip":
        print(final.flip(command[1], int(command[2]), int(command[3])))

    elif check_command == "Contains":
        print(final.contains(command[1]))

print(final)