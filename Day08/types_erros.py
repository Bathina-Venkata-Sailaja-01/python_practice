# ==============================================================
# TYPES OF ERRORS IN PYTHON
# ==============================================================

"""
This file contains examples of different types of
errors in Python.

Each error contains at least 3 examples.

IMPORTANT:
The error-producing statements are commented out.
Remove the # before an example to see the error.
"""

# ==============================================================
# 1. SYNTAX ERROR
# ==============================================================

"""
SyntaxError occurs when Python syntax/grammar is incorrect.
"""

# Example 1: Missing closing parenthesis

# print("Hello"

# Example 2: Missing colon

# if age >= 18

# print("Eligible")

# Example 3: Incorrect syntax in a for loop

# for i in range(5)

# print(i)

# ==============================================================

# 2. INDENTATION ERROR

# ==============================================================

"""
IndentationError occurs when the indentation of
Python code is incorrect.
"""

# Example 1: Missing indentation

#

# if True:

# print("Hello")

# Example 2: Unexpected indentation

#

# x = 10

# y = 20

# Example 3: Incorrect indentation inside a function

#

# def greet():

# print("Hello")

# ==============================================================

# 3. NAME ERROR

# ==============================================================

"""
NameError occurs when we try to use a variable or
function that has not been defined.
"""

# Example 1: Variable does not exist

# print(student_name)

# Example 2: Typing mistake in variable name

#

# age = 21

# print(ag)

# Example 3: Function does not exist

# calculate()

# ==============================================================

# 4. TYPE ERROR

# ==============================================================

"""
TypeError occurs when an operation is performed
between incompatible data types.
"""

# Example 1: Adding string and integer

#

# name = "Sailaja"

# age = 21

# print(name + age)

# Example 2: Dividing string by integer

#

# number = "100"

# print(number / 2)

# Example 3: Calling an integer as a function

#

# number = 10

# number()

# ==============================================================

# 5. VALUE ERROR

# ==============================================================

"""
ValueError occurs when the data type is correct,
but the given value is not appropriate.
"""

# Example 1: Converting letters into integer

#

# number = int("abc")

# Example 2: Converting decimal string directly into integer

#

# number = int("10.5")

# Example 3: Converting invalid value to float

#

# price = float("hello")

# ==============================================================

# 6. ZERO DIVISION ERROR

# ==============================================================

"""
ZeroDivisionError occurs when we try to divide a number
by zero.
"""

# Example 1: Normal division

#

# result = 10 / 0

# Example 2: Floor division

#

# result = 20 // 0

# Example 3: Modulus operation

#

# result = 25 % 0

# ==============================================================

# 7. INDEX ERROR

# ==============================================================

"""
IndexError occurs when we try to access an index
that does not exist.
"""

# Example 1: List index out of range

#

# numbers = [10, 20, 30]

# print(numbers[5])

# Example 2: String index out of range

#

# name = "Python"

# print(name[10])

# Example 3: Tuple index out of range

#

# values = (100, 200, 300)

# print(values[4])

# ==============================================================

# 8. KEY ERROR

# ==============================================================

"""
KeyError occurs when we try to access a dictionary
key that does not exist.
"""

# Example 1: Missing key

#

# student = {

# "name": "Sailaja",

# "age": 21

# }

#

# print(student["marks"])

# Example 2: Incorrect spelling of key

#

# employee = {

# "name": "Rahul",

# "salary": 30000

# }

#

# print(employee["Salary"])

# Example 3: Accessing a non-existing key

#

# products = {

# "laptop": 50000,

# "mobile": 20000

# }

#

# print(products["tablet"])

# ==============================================================

# 9. ATTRIBUTE ERROR

# ==============================================================

"""
AttributeError occurs when an object does not have
the attribute or method we are trying to access.
"""

# Example 1: Invalid string method

#

# name = "Python"

# print(name.upper_case())

# Example 2: Invalid list method

#

# numbers = [10, 20, 30]

# numbers.push(40)

# Example 3: Invalid integer attribute

#

# number = 100

# print(number.length)

# ==============================================================

# 10. MODULE NOT FOUND ERROR

# ==============================================================

"""
ModuleNotFoundError occurs when Python cannot find
the module that we are trying to import.
"""

# Example 1: Non-existing module

#

# import abcxyz

# Example 2: Misspelled module name

#

# import mathh

# Example 3: Non-existing package

#

# import my_unknown_package

# ==============================================================

# 11. FILE NOT FOUND ERROR

# ==============================================================

"""
FileNotFoundError occurs when we try to open a file
that does not exist.
"""

# Example 1: File does not exist

#

# file = open("student.txt", "r")

# Example 2: Incorrect file name

#

# file = open("student_data.csv", "r")

# Example 3: Incorrect file path

#

# file = open("C:/Python/Data/example.txt", "r")

# ==============================================================

# 12. OVERFLOW ERROR

# ==============================================================

"""
OverflowError occurs when a numerical calculation
produces a result that is too large for the operation.
"""

# Example 1: Very large exponential value

#

# import math

# result = math.exp(1000)

# Example 2: Another large exponential value

#

# import math

# result = math.exp(10000)

# Example 3: Large power converted to float

#

# number = float(10 ** 1000)

# ==============================================================

# 13. RECURSION ERROR

# ==============================================================

"""
RecursionError occurs when a function keeps calling
itself without reaching a stopping condition.
"""

# Example 1: Function calls itself forever

#

# def test():

# test()

#

# test()

# Example 2: Recursive function without base condition

#

# def count(n):

# print(n)

# count(n + 1)

#

# count(1)

# Example 3: Infinite recursion

#

# def hello():

# hello()

#

# hello()

# ==============================================================

# 14. UNBOUND LOCAL ERROR

# ==============================================================

"""
UnboundLocalError occurs when a local variable is
used before it has been assigned a value.
"""

# Example 1:

#

# x = 10

#

# def test():

# print(x)

# x = 20

#

# test()

# Example 2:

#

# def calculate():

# print(total)

# total = 100

#

# calculate()

# Example 3:

#

# def student():

# print(name)

# name = "Sailaja"

#

# student()

# ==============================================================

# 15. LOGICAL ERROR

# ==============================================================

"""
Logical Error occurs when the program runs successfully,
but the output is incorrect because the logic is wrong.

Logical errors do NOT normally display an error message.
"""

# Example 1: Incorrect average calculation

#

# a = 10

# b = 20

#

# average = a + b / 2

#

# Expected output: 15

# Actual output: 20

# Correct logic:

a = 10
b = 20

average = (a + b) / 2

print("Correct Average:", average)

# Example 2: Incorrect condition

#

# age = 20

#

# if age > 18:

# print("Eligible")

# else:

# print("Not Eligible")

#

# This may be logically incorrect if 18 should also be eligible.

# Correct logic:

age = 18

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Example 3: Incorrect multiplication

#

# length = 10

# width = 5

#

# # Wrong formula

# area = length + width

#

# Expected: 50

# Actual: 15

# Correct logic:

length = 10
width = 5

area = length * width

print("Area:", area)

# ==============================================================

# SUMMARY

# ==============================================================

print("\n" + "=" * 60)
print("TYPES OF ERRORS IN PYTHON")
print("=" * 60)

print("1.  SyntaxError")
print("2.  IndentationError")
print("3.  NameError")
print("4.  TypeError")
print("5.  ValueError")
print("6.  ZeroDivisionError")
print("7.  IndexError")
print("8.  KeyError")
print("9.  AttributeError")
print("10. ModuleNotFoundError")
print("11. FileNotFoundError")
print("12. OverflowError")
print("13. RecursionError")
print("14. UnboundLocalError")
print("15. Logical Error")

print("=" * 60)
print("Each error has 3 examples in this file.")
print("Uncomment an example to test the error.")
print("=" * 60)
