# Q1 Write a program to check whether a given string is a palindrome or not.

print("Question 1 --->")
print("----------------------------------")

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

print()
string = input("Enter a string: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
print()

# Q2 Write a function in Python to check whether a given number is a perfect square or not.

print("Question 2 --->")
print("----------------------------------")

import math
def is_perfect_square(n):
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n

print()
number = int(input("Enter a number: "))
if is_perfect_square(number):
    print(f"{number} is a perfect square.")
else:
    print(f"{number} is not a perfect square.")
print()

# Q3 Write a Python function that takes a list as input and returns all the duplicate elements present in the list without using typecasting.

print("Question 3 --->")
print("----------------------------------")

def find_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates

print()
input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
duplicates = find_duplicates(input_list)
if duplicates:
    print("Duplicate elements:", duplicates)
else:
    print("No duplicate elements found.")
print()

# Q4 Create a list of integers and write a program to reverse the list without using the built-in reverse() function and slicing operator.

print("Question 4 --->")
print("----------------------------------")

def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

print()
int_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
reversed_list = reverse_list(int_list)
print("Reversed list:", reversed_list)
print()

# Write a Python program to demonstrate the use of try, except and finally.

print("Question 5 --->")
print("----------------------------------")

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please enter numbers."
    else:
        return f"The result of {a} divided by {b} is {result}."
    finally:
        print("Execution of function is complete.")
        
print()
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))
print(divide_numbers(num1, num2))
print()

# Q6 Write a Python function that takes a list of integers as input and replaces all negative numbers with 0.

print("Question 6 --->")
print("----------------------------------")

def replace_negatives_with_zero(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = 0
    return lst

print()
int_list = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
modified_list = replace_negatives_with_zero(int_list)
print("List after replacing negative numbers with 0:", modified_list)
print()

# Q7 (a) Create a set with some elements and write a program to add two new elements into
# the set.
# (b) Using the updated set from part (a), write a program to check whether a given element exists in it.
# (c) Now clear all elements from the set and display the result.
# (d) After clearing, create two new sets and write a program to check if they are equal.
# (e) Finally, take one of the sets from part (d) and write a program to iterate through it and
# print each element.

print("Question 7 --->")
print("----------------------------------")

# (a) Create a set and add two new elements
init_set = {1, 2, 3, 4}
print("Original set:", init_set)
init_set.add(5)
init_set.add(6)
print("Set after adding two elements:", init_set)

# (b) Check if an element exists in the set
element = int(input("Enter an element to check if it exists in the set: "))
if element in init_set:
    print(f"{element} exists in the set.")
else:
    print(f"{element} does not exist in the set.")

# (c) Clear all elements from the set and display the result
init_set.clear()
print("Set after clearing all elements:", init_set)

# (d) Create two new sets and check if they are equal
set1 = {10, 20, 30}
set2 = {30, 20, 10}
if set1 == set2:
    print("set1 and set2 are equal.")
else:
    print("set1 and set2 are not equal.")

# (e) Iterate through one of the sets and print each element
print("Elements in set1:")
for elem in set1:
    print(elem)
    

# Q8 (a) Create a dictionary of 3 students with their names as keys and marks (out of 100) as values.
# Display the dictionary.
# (b) Add a new student entry into the dictionary and update the marks of one existing student.
# (c) From the updated dictionary, write a program to find the student with the highest marks.
# (d) Remove the student with the lowest marks from the dictionary and display the updated
# dictionary.
# (e) Finally, iterate through the dictionary and print each student’s name along with their marks in
# the format: “Alice got 85 marks”.

print("Question 8 --->")
print("----------------------------------")

# (a) Create a dictionary of 3 students and display it
print()
students = {"Alice": 85, "Bob": 78, "Charlie": 92}
print("Initial dictionary of students and marks:", students)

# (b) Add a new student and update marks of one existing student
print()
students["David"] = 88
students["Bob"] = 82
print("Dictionary after adding and updating:", students)

# (c) Find the student with the highest marks
print()
highest_student = max(students, key=students.get)
print(f"Student with the highest marks: {highest_student} ({students[highest_student]} marks)")

# (d) Remove the student with the lowest marks and display the updated dictionary
print()
lowest_student = min(students, key=students.get)
students.pop(lowest_student)
print("Dictionary after removing the student with the lowest marks:", students)

# (e) Iterate and print each student's name and marks
print()
for name, marks in students.items():
    print(f"{name} got {marks} marks")