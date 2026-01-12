'''
Write a code to:
1. Create a tuple of only even numbers from the list using tuple comprehension
2. Find the sum of numbers divisible by 3 using filter() and reduce()
3. Create a new list where each number is squared, using map() and lambda
'''

numbers = [12, 45, 23, 67, 89, 34, 56, 78, 90, 11]

even_tuple = tuple(num for num in numbers if num % 2 == 0)
dvd = list(filter(lambda x: x % 3 == 0, numbers))
from functools import reduce
dvd_redce = reduce(lambda a, b: a + b, dvd)
squared_list = list(map(lambda x: x ** 2, numbers))
print("Tuple of even numbers:", even_tuple)
print("Sum of numbers divisible by 3:", dvd_redce)
print("List of squared numbers:", squared_list)
print()

'''
Write code to:
1. Use dictionary comprehension to create a new dict with only items having quantity > 25
2. Use lambda with sorted() to get a list of fruit names sorted by their quantities (descending)
'''

inventory = {
    'apples': 50,
    'bananas': 30,
    'oranges': 45,
    'grapes': 20,
    'mangoes': 15
}

high_qty = {fruit: qty for fruit, qty in inventory.items() if qty > 25}
srt = sorted(inventory.items(), key=lambda item: item[1], reverse=True)
sorted_fruits = [fruit for fruit, qty in srt]
print("Fruits with quantity > 25:", high_qty)
print("Fruits sorted by quantity (descending):", sorted_fruits)
print()

'''
Write code to find:
Elements in set_a but not in set_b (using set operation)
Elements common to both sets
All unique elements from both sets combined
'''

set_a = {1, 2, 3, 4, 5, 6}
set_b = {4, 5, 6, 7, 8, 9}

only_a = set_a - set_b
common = set_a & set_b
all_unique = set_a | set_b
print("Elements in set_a but not in set_b:", only_a)
print("Elements common to both sets:", common)
print("All unique elements from both sets combined:", all_unique)
print()

'''
Write a recursive function sum_digits(n) that:
1. Takes a positive integer as input
2. Returns the sum of its digits
3. Example: sum_digits(1234) returns 10 (1+2+3+4)
'''

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)
    
print("Sum of digits of 567:", sum_digits(567))
print("Sum of digits of 9:", sum_digits(9))

'''
Write functions using lambda and map/filter:
1. Convert all to Fahrenheit (Formula: F = C × 9/5 + 32)
2. Filter only temperatures above 50°F from the converted list
3. Calculate average of the filtered Fahrenheit temperatures using reduce()
'''

celsius_temps = [0, 10, 20, 30, 40, 100]

frh = list(map(lambda c: c * 9/5 + 32, celsius_temps))
high_frh = list(filter(lambda f: f > 50, frh))
from functools import reduce
avg_frh = reduce(lambda a, b: a + b, high_frh) / len(high_frh) if high_frh else 0

print("Fahrenheit temperatures:", frh)
print("Temperatures above 50°F:", high_frh)
print("Average of filtered Fahrenheit temperatures:", avg_frh)
print()

'''
Create a single list comprehension that generates a list of tuples:
1. Each tuple contains (number, square, cube)
2. For numbers from 1 to 10
3. But only include numbers that are either even OR divisible by 3
'''

num_tuples = [(n, n**2, n**3) for n in range(1, 11) if n % 2 == 0 or n % 3 == 0]
print("List of tuples (number, square, cube) for even numbers or divisible by 3:", num_tuples)
print()

'''
1. Base Class Employee:
    1. Attributes: name, emp_id, base_salary
    2. Method: calculate_salary() - returns base_salary
    3. Method: display_info() - returns formatted string with all details


2. Child Class Manager (inherits from Employee):
    1. Additional attribute: team_size
    2. Bonus: Rs. 500 per team member
    3. Override calculate_salary() to include bonus
    4. Override display_info() to include team size


3. Child Class Developer (inherits from Employee):
    1. Additional attribute: programming_languages (list)
    2. Bonus: Rs. 1000 per programming language known
    3. Override calculate_salary() to include bonus
    4. Override display_info() to show languages
    
    
Write code using lambda/map/filter/comprehensions to:
1. Get list of all employee names whose salary (calculated) is above 40000
2. Calculate total salary expense for all employees
3. Create a dictionary with emp_id as key and calculated salary as value (use dict comprehension)
4. Find the highest paid employee (return the object itself)
'''

class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def display_info(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Base Salary: Rs. {self.base_salary}"
    
class Manager(Employee):
    def __init__(self, name, emp_id, base_salary, team_size):
        super().__init__(name, emp_id, base_salary)
        self.team_size = team_size

    def calculate_salary(self):
        bonus = 500 * self.team_size
        return self.base_salary + bonus

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Team Size: {self.team_size}"
    
class Developer(Employee):
    def __init__(self, name, emp_id, base_salary, programming_languages):
        super().__init__(name, emp_id, base_salary)
        self.programming_languages = programming_languages

    def calculate_salary(self):
        bonus = 1000 * len(self.programming_languages)
        return self.base_salary + bonus

    def display_info(self):
        base_info = super().display_info()
        languages = ', '.join(self.programming_languages)
        return f"{base_info}, Programming Languages: {languages}"
    
employees = [
    Employee("Alice", "E001", 30000),
    Manager("Bob", "M001", 50000, 5),
    Developer("Charlie", "D001", 40000, ["Python", "Java", "C++"]),
    Employee("David", "E002", 28000),
    Developer("Eve", "D002", 45000, ["JavaScript", "React"])
]

high_salary_names = list(map(lambda emp: emp.name, filter(lambda emp: emp.calculate_salary() > 40000, employees)))
total_salary_expense = sum(map(lambda emp: emp.calculate_salary(), employees))
salary_dict = {emp.emp_id: emp.calculate_salary() for emp in employees}
highest_paid_employee = max(employees, key=lambda emp: emp.calculate_salary())

print("Employees with salary above 40000:", high_salary_names)
print("Total salary expense for all employees: Rs.", total_salary_expense)
print("Salary dictionary (emp_id: calculated_salary):", salary_dict)
print("Highest paid employee info:", highest_paid_employee.display_info())
print()