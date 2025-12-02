# Write a python class student with attributes name, roll no and marks. Write a method to find and calculate the average marks along with their details.

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def average_marks(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def student_details(self):
        avg_marks = self.average_marks()
        return f"Name: {self.name}, Roll No: {self.roll_no}, Average Marks: {avg_marks:.2f}"
    
# Example usage:
student1 = Student("Alice", 101, [85, 90, 78])
student2 = Student("Bob", 102, [88, 76, 92])
student3 = Student("Charlie", 103, [90, 91, 89])
student4 = Student("David", 104, [70, 75, 80])
student5 = Student("Eve", 105, [95, 100, 98])

print()
print(student1.student_details())
print(student2.student_details())
print(student3.student_details())
print(student4.student_details())
print(student5.student_details())
print()