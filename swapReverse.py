# Take input of a string and return the reversed string by a swapping function

def swap_reverse(input_string):
    char_list = list(input_string)
    left, right = 0, len(char_list) - 1
    
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    
    return ''.join(char_list)

print("Enter a string to reverse by swapping:")
user_input = input()
reversed_string = swap_reverse(user_input)
print("Reversed string:", reversed_string)
