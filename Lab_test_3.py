# Q1. Write a recursive function to calculate the factorial of a given number.

print("Q1. Write a recursive function to calculate the factorial of a given number --> ")
print()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {num} is {factorial(num)}")
print()

# Q2. Write a recursive function to find the greatest common divisor (GCD) of two numbers.

print("Q2. Write a recursive function to find the greatest common divisor (GCD) of two numbers --> ")
print()

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")
print()

# Q3. Write a recursive function to reverse a given string.

print("Q3. Write a recursive function to reverse a given string --> ")
print()

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
    
input_str = input("Enter a string to reverse: ")
print(f"The reversed string is: {reverse_string(input_str)}")
print()

# Q4. Write a Python program to separate even and odd numbers from a given list.

print("Q4. Write a Python program to separate even and odd numbers from a given list --> ")
print()

def separate_even_odd(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

input_str = input("Enter a list of numbers separated by spaces: ")
num_list = list(map(int, input_str.split()))
even_numbers, odd_numbers = separate_even_odd(num_list)
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print()

# Q5. Write a program to count how many times each word appears in a given paragraph.

print("Q5. Write a program to count how many times each word appears in a given paragraph --> ")
print()

def word_count(paragraph):
    words = paragraph.split()
    word_freq = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')  # Normalize the word
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

input_paragraph = input("Enter a paragraph: ")
word_frequencies = word_count(input_paragraph)
print("Word frequencies:")
for word, count in word_frequencies.items():
    print(f"{word}: {count}")
print()