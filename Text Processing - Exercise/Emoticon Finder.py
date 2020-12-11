def emo_extract(word):
    for index, char in enumerate(word):
        if char == ":":
            yield char + word[index + 1]


text = input()

for emo in emo_extract(text):
    print(emo)
