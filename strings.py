text = "Python"

print(text[0])    # First character
print(text[-1])   # Last character
print(text[1:4])  # Characters from index 1 to 3
print(text[:3])   # First three characters
print(text[3:])   # Characters from index 3 to the end
print(text[::2])  # Every second character

a = "Data"
b = "Science"
print(a + " " + b)  # Concatenation
print(a * 3)        # Repetition

s = "hello world"
print(s.upper())        # Convert to uppercase
print(s.lower())        # Convert to lowercase
print(s.capitalize())   # Capitalize first letter
print(s.title())        # Title case
print(s.swapcase())     # Swap case

c = "Python3"
print(c.isalpha())          # Check if all characters are alphabetic
print("Python".isalpha())   # Check if all characters are alphabetic
print("123".isdigit())      # Check if all characters are digits
print("abc123".isalnum())   # Check if all characters are alphanumeric
print("   ".isspace())      # Check if all characters are whitespace
print("hello".islower())    # Check if all characters are lowercase
print("HELLO".isupper())    # Check if all characters are uppercase

d = "Data Science with Python"
print(d.find("Science"))     # Find substring
print(d.find("AI"))          # Substring not found
print(d.count("a"))          # Count occurrences of 'a'
print(d.startswith("Data"))  # Check if starts with 'Data'
print(d.endswith("Python"))  # Check if ends with 'Python'