# Take factorial of n numbers using recursion function

def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
print()
input_str = input("Enter a non-negative integer: ")
try:
    n = int(input_str)
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        result = factorial_recursive(n)
        print(f"The factorial of {n} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid non-negative integer.")