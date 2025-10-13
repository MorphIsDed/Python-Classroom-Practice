# Examples of different types of functions in Python

print("="*40)
print("1. Built-in Function Example")
print("="*40)

# Using the built-in len() function

my_list = [1, 2, 3, 4]
print(f"Length of my_list: {len(my_list)}\n")

print("="*40)
print("2. User-defined Function Example")
print("="*40)
def greet(name):
    """Greets the user by name."""
    return f"Hello, {name}!"

print(greet("Alice"), "\n")

print("="*40)
print("3. Lambda (Anonymous) Function Example")
print("="*40)

# Lambda function to add two numbers

add = lambda x, y: x + y
print(f"Sum using lambda: {add(5, 7)}\n")

print("="*40)
print("4. Recursive Function Example")
print("="*40)
def factorial(n):
    """Returns the factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(f"Factorial of 5: {factorial(5)}\n")

print("="*40)
print("5. Function with Default Arguments Example")
print("="*40)
def power(base, exponent=2):
    """Returns base raised to the power of exponent."""
    return base ** exponent

print(f"power(3): {power(3)}")
print(f"power(3, 3): {power(3, 3)}\n")

print("="*40)
print("6. Function with Variable-length Arguments Example")
print("="*40)
def sum_all(*args):
    """Returns the sum of all arguments."""
    return sum(args)

print(f"Sum of 1, 2, 3, 4: {sum_all(1, 2, 3, 4)}\n")