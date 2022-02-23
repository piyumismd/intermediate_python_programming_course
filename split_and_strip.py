

string = "  Hello World\n  "
string1 = "  welcome\n  "
string2 = "  New Year  "
string_set = string + string1 + string2

new_word = string_set.split()
print(new_word)

new_word = string_set.split("\n")
print(new_word)

new_word = string_set.split(" ")
print(new_word)

new_word = string_set.strip(" ")
print(new_word)

new_word = string_set.strip()
print(new_word)

new_word = string_set.strip("\n ")
print(new_word)