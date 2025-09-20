# we have f(x, y), find x + y^2

def name(a):
    return "Hello " + a

def function(x, y):    
    return x + y**2

print()
nm = input("Enter your name: ")
print(name(nm))

print()
x = int(input("Enter x: "))
y = int(input("Enter y: "))

print()
final = function(x, y)
print("Final Result is: ", final)
print("Thank you for using the program " + nm)

print()