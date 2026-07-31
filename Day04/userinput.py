# ==========================================
# Python User Input Examples
# ==========================================

# ------------------------------------------
# Example 1: String Input
# ------------------------------------------
name = input("Enter your name: ")
print("Hello,", name)

print("-" * 40)

# ------------------------------------------
# Example 2: Integer Input
# ------------------------------------------
age = int(input("Enter your age: "))
print("Your age is:", age)

print("-" * 40)

# ------------------------------------------
# Example 3: Float Input
# ------------------------------------------
height = float(input("Enter your height (in meters): "))
print("Your height is:", height)

print("-" * 40)

# ------------------------------------------
# Example 4: Two Integer Inputs
# ------------------------------------------
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", num1 + num2)
print("Difference =", num1 - num2)
print("Product =", num1 * num2)
print("Division =", num1 / num2)

print("-" * 40)

# ------------------------------------------
# Example 5: Multiple Inputs in One Line
# ------------------------------------------
a, b = map(int, input("Enter two numbers separated by space: ").split())

print("First Number :", a)
print("Second Number:", b)
print("Sum =", a + b)

print("-" * 40)

# ------------------------------------------
# Example 6: Checking Data Type
# ------------------------------------------
value = input("Enter any value: ")
print("You entered:", value)
print("Data Type:", type(value))

print("-" * 40)

# ------------------------------------------
# Example 7: Real-Time Example
# Rectangle Area
# ------------------------------------------
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of Rectangle =", area)

print("-" * 40)

# ------------------------------------------
# Example 8: eval() - Integer Input
# ------------------------------------------
num = eval(input("Enter an integer: "))
print("Value:", num)
print("Data Type:", type(num))

print("-" * 40)

# ------------------------------------------
# Example 9: eval() - Float Input
# ------------------------------------------
num = eval(input("Enter a float value: "))
print("Value:", num)
print("Data Type:", type(num))

print("-" * 40)

# ------------------------------------------
# Example 10: eval() - Boolean Input
# ------------------------------------------
value = eval(input("Enter True or False: "))
print("Value:", value)
print("Data Type:", type(value))

print("-" * 40)

# ------------------------------------------
# Example 11: eval() - List Input
# ------------------------------------------
data = eval(input("Enter a list: "))
print("List:", data)
print("Data Type:", type(data))

print("-" * 40)

# ------------------------------------------
# Example 12: eval() - Tuple Input
# ------------------------------------------
data = eval(input("Enter a tuple: "))
print("Tuple:", data)
print("Data Type:", type(data))

print("-" * 40)

# ------------------------------------------
# Example 13: eval() - Dictionary Input
# ------------------------------------------
data = eval(input("Enter a dictionary: "))
print("Dictionary:", data)
print("Data Type:", type(data))

print("-" * 40)

# ------------------------------------------
# Example 14: eval() - Mathematical Expression
# ------------------------------------------
result = eval(input("Enter a mathematical expression: "))
print("Result =", result)

print("-" * 40)

# ------------------------------------------
# Example 15: eval() - Complex Number
# ------------------------------------------
num = eval(input("Enter a complex number: "))
print("Value:", num)
print("Data Type:", type(num))

print("-" * 40)

# ------------------------------------------
# End of Program
# ------------------------------------------
print("All user input examples completed successfully!")