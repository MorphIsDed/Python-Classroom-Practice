# import keyword

# print()
# print("Python Keywords -->", keyword.kwlist)
# print()

# Loops in Python

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)

print()
print()

for x in "banana":
    print(x)
    
print()
print()
    
for x in fruits:
    print(x)
    if x == "banana":
        break
    
if True:
    print("Inside If Block")
print("Outside If Block")
    
# Functions in Python
def num(ber, name):
    print("Hello from a function")
    return f"Hello! welcome {name}"