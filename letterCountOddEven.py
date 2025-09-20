# To check whether the number of letters present in a name is odd or even

def name(a):
    return "Hello " + a

def letter_count_odd_even(name):
    count = len(name)
    print("The number of letters is:", count)
    if count % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print()
nm = input("Enter your name: ")
print(name(nm))

print()
result = letter_count_odd_even(nm)
print()
print(f"The number of letters in your name is {result}.")
print("Thank you for using the program " + nm)
print() 