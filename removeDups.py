# Remove all the duplicates from a given list

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print()
input_str = input("Enter a list of elements separated by spaces: ")
my_list = input_str.split()
print("Original list: ", my_list)
print("Modified List: ", remove_duplicates(my_list))