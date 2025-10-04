# Find the first non repeating character in a string

def first_non_repeating_character(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

print()
input_str = input("Enter a string to find the first non-repeating character: ")
first_non_repeating_character(input_str)
print("The first non-repeating character is:", first_non_repeating_character(input_str))
print()