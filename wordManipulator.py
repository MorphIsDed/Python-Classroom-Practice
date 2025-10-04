# Program to replace every space in a string with a given character

def replace_spaces(s, char):
    return s.replace(" ", char)

print()
input_str = input("Enter a string: ")
replace_char = input("Enter a character to replace spaces with: ")
print("String after replacing spaces:", replace_spaces(input_str, replace_char))
print()