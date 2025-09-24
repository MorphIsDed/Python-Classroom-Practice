# Program to find the sub array with maximum product (with provision for negative numbers)

def max_product_subsequence(arr):
    if not arr:
        return 0, []

    if len(arr) == 1:
        return arr[0], arr

    positives = [x for x in arr if x > 0]
    negatives = [x for x in arr if x < 0]
    has_zeros = any(x == 0 for x in arr)

    if not positives and not negatives:
        return 0, [0]

    if len(negatives) % 2 != 0:
        if len(negatives) == 1 and not positives:
            if has_zeros:
                return 0, [0]
            else:
                return negatives[0], negatives
        
        negatives.sort()
        
        subsequence_for_max_product = positives + negatives[:-1]
        
    else:
        subsequence_for_max_product = positives + negatives

    if not subsequence_for_max_product and has_zeros:
        return 0, [0]
    
    max_prod = 1
    for num in subsequence_for_max_product:
        max_prod *= num
        
    return max_prod, subsequence_for_max_product

try:
    input_str = input("Enter a list of integers separated by spaces: ")
    int_list = [int(x) for x in input_str.split()]

    if not int_list:
        print("The list is empty.")
    else:
        max_product, max_subsequence = max_product_subsequence(int_list)
        print("\nArray: ", int_list)
        print("Maximum product of a subsequence: ", max_product)
        print("Subsequence with maximum product: ", max_subsequence)

except ValueError:
    print("Invalid input. Please enter only integers separated by spaces.")