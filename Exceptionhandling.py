#Exception Handling
# try: takes the error 
# catch: handes the error 
# RunTime error  

# try:
#     print(1/0)
# except:
#     print("Division by zero is not allowed") 
    
try:
    x = int("Hello")
    y = 10/0
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Invalid conversion to integer.")    