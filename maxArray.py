# Program to find the sub array with maximum product (with provision for negative numbers)

def max_product_subarray(arr):
    if not arr:
        return 0, []

    global_max_product = arr[0]
    result_start_index = 0
    result_end_index = 0

    max_prod_ending_here = arr[0]
    min_prod_ending_here = arr[0]
    
    current_max_start_index = 0
    current_min_start_index = 0

    for i in range(1, len(arr)):
        num = arr[i]

        if num < 0:
            max_prod_ending_here, min_prod_ending_here = min_prod_ending_here, max_prod_ending_here
            current_max_start_index, current_min_start_index = current_min_start_index, current_max_start_index

        if num > max_prod_ending_here * num:
            max_prod_ending_here = num
            current_max_start_index = i
        else:
            max_prod_ending_here = max_prod_ending_here * num

        if num < min_prod_ending_here * num:
            min_prod_ending_here = num
            current_min_start_index = i
        else:
            min_prod_ending_here = min_prod_ending_here * num
        
        if max_prod_ending_here > global_max_product:
            global_max_product = max_prod_ending_here
            result_start_index = current_max_start_index
            result_end_index = i

    return global_max_product, arr[result_start_index : result_end_index + 1]

try:
    input_str = input("Enter a list of integers separated by spaces: ")
    int_list = [int(x) for x in input_str.split()]

    if not int_list:
        print("The list is empty.")
    else:
        max_product, max_subarray = max_product_subarray(int_list)
        print("\nArray: ", int_list)
        print("Maximum product of a subarray: ", max_product)
        print("Subarray with maximum product: ", max_subarray)

except ValueError:
    print("Invalid input. Please enter only integers separated by spaces.")