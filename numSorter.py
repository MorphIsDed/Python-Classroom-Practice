# Task to sort all the zeros towards the end of the list while maintaining the order of non-zero elements

def move_zeros_to_end(lst):
    result = [x for x in lst if x != 0] + [0] * lst.count(0)
    return result

numbers = [1, 0, 3, 0, 0, 5, 7, 0, 9]
result = move_zeros_to_end(numbers)
print(f"Original list: {numbers}")
print(f"List with zeros at end: {result}")