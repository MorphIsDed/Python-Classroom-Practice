# Take input of numbers as list and return the reversed list by a swapping function

def swap_reverse(num_list):
    left, right = 0, len(num_list) - 1
    
    while left < right:
        num_list[left], num_list[right] = num_list[right], num_list[left]
        left += 1
        right -= 1
    
    return num_list

print()
print("Enter numbers separated by spaces to reverse by swapping:")
user_input = input()
num_list = list(map(int, user_input.split()))
reversed_list = swap_reverse(num_list)
print()
print("Reversed list:", reversed_list)
