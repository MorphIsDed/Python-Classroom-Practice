# Question 1 --->
# a) Convert all employees into a set to remove duplicates.
# b) Using set operations, find the employees who are absent in the second list but present in the first list.
# c) Create a dictionary attendance_record where keys are employee names and values are "Present" or "Absent".
# d) Add a new employee "Meena" into the attendance system (initiall marked absent). Use a dictionary method.

print()
print("Question 1 --->")
print()

all_employees = ["Rohan", "Sneha", "Amit", "Sneha", "Priya", "Amit"]
present_today = ("Rohan", "Priya", "Amit")

# a) Convert all employees into a set to remove duplicates.
print()
unique_employees = set(all_employees)
print("Unique Employees:", unique_employees)

# b) Using set operations, find the employees who are absent in the second list but present in the first list.
print()
absent_employees = unique_employees - set(present_today)
print("Absent Employees:", absent_employees)

# c) Create a dictionary attendance_record where keys are employee names and values are "Present" or "Absent".
print()
attendance_record = {employee: ("Present" if employee in present_today else "Absent") for employee in unique_employees}
print("Attendance Record:", attendance_record)

# d) Add a new employee "Meena" into the attendance system (initially marked absent). Use a dictionary method.
print()
attendance_record.setdefault("Meena", "Absent")
print("Updated Attendance Record:", attendance_record)
print()



# Question 2 --->
# a) Covert the movie list into a set to find unique movies.
# b) Add a new rating 3 for "Dunkirk" using list methods.
# c) Write a function average_rating(movie_name) that returns average rating using the dictionary.
# d) Convert the final dictionary keys into tuple and print it.

print()
print("Question 2 --->")
print()

movies = ["Inception", "Interstellar", "Dunkirk", "Inception"]
user_ratings = {
    "Inception": [5, 4, 5],
    "Interstellar": [5, 5],
    "Dunkirk": [4]
}

# a) Convert the movie list into a set to find unique movies.
print()
unique_movies = set(movies)
print("Unique Movies:", unique_movies)

# b) Add a new rating 3 for "Dunkirk" using list methods.
print()
user_ratings["Dunkirk"].append(3)
print("Updated Ratings for Dunkirk:", user_ratings["Dunkirk"])

# c) Write a function average_rating(movie_name) that returns average rating using the dictionary.
print()
def average_rating(movie_name):
    ratings = user_ratings.get(movie_name, [])
    if not ratings:
        return "No ratings available for this movie."
    return sum(ratings) / len(ratings)

movie_to_check = "Dunkirk"
avg_rating = average_rating(movie_to_check)
print(f"Average rating for {movie_to_check}: {avg_rating}")

# d) Convert the final dictionary keys into tuple and print it.
print()
movie_keys_tuple = tuple(user_ratings.keys())
print("Movie Keys as Tuple:", movie_keys_tuple)
print()