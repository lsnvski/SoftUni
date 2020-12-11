hyphens = [
    95, # underscore
    45, # hypen
]


def validator(s):
    is_valid = False

    for symbol in s:

        # If not digit or alpha
        # Check for hyphen and underscore:
        if not symbol.isdigit() and not symbol.isalpha():
            if ord(symbol) in hyphens:
                continue
            else:
                is_valid = False
                break

        is_valid = True

    return is_valid


valid = []

username = input().split(", ")

for user in username:
    if 3 <= len(user) <= 16 and validator("".join(s for s in user)):
        valid.append(user)

print("\n".join(x for x in valid))
