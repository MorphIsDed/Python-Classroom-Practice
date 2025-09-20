# Make a menu driven program using dictionary in which we input marks of 5 students and the user has option to chck the highest, lowest and the average marks.

marks = {}
for i in range(1, 6):
    student_name = input(f"Enter the name of student {i}: ")
    student_marks = float(input(f"Enter the marks of {student_name}: "))
    marks[student_name] = student_marks

def highest_marks(marks):
    highest_student = max(marks, key=marks.get)
    return highest_student, marks[highest_student]

def lowest_marks(marks):
    lowest_student = min(marks, key=marks.get)
    return lowest_student, marks[lowest_student]

def average_marks(marks):
    avg = sum(marks.values()) / len(marks)
    return avg

def individual_marks(marks):
    for student, score in marks.items():
        print(f"{student}: {score}")
    
while True:
    print()
    print("Menu:")
    print("1. Check Highest Marks")
    print("2. Check Lowest Marks")
    print("3. Check Average Marks")
    print("4. Check Individual Marks")
    print("0. Exit")
    choice = int(input("Enter your choice (1-4): "))
    print()
    if choice == 1:
        student, score = highest_marks(marks)
        print(f"The highest marks are {score} scored by {student}.")
    elif choice == 2:
        student, score = lowest_marks(marks)
        print(f"The lowest marks are {score} scored by {student}.")
    elif choice == 3:
        avg = average_marks(marks)
        print(f"The average marks of the students are {avg}.")
    elif choice == 4:
        print("Individual Marks:")
        individual_marks(marks)
    elif choice == 0:
        print("Thank you for using the program.")
        break
    else:
        print("Invalid choice! Please select a valid option.")