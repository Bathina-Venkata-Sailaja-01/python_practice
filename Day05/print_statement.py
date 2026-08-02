# ==================================================
# Day 05 - Print Statement in Python
# ==================================================

# --------------------------------------------------
# Example 1: Print a Calculated Result
# --------------------------------------------------

n1 = eval(input("Enter n1: "))
n2 = eval(input("Enter n2: "))
n3 = eval(input("Enter n3: "))

average = (n1 + n2 + n3) / 3
print("Average =", average)

print("-" * 50)

# --------------------------------------------------
# Example 2: Hardcoded Output
# --------------------------------------------------

print("The addition of 10,20,30 is: 60")

print("-" * 50)

# --------------------------------------------------
# Example 3: Printing Variable Names
# --------------------------------------------------

print("The addition of n1, n2, n3 is: add")

print("-" * 50)

# --------------------------------------------------
# Example 4: Printing Variables Using Commas
# --------------------------------------------------

n1 = eval(input("Enter n1: "))
n2 = eval(input("Enter n2: "))
n3 = eval(input("Enter n3: "))

add = n1 + n2 + n3

print("The addition of", n1, ",", n2, ",", n3, "is:", add)

print("-" * 50)

# --------------------------------------------------
# Example 5: Using format()
# --------------------------------------------------

n1 = eval(input("Enter n1: "))
n2 = eval(input("Enter n2: "))
n3 = eval(input("Enter n3: "))

add = n1 + n2 + n3

print("The addition of {}, {}, {} is: {}".format(n1, n2, n3, add))

print("-" * 50)

# --------------------------------------------------
# Example 6: Using f-Strings
# --------------------------------------------------

n1 = eval(input("Enter n1: "))
n2 = eval(input("Enter n2: "))
n3 = eval(input("Enter n3: "))

add = n1 + n2 + n3

print(f"The addition of {n1}, {n2}, and {n3} is: {add}")

print("-" * 50)

# --------------------------------------------------
# Example 7: Printing Multiple Values
# --------------------------------------------------

name = "Sailu"
age = 22
course = "Python"

print(name, age, course)

print("-" * 50)

# --------------------------------------------------
# Example 8: Using sep Parameter
# --------------------------------------------------

print(10, 20, 30, sep="-")
print(10, 20, 30, sep=" -> ")
print("2026", "08", "02", sep="/")

print("-" * 50)

# --------------------------------------------------
# Example 9: Using end Parameter
# --------------------------------------------------

print("Hello", end=" ")
print("World")

print("Python", end=" --> ")
print("Programming")

print()

print("-" * 50)

# --------------------------------------------------
# Example 10: Printing Different Data Types
# --------------------------------------------------

print(100)
print(10.5)
print(True)
print("Python")
print([10, 20, 30])
print((1, 2, 3))
print({"name": "Sailu", "age": 22})

print("-" * 50)

# --------------------------------------------------
# Example 11: Printing Arithmetic Expressions
# --------------------------------------------------

print("10 + 20 =", 10 + 20)
print("15 * 4 =", 15 * 4)
print("100 / 5 =", 100 / 5)

print("-" * 50)

# --------------------------------------------------
# Example 12: Escape Characters
# --------------------------------------------------

print("Hello\nWorld")
print("Python\tProgramming")
print("He said, \"Python is easy!\"")

print("-" * 50)

# --------------------------------------------------
# Example 13: Printing Quotes
# --------------------------------------------------

print("I'm learning Python")
print('He said, "Python is easy."')

print("-" * 50)

# --------------------------------------------------
# Example 14: Printing Special Symbols
# --------------------------------------------------

print("*" * 30)
print("=" * 30)
print("#" * 30)

print("-" * 50)

# --------------------------------------------------
# Example 15: Printing Variables with Labels
# --------------------------------------------------

name = "Sailu"
age = 22
city = "Hyderabad"

print("Name :", name)
print("Age  :", age)
print("City :", city)

print("-" * 50)

# --------------------------------------------------
# Example 16: Printing a Simple Table
# --------------------------------------------------

print("Name\tAge\tCity")
print("Sailu\t22\tHyderabad")
print("Ravi\t21\tChennai")
print("Kiran\t23\tBangalore")

print("-" * 50)

# --------------------------------------------------
# Example 17: Printing a Pattern
# --------------------------------------------------

print("*")
print("**")
print("***")
print("****")
print("*****")

print("-" * 50)

# --------------------------------------------------
# Example 18: Mixing Strings and Variables
# --------------------------------------------------

language = "Python"
version = 3.14

print(f"I am learning {language} version {version}.")

print("-" * 50)

# --------------------------------------------------
# End of Day 05
# --------------------------------------------------
print("Day 05 - Print Statement Examples Completed!")