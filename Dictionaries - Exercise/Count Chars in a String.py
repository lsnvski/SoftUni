def parser(string_list):
    occurences_list = {}
    for word in string_list:
        for letter in word:
            key = occurences_list.keys()
            if letter in key:
                occurences_list[letter] += 1
            else:
                occurences_list[letter] = 1
    return occurences_list


string = input().split(" ")
final = parser(string)
for key in final:
    print(f'{key} -> {final[key]}')
