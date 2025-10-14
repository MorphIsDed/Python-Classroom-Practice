# To create a program to square each element in a list using map function

print("="*40)
print("1. Squaring each element in a list using map function")
print("="*40)

def square(x):
    return x * x

def main():
    input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    squared_numbers = list(map(square, input_list))
    print(f"Squared numbers: {squared_numbers}")
    
if __name__ == "__main__":
    main()
    
# To create a program to convert each word to uppercase using map function

print("="*40)
print("2. Converting each word to uppercase using map function")
print("="*40)

def to_upper(word):
    return word.upper()

def main_uppercase():
    ipt_words = input("Enter words separated by spaces: ").split()
    uppercase_words = list(map(to_upper, ipt_words))
    print(f"Uppercase words: {uppercase_words}")

main_uppercase()

# To create a program to find the cube of each number 

print("="*40)
print("3. Finding the cube of each number using map function")
print("="*40)

def cube(x):
    return x ** 3

def main_cube():
    ipt_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    cubed_numbers = list(map(cube, ipt_list))
    print(f"Cubed numbers: {cubed_numbers}")
    
main_cube()

# To create a program using map() to add the coreesponding elements of two lists

print("="*40)
print("4. Adding corresponding elements of two lists using map function")
print("="*40)

def add(x, y):
    return x + y

def main_add():
    list1 = list(map(int, input("Enter the first list of numbers separated by spaces: ").split()))
    list2 = list(map(int, input("Enter the second list of numbers separated by spaces: ").split()))
    summed_list = list(map(add, list1, list2))
    print(f"Summed list: {summed_list}")
    
main_add()

# Given a list of temparatures in Celsius, convert them to Fahrenheit using map and a lambda function

print("="*40)
print("5. Converting Celsius to Fahrenheit using map and lambda function")
print("="*40)

celsius_temps = list(map(float, input("Enter a list of temperatures in Celsius separated by spaces: ").split()))
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print(f"Temperatures in Fahrenheit: {fahrenheit_temps}")