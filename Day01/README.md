# 📘 Day 01 - Variables in Python

## 🎯 Objective

Learn what variables are, how to create them, the rules for naming variables, and their importance in Python programming.

---

# 📖 What are Variables?

A **variable** is a **storage location** used to store data in a program.

The stored data can be of different types, such as:

- Integer
- Float
- String
- Boolean
- List
- Tuple
- Dictionary
- Set

A variable acts like a **container** that holds a value, which can be changed whenever needed.

---

# 📝 Syntax

```python
variable_name = value
```

### Example

```python
age = 22
name = "Sailu"
cgpa = 8.9

print(age)
print(name)
print(cgpa)
```

### Output

```
22
Sailu
8.9
```

---

# 🔄 Variable Reassignment

Variables can be modified by assigning a new value.

```python
age = 22
print(age)

age = 23
print(age)
```

### Output

```
22
23
```

---

# 📝 Assigning Multiple Variables

## Different Values

You can assign different values to multiple variables in a single line.

```python
name, age, city = "Sailu", 22, "Hyderabad"

print(name)
print(age)
print(city)
```

---

## Same Value

You can assign the same value to multiple variables.

```python
a = b = c = 100

print(a)
print(b)
print(c)
```

---

# ❌ Invalid Assignment

One value **cannot belong to multiple variables in the same assignment expression** like this:

```python
100 = a = b
```

This is **invalid** because values cannot be assigned to variables in reverse order.

### Easy Analogy

Think of variables as **bags**.

- ✅ You can put many apples into different bags by assigning values correctly.
- ✅ You can give the same type of apple to many bags.
- ❌ But you cannot make the apple itself become the bag.

---

# 📋 Rules for Naming Variables

## ✅ Rule 1: Start with a Letter or Underscore

A variable name must begin with:

- Letters (`A-Z`, `a-z`)
- Underscore (`_`)

### Valid Examples

```python
name = "Sailu"
Name = "Python"
_python = 100
```

---

## ✅ Rule 2: Can Contain Letters, Numbers, and Underscores

### Valid Examples

```python
student123 = "Sailu"
python_course = "Python"
data2026 = 100
```

---

## ❌ Rule 3: Cannot Start with Numbers

### Invalid Examples

```python
123name = "Sailu"
2026data = 100
```

---

## ❌ Rule 4: Cannot Start with Special Characters

### Invalid Examples

```python
@name = "Python"
$name = "Python"
%marks = 90
&course = "Python"
```

---

## ❌ Rule 5: Spaces Are Not Allowed

Variable names cannot contain spaces.

### Invalid

```python
python practice = "Python"
```

### Valid

```python
python_practice = "Python"
pythonPractice = "Python"
```

---

## ❌ Rule 6: Cannot Use Python Keywords

Python keywords have predefined meanings and cannot be used as variable names.

### Invalid Examples

```python
if = 10
for = 20
while = 30
class = "Python"
```

---

## ✅ Rule 7: Variables are Case Sensitive

Python treats uppercase and lowercase letters as different variables.

```python
name = "Sailu"
Name = "Python"

print(name)
print(Name)
```

### Output

```
Sailu
Python
```

---

# 🔍 Checking Variable Type

Use the `type()` function to identify the data type stored in a variable.

```python
name = "Sailu"
age = 22
cgpa = 8.5

print(type(name))
print(type(age))
print(type(cgpa))
```

### Output

```
<class 'str'>
<class 'int'>
<class 'float'>
```

---

# 🌍 Real-Time Examples

## Example 1: Student Information

```python
name = "Sailu"
age = 22
course = "Data Science"
```

---

## Example 2: Employee Details

```python
employee_name = "Rahul"
salary = 50000
department = "IT"
```

---

## Example 3: Shopping Cart

```python
product = "Laptop"
price = 55000
quantity = 2
```

---

## Example 4: Bank Account

```python
account_holder = "Sailu"
balance = 25000.75
```

---

## Example 5: Online Registration

```python
username = "python_user"
password = "********"
```

---

# ✅ Advantages of Variables

- Makes programs easy to understand.
- Avoids repeating values.
- Makes code reusable.
- Easy to update values.
- Improves code readability.
- Simplifies calculations and data storage.

---

# ❌ Disadvantages of Variables

- Poor naming makes code difficult to understand.
- Using many unnecessary variables increases memory usage.
- Reassigning values incorrectly can produce unexpected results.
- Similar variable names may confuse beginners.

---

# 📝 Summary

- Variables are used to store data.
- Values stored in variables can be changed.
- Variables can hold different data types.
- Multiple variables can be assigned in one line.
- The same value can be assigned to multiple variables.
- Variable names must follow Python naming rules.
- Variables are case-sensitive.
- Use `type()` to identify the data type of a variable.

---

# 📂 Folder Structure

```
Day01/
│── variables.py
│── README.md
```

---

# 💻 Happy Coding!

> **"Good variable names make code easy to read, understand, and maintain."** 🚀
````
