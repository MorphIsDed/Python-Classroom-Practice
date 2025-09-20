# Check if the sum of two numbers are odd or even

def name(a):
    return "Hello " + a

def check_odd_even(num1, num2):
    total = num1 + num2
    print("The sum is:", total)
    if total % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print()
nm = input("Enter your name: ")
print(name(nm))
    
print()
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
result = check_odd_even(n1, n2)

print()
print(f"The sum of {n1} and {n2} is {result}.")
print()