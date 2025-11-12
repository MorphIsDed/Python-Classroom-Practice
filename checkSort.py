# Check if the list is sorted in ascending order without using pre-built functions

def is_sorted_ascending(lst):
    if len(lst) < 2:
        return "Too few elements to determine sorting."
    
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return "The list is not sorted in ascending order."
    return "The list is sorted in ascending order."

lst = [input("Enter numbers separated by spaces: ").split()]
result = is_sorted_ascending(lst)

print()

print(f"Input list: {lst}")
print(result)

print()