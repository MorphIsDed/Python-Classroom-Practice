st_lst = [45, 78, 92, 67, 88, 34, 91, 55]

def st_passed(marks):
    if marks >= 50:
        return True
    else:
        return False
    
passed_students = list(filter(st_passed, st_lst))
print()
print(f"List of students who passed: {passed_students}")
print(f"Number of students who passed: {len(passed_students)}")
print(f"Number of students who failed: {len(st_lst) - len(passed_students)}")
print()

# Challange A -- Use map() and lambda to apply a 20% discount to all prices

prices = [100, 250, 450, 80, 320]
dsc_prc = list(map(lambda price: price * 0.8, prices))

# Challenge B -- Use filter() and lambda to get only names with more than 4 letters

names = ['alice', 'bob', 'charlie', 'david']
names_4 = list(filter(lambda name: len(name) > 4, names))

# Challenge C -- Use reduce() and lambda to find the sum of all numbers

numbers = [5, 10, 15, 20]
from functools import reduce
sum_num = reduce(lambda a, b: a + b, numbers)

'''
Using list comprehension, create a list of just the names of students who scored >= 50
Using filter() and lambda, get all student dictionaries where marks >= 50
Using map() and lambda, create a new list where each student gets 5 bonus marks (but keep it as dictionaries)
'''

students = [
    {'name': 'Alice', 'marks': 85},
    {'name': 'Bob', 'marks': 45},
    {'name': 'Charlie', 'marks': 92},
    {'name': 'David', 'marks': 58},
    {'name': 'Eve', 'marks': 34}
]

st_50 = [student['name'] for student in students if student['marks'] >= 50]
st_dict_50 = list(filter(lambda student: student['marks'] >= 50, students))
st_bonus = list(map(lambda student: {'name': student['name'], 'marks': student['marks'] + 5}, students))

'''
A parent class called Person with attributes like name and age
A child class called Student that inherits from Person but ALSO has additional attributes like student_id and marks
'''

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
        
class Student(Parent):
    def __init__(self, name, age, student_id, marks):
        super().__init__(name, age)
        self.student_id = student_id
        self.marks = marks
        
    def introduce(self):
        return super().introduce() + f" I am a student with ID {self.student_id} and I have scored {self.marks} marks."
        
parent1 = Parent("John", 45)
parent2 = Parent("Mary", 38)
student1 = Student("Abhinay", 20, "501", 95)
student2 = Student("Rohan", 21, "502", 88)
print()
print(parent1.introduce())
print(student1.introduce())
print(f"Student 1: Name={student1.name}, Age={student1.age}, ID={student1.student_id}, Marks={student1.marks}")
print(f"Student 2: Name={student2.name}, Age={student2.age}, ID={student2.student_id}, Marks={student2.marks}")
print()

# Library Management System

class Book:
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price
        
    def get_info(self):
        return f"Name: {self.title}, Author: {self.author}, Price: Rs{self.price}"
    
class DigitalBook(Book):
    def __init__(self, author, title, price, file_size):
        super().__init__(author, title, price)
        self.file_size = file_size
        
    def get_info(self):
        return super().get_info() + f", File Size: {self.file_size}MB"
    
books = [
    Book("Python Basics", "John Doe", 299),
    Book("Data Science", "Jane Smith", 499),
    DigitalBook("AI Fundamentals", "Bob Johnson", 399, 25),
    Book("Web Development", "Alice Brown", 349),
    DigitalBook("Machine Learning", "Charlie Davis", 599, 40)
]

plus350 = list(filter(lambda book: book.price > 350, books))
disc = list(map(lambda book: DigitalBook(book.author, book.title, book.price * 0.9, book.file_size) if isinstance(book, DigitalBook) else Book(book.author, book.title, book.price * 0.9), books))

print()
print("Books with price greater than Rs350:")
for book in plus350:
    print(book.get_info())
print("\nBooks after applying 10% discount:")
for book in disc:
    print(book.get_info())
print("Digital Books Info:")
for book in books:
    if isinstance(book, DigitalBook):
        print(book.get_info())
print()

# Recursive questions practice

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print()
print(factorial(5))