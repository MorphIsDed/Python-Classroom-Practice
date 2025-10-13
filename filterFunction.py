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