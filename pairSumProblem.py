inp = [1, 0, -1, 3, 0, 5]

def zero_shift_end(arr):
    zero_count = arr.count(0)
    non_zero_elements = [num for num in arr if num != 0]
    return non_zero_elements + [0] * zero_count

result = zero_shift_end(inp)
print("Array after shifting zeros to the end:")
print(result)
