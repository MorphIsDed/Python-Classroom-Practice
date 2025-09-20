# Testing how different list functions work

a = [1, 2, 3, 4, 5, 6]
a.append(7)
print("Append --> ", a)
print()
a.extend([8, 9])
print("Extend --> ", a)
print()
a.insert(0 , 0)
print("Insert --> ", a)
print()
a.remove(9)
print("Remove --> ", a)
print()
a.pop()
print("Pop --> ", a)
print()
a.clear()
print("Clear --> ", a)
print()

# Some more function
# index(x), count(), sort(key=None, reverse=False), reverse(), dipcopy(), shallowcopy()
# Write the difference between shallow copy and dipcopy