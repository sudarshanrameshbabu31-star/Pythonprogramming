# Input: get values from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))

# Calculation
next_year_age = age + 1

# Output: display values
print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print(f"Next year, you will be {next_year_age} years old.")

# Check data types
print(type(name))
print(type(age))
print(type(salary))