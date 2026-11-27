
import sys

def calculate_wages(daily_wage, working_days):
    return daily_wage * working_days

name = input("Enter employee name: ")
daily_wage = float(input("Enter daily wage: "))
working_days = int(input("Enter working days: "))

total = calculate_wages(daily_wage, working_days)
danuu

print("\n----- Employee Salary Details -----")
print("Employee Name:", name)
print("Daily Wage:", daily_wage)
print("Working Days:", working_days)
print("Total Wages:", total)
