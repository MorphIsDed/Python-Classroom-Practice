# Reverse the numbers given by the user 

def reverse(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

print()
n = int(input("Enter a number to reverse: "))
reversed_number = reverse(n)
print(f"The reversed number is: {reversed_number}")
print()