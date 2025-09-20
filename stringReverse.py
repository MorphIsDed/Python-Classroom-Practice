# Take input of a string and return the reversed string.

def reverse_string(input_string):
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str

print("Enter a string to reverse:")
user_input = input()
reversed_string = reverse_string(user_input)
print("Reversed string:", reversed_string)