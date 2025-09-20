# Creating tuples
t1 = (1, 2, 3)
t2 = (1,)           # Single-Element tuple (Comma Required!)
t3 = 1, 2, 3
nested = (1, (2, 3), 4)

print(t1)
print(t2)
print(t3)
print(nested)

print()
print()

#Indexing and SLicing
t = (10, 20, 30, 40, 50)
print(t[0])   # first
print(t[-1])  # last
print(t[1:4]) # slice

print()
print()

# Concatenation & Repetition
a = (1, 2)
b = (3, 4)
print(a + b)   # Concatenation
print(a * 3)   # Repetition

print()
print()

# Tuple Unpacking
point = (3, 4)
x, y = point
print(x, y)

print()
print()

# Swapping
a, b = 5, 10
a, b = b , a
print(a, b)