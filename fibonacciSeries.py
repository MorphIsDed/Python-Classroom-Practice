# Take user input of n and print the Fibonacci series up to n numbers

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