# Make a list by taking in input from the user and perform the following operations:
# 1. Make a function for reversing the list
# 2. Make a function for sorting the list
# 3. Make a function for finding the maximum and minimum element in the list

def reverse_list(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst

def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def max_min_list(lst):
    maximum = lst[0]
    minimum = lst[0]
    for item in lst:
        if item > maximum:
            maximum = item
        if item < minimum:
            minimum = item
    return maximum, minimum

user_list = []

print("Enter elements for the list (type 'done' to finish):")
while True:
    element = input("Enter element: ")
    if element.lower() == 'done' or element == 'Done' or element == 'DONE':
        break
    try:
        user_list.append(int(element))
    except ValueError:
        try:
            user_list.append(float(element))
        except ValueError:
            user_list.append(element)
print("Your list:", user_list)

while True:
    print()
    print("Menu:")
    print("1. Reverse the list")
    print("2. Sort the list")
    print("3. Find Maximum and Minimum elements in the list")
    print("0. Exit")
    choice = int(input("Enter your choice (0-3): "))
    print()
    if choice == 1:
        reversed_list = reverse_list(user_list.copy())
        print("Reversed List:", reversed_list)
    elif choice == 2:
        sorted_list = sort_list(user_list.copy())
        print("Sorted List:", sorted_list)
    elif choice == 3:
        maximum, minimum = max_min_list(user_list)
        print(f"Maximum element: {maximum}")
        print(f"Minimum element: {minimum}")
    elif choice == 0:
        print("Thank you for using the program.")
        break
    else:
        print("Invalid choice! Please select a valid option.")