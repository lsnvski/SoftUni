class Arrange:

    def __init__(self, string):
        self.string = string

    def move(self, direction, index):

        if index in range(len(self.string)):
            if direction == "Right":
                if index != len(self.string) - 1:
                    self.string[index], self.string[index + 1] = self.string[index + 1], self.string[index]

            elif direction == "Left":
                if index != 0:
                    self.string[index], self.string[index - 1] = self.string[index - 1], self.string[index]

    def check(self, number):
        to_show = []

        for index, element in enumerate(self.string):
            if number == "Even":
                if index % 2 == 0:
                    to_show.append(element)

            elif number == "Odd":
                if index % 2 != 0:
                    to_show.append(element)

        return ' '.join(to_show)

    def __repr__(self):
        return f"You crafted {''.join(self.string)}!"


string_particles = str(input()).split("|")
final = Arrange(string_particles)

while True:
    command = input()

    if command == "Done":
        break

    command = command.split(" ")

    if command[0] == "Move":
        direction = command[1]
        index = int(command[2])
        final.move(direction, index)

    elif command[0] == "Check":
        print(final.check(command[1]))

print(final)