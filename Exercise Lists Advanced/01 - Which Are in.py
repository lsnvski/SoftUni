<<<<<<< HEAD

list_string_1 = input().split(", ")
list_string_2 = input().split(", ")


list_string = [string1 for string1 in list_string_1 for string2 in list_string_2 if string1 in string2]
list_string = list(dict.fromkeys(list_string))

=======

list_string_1 = input().split(", ")
list_string_2 = input().split(", ")


list_string = [string1 for string1 in list_string_1 for string2 in list_string_2 if string1 in string2]
list_string = list(dict.fromkeys(list_string))

>>>>>>> 208b47ea4d0bcafc85cf570be2bfb1f6ac828c17
print(list_string)