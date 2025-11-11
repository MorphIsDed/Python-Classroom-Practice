# In a list of integers, find the first repeated element.

def find_repeated_element(lst):
    seen = set()
    for num in lst:
        if num in seen:
            return num
        seen.add(num)
    return None

numbers = [2, 4, 3, 5, 1, 4, 6, 3]
result = find_repeated_element(numbers)

print()

print(f"Original list: {numbers}")
if result is not None:
    print(f"The first repeated element is: {result}")
    print(f"Total occurrences of {result}: {numbers.count(result)}")
else:
    print("No repeated elements found.")

print()