def max_product_subarray(arr):
    if not arr:
        return 0, []

    max_so_far = arr[0]
    min_so_far = arr[0]
    result = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_so_far, min_so_far = min_so_far, max_so_far

        temp_max = max(arr[i], max_so_far * arr[i])
        temp_min = min(arr[i], min_so_far * arr[i])

        if temp_max == arr[i]:
            s = i

        max_so_far = temp_max
        min_so_far = temp_min

        if max_so_far > result:
            result = max_so_far
            start = s
            end = i

    return result, arr[start:end+1]

int_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
max_product, max_subarray = max_product_subarray(int_list)
print("Array: ", int_list)
print("Maximum product of subarray: ", max_product)
print("Subarray with maximum product: ", max_subarray)