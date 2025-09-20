def print_header():
    print()
    print("---------------------------------------")
    print("          Lab Test - 1                 ")
    print("---------------------------------------")
    print()

print_header()

def welcome_message():
    print("Welcome to my Program")
    print()

welcome_message()

def print_footer():
    print("|-------------------------------------|")
    print("|            Thank You!               |")
    print("|             Made By:                |")
    print("|        Abhinay Kumar Sahu           |")
    print("|             24112501                |")
    print("|-------------------------------------|")
    print()

# Question 1 - Write a function check_even_odd(n) that takes a number as input and prints whether it is Even or Odd.

print("Question 1 - Write a function check_even_odd(n) that takes a number as input and prints whether it is Even or Odd.")
print()
def check_odd_even(num1, num2):
    total = num1 + num2
    print("The sum is:", total)
    if total % 2 == 0:
        return "Even"
    else:
        return "Odd"    

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
result = check_odd_even(n1, n2)
print(f"The sum of {n1} and {n2} is {result}.")
print()

# Question 2 - Write a function is_prime(n) that returns True if the number is prime, otherwise False.

print("Question 2 - Write a function is_prime(n) that returns True if the number is prime, otherwise False.")
print()
def is_prime(n):
    if n < 1:
        return False
    if n == 1:
        return print("1 is neither prime nor composite.")
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it is prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
print()

# Question 3 - Write a function factorial(n) that returns the factorial of a given number.

print("Question 3 - Write a function factorial(n) that returns the factorial of a given number.")
print()
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact
    
number = int(input("Enter a number to find its factorial: "))
fact_result = factorial(number)
print(f"The factorial of {number} is {fact_result}.")
print()

# Question 4 - Write a function is_perfect(n) that checks whether a number is Perfect.

print("Question 4 - Write a function is_perfect(n) that checks whether a number is Perfect.")
print()
def is_perfect(n):
    if n < 1:
        return False
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n

num = int(input("Enter a number to check if it is perfect: "))
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
print()

# Question 5 - Write a function gcd(a, b) that returns the Greatest Common Divisor (HCF) of two numbers.

print("Question 5 - Write a function gcd(a, b) that returns the Greatest Common Divisor (HCF) of two numbers.")
print()
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd_result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd_result}.")
print()

print_footer()