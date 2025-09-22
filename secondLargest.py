# Find the second largest number in a list

def find_second_largest(num_list):
    if len(num_list) < 2:
        return None
    
    first, second = float('-inf'), float('-inf')
    
    for num in num_list:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    
    return second if second != float('-inf') else None

print()
user_input = input("Enter numbers separated by spaces to find the second largest: ")
num_list = list(map(int, user_input.split()))
second_largest = find_second_largest(num_list)
print()
if second_largest is not None:
    print("Second largest number:", second_largest)
else:
    print("There is no second largest number.")
print() 