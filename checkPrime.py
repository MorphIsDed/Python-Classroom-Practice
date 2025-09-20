# Check the number given is prime or not

def name(a):
    return "Hello " + a

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print()
nm = input("Enter your name: ")
print(name(nm))

print()
n = int(input("Enter a number to check if it is prime: "))
result = is_prime(n)
print()

if result:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
print("Thank you for using the program " + nm)
print()