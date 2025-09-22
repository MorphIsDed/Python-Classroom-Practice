# Take input of two list and find their intersection

def intersection_of_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = list(set1 & set2)
    return intersection

print()
user_input1 = input("Enter numbers for the first list separated by spaces: ")
list1 = list(map(int, user_input1.split()))
user_input2 = input("Enter numbers for the second list separated by spaces: ")
list2 = list(map(int, user_input2.split()))
intersection = intersection_of_lists(list1, list2)
print()
if intersection:
    print("Intersection of the two lists:", intersection)
else:
    print("There is no intersection between the two lists.")
print()