# Creating sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = set([1, 2, 2, 3])  # removes duplicate

print()
print(s1)
print(s2)
print(s3)

# Membership Test
print()
print(3 in s1)
print(7 in s1)

print()
print()

# Union, Intersection, Difference, Symmetric Difference
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)

# Adding and Removing
s = {1, 2, 3}
s.add(4)
s.remove(2)      # raises keyError if not found
s.discard(99)    # safe removal (no error)
print()
