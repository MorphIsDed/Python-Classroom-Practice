# 1. Write a function that counts how many times each word occurs in a given string.

def count_word_occurrences(input_string):
    words = input_string.split()
    word_count = {}

    for word in words:
        word = word.lower()  # Convert to lowercase to make the count case-insensitive
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

print()
print("Q1. Count word occurrences in a string -->")
input_str = input("Enter a string to count word occurrences: ")
result = count_word_occurrences(input_str)
print("Word occurrences:", result)

# 2. Write a program to find the longest word in a given sentence.

def find_longest_word(sentence):
    words = sentence.split()
    if not words:
        return None

    longest_word = max(words, key=len)
    return longest_word

print()
print("Q2. Find the longest word in a sentence -->")
input_str = input("Enter a sentence to find the longest word: ")
print("The longest word is:", find_longest_word(input_str))

# 3. Write a recursive function that prints the first n Fibonacci numbers.

def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_series = [0, 1]
    for i in range(2, n):
        next_value = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_value)

    return fib_series

print()
print("Q3. Generate Fibonacci series up to n numbers -->")
input_str = input("Enter a positive integer n to generate Fibonacci series up to n numbers: ")
try:
    n = int(input_str)
    if n < 0:
        print("Please enter a positive integer.")
    else:
        result = fibonacci_series(n)
        print(f"The Fibonacci series up to {n} numbers is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
    
# 4. Write a function that removes all vowels from a given string.

def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    no_vowel_string = ''.join([char for char in input_string if char not in vowels])
    return no_vowel_string

print()
print("Q4. Remove all vowels from a string -->")
input_str = input("Enter a string to remove vowels: ")
result = remove_vowels(input_str)
print("String without vowels:", result)
print()

print("----------------------------------------------")
print("               Thank You!                     ")
print("          Made by: Abhinay Sahu               ")
print("             Reg No: 24112501                 ")
print("----------------------------------------------")
print()