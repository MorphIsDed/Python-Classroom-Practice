# Take user input of a string and find the duplicate letters (including spaces) and their count in the string.

def find_duplicates(input_string):
    char_count = {}
    
    for char in input_string:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    duplicates = {char: count for char, count in char_count.items() if count > 1}
    
    return duplicates

print("Enter a string:")
user_input = input()
duplicates = find_duplicates(user_input)
if duplicates:
    print("Duplicate letters and their counts:")
    for char, count in duplicates.items():
        print(f"'{char}': {count}")
else:
    print("No duplicate letters found.")