# Sorting and filtering a list of numbers to get only prime numbers

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
prime_numbers = list(filter(lambda x: is_prime(x), input_list))
print(f"Prime numbers in the list: {prime_numbers}")

# Use filter() to get even numbers from a list

def is_even(n):
    return n % 2 == 0

input_list_even = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
even_numbers = list(filter(is_even, input_list_even))
print(f"Even numbers in the list: {even_numbers}")

# Use filter() to get number less than some number 

def less_than(n):
    return n < 10

input_list_lt = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
less_than_n_numbers = list(filter(less_than, input_list_lt))
print(f"Numbers less than five: {less_than_n_numbers}")

# From a list of words, keep only the word which starts from 'a' or 'A'

def starts_with_a(word):
    return word.lower().startswith('a')

input_words = input("Enter words separated by spaces: ").split()
words_starting_with_a = list(filter(starts_with_a, input_words))
print(f"Words starting with 'a' or 'A': {words_starting_with_a}")

