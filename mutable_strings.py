
input_string = "immutable"
char_list = list(input_string)
print("Current List:", char_list)
change_index = 3
new_char = 'p'

if 0 <= change_index < len(char_list):
    char_list[change_index] = new_char
else:
    print("Index out of range")


modified_string = ''.join(char_list)

print("Modified String:", modified_string)
