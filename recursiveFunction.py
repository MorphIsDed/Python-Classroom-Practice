# Take user input as n and add the numbers from 1 till n

def sum_recursive(n):
    if n <= 0:
        return 0
    else:
        return n + sum_recursive(n - 1)
    
print()
input_str = input("Enter a positive integer: ")
try:
    n = int(input_str)
    if n < 0:
        print("Please enter a positive integer.")
    else:
        result = sum_recursive(n)
        print(f"The sum of all integers from 1 to {n} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer")