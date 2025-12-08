# Question 1 ---->
# A food-delivery company wants to analyse its daily delivery performance.
# Create a Python class DeliveryAnalysis that stores a list of delivery times (in minutes). Write the following methods:
# average_time() → returns the average delivery time
# fast_deliveries() → returns all deliveries under 30 minutes
# delayed_deliveries() → returns the count of deliveries above 45 minutes
# performance_category() → returns Excellent/Good/Average/Poor based on average
# display_report() → prints the complete performance report

class DeliveryAnalysis:
    def __init__(self, delivery_times):
        self.delivery_times = delivery_times

    def average_time(self):
        if len(self.delivery_times) == 0:
            return 0
        return sum(self.delivery_times) / len(self.delivery_times)

    def fast_deliveries(self):
        return [time for time in self.delivery_times if time < 30]

    def delayed_deliveries(self):
        return sum(1 for time in self.delivery_times if time > 45)

    def performance_category(self):
        avg_time = self.average_time()
        if avg_time < 20:
            return "Excellent"
        elif avg_time < 35:
            return "Good"
        elif avg_time < 50:
            return "Average"
        else:
            return "Poor"

    def display_report(self):
        avg_time = self.average_time()
        fast_count = len(self.fast_deliveries())
        delayed_count = self.delayed_deliveries()
        category = self.performance_category()
        
        report = (
            f"Average Delivery Time: {avg_time:.2f} minutes\n"
            f"Fast Deliveries (under 30 mins): {fast_count}\n"
            f"Delayed Deliveries (over 45 mins): {delayed_count}\n"
            f"Performance Category: {category}"
        )
        print(report)
        

print()
delivery_times = [25, 35, 45, 20, 50, 15, 60, 30, 40, 55]
print(f"The Different Times for 10 Deliveries are: {delivery_times}")
analysis = DeliveryAnalysis(delivery_times)
analysis.display_report()
print()


        
# Question 2 ---->        
# Create a class WeatherReport that stores temperatures of 7 days.
# Include methods to:
# Compute average temperature
# Find hottest and coldest day
# Classify weather as Hot / Moderate / Cold
# Create an object using sample temperature values.

class WeatherReport:
    def __init__(self, temperatures):
        self.temperatures = temperatures

    def average_temperature(self):
        if len(self.temperatures) == 0:
            return 0
        return sum(self.temperatures) / len(self.temperatures)

    def hottest_day(self):
        return max(self.temperatures)

    def coldest_day(self):
        return min(self.temperatures)

    def weather_classification(self):
        avg_temp = self.average_temperature()
        if avg_temp > 30:
            return "Hot"
        elif avg_temp > 15:
            return "Moderate"
        else:
            return "Cold"

    def display_report(self):
        avg_temp = self.average_temperature()
        hottest = self.hottest_day()
        coldest = self.coldest_day()
        classification = self.weather_classification()
        
        report = (
            f"Average Temperature: {avg_temp:.2f}°C\n"
            f"Hottest Day: {hottest}°C\n"
            f"Coldest Day: {coldest}°C\n"
            f"Weather Classification: {classification}"
        )
        print(report)
        

print()
temperatures = [32, 28, 35, 30, 25, 20, 15]
print(f"The Different Temperatures for 7 days are: {temperatures}")
weather_report = WeatherReport(temperatures)
weather_report.display_report()
print()



# Question 3 ---->
# Create a Python class Employee that stores an employee’s name, basic salary, and bonus percentage.
# Write methods to:
# Calculate total salary
# Check whether salary is above ₹50,000
# Display employee details
# Create an object for one employee and show the complete report.


class Employee:    
    def __init__(self, name, basic_salary, bonus_percentage):
        self.name = name
        self.basic_salary = basic_salary
        self.bonus_percentage = bonus_percentage
    def total_salary(self):
        bonus_amount = (self.bonus_percentage / 100) * self.basic_salary
        return self.basic_salary + bonus_amount
    def is_salary_above_50000(self):
        return self.total_salary() > 50000
    def display_employee_details(self):
        total_sal = self.total_salary()
        salary_status = "above ₹50,000" if self.is_salary_above_50000() else "below ₹50,000"
        details = (
            f"Employee Name: {self.name}\n"
            f"Basic Salary: ₹{self.basic_salary:.2f}\n"
            f"Bonus Percentage: {self.bonus_percentage}%\n"
            f"Total Salary: ₹{total_sal:.2f}\n"
            f"Salary Status: {salary_status}"
        )
        print(details)
        
print()
employee = Employee("Abhinay", 450000, 15)
employee2 = Employee("Ravi", 40000, 10)
employee.display_employee_details()
print()
employee2.display_employee_details()
print()