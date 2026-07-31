# 📘 Day 02 - User Input in Python

## 🎯 Objective

Learn how to take input from the user using Python's built-in `input()` function and convert it into the required data type.

---

# 📖 What is User Input?

User input allows a program to receive data from the keyboard while it is running. This makes programs interactive because they can perform different operations based on the values entered by the user.

Python provides the **`input()`** function to accept input from the keyboard.

---

# 📝 Syntax

```python
variable = input("Enter a value: ")
```

### Example

```python
name = input("Enter your name: ")
print("Hello,", name)
```

### Output

```
Enter your name: Sailu
Hello, Sailu
```

---

# ⚙️ How `input()` Works

1. Displays the message inside `input()`.
2. Waits for the user to enter a value.
3. Stores the entered value in a variable.
4. Returns the value as a **string (`str`)**.

---

# 🔍 Return Type of `input()`

The `input()` function always returns a **string**, regardless of what the user enters.

```python
value = input("Enter something: ")
print(type(value))
```

### Output

```
Enter something: 100
<class 'str'>
```

---

# 🔄 Type Conversion

To perform mathematical operations, convert the input into the required data type.

| Function | Converts To | Example |
|----------|-------------|---------|
| `int()` | Integer | `int(input())` |
| `float()` | Float | `float(input())` |
| `str()` | String | `str(100)` |
| `bool()` | Boolean | `bool(1)` → `True` |
| `eval()` | Automatically evaluates the input | `eval(input())` |

---

# 📖 What is `eval()`?

`eval()` is a built-in Python function that **evaluates a string as a Python expression** and returns the corresponding value.

It is commonly used when you want Python to automatically determine the data type of the entered value.

### Syntax

```python
variable = eval(input("Enter a value: "))
```

### How `eval()` Works

1. `input()` accepts the user's input as a string.
2. `eval()` evaluates that string.
3. Python converts it into its actual data type.

---

### Examples

#### Integer Input

```python
num = eval(input("Enter a number: "))
print(num)
print(type(num))
```

**Input**

```
25
```

**Output**

```
25
<class 'int'>
```

---

#### Float Input

```python
num = eval(input("Enter a number: "))
print(type(num))
```

**Input**

```
12.5
```

**Output**

```
<class 'float'>
```

---

#### Boolean Input

```python
value = eval(input("Enter value: "))
print(type(value))
```

**Input**

```
True
```

**Output**

```
<class 'bool'>
```

---

#### List Input

```python
data = eval(input("Enter a list: "))
print(data)
print(type(data))
```

**Input**

```
[10, 20, 30]
```

**Output**

```
[10, 20, 30]
<class 'list'>
```

---

#### Tuple Input

```python
data = eval(input("Enter a tuple: "))
print(type(data))
```

**Input**

```
(1, 2, 3)
```

**Output**

```
<class 'tuple'>
```

---

#### Dictionary Input

```python
data = eval(input("Enter a dictionary: "))
print(type(data))
```

**Input**

```
{"name":"Sailu","age":22}
```

**Output**

```
<class 'dict'>
```

---

#### Mathematical Expression

```python
result = eval(input("Enter expression: "))
print(result)
```

**Input**

```
10+20*3
```

**Output**

```
70
```

---

# 📌 Difference Between `int()` and `eval()`

| `int()`                     | `eval()`                                                      |
|-----------------------------|---------------------------------------------------------------|
| Converts only integer values| Evaluates any valid Python expression                         |
| `int("10")` → `10`          | `eval("10")` → `10`                                           |
| `int("10.5")` → Error       | `eval("10.5")` → `10.5`                                       |
| Cannot evaluate expressions | Can evaluate expressions like `10+20`                         |
| Returns only `int`          | Returns `int`, `float`, `list`, `tuple`, `dict`, `bool`, etc. |

---

# ⚠️ Note About `eval()`

Although `eval()` is useful for learning, **it is not recommended for real-world applications** because it can execute any Python code entered by the user, which may create security risks.

Use `int()`, `float()`, or other specific conversion functions whenever possible.

---

# 💻 Examples

## 1️⃣ String Input

```python
name = input("Enter your name: ")
print("Hello,", name)
```

---

## 2️⃣ Integer Input

```python
age = int(input("Enter your age: "))
print("Age:", age)
```

---

## 3️⃣ Float Input

```python
height = float(input("Enter your height: "))
print("Height:", height)
```

---

## 4️⃣ Using `eval()`

```python
num = eval(input("Enter a value: "))
print(num)
print(type(num))
```

---

## 5️⃣ Two Integer Inputs

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
```

---

## 6️⃣ Multiple Inputs in One Line

```python
a, b = map(int, input("Enter two numbers: ").split())

print("Sum =", a + b)
```

---

# 🌍 Real-Time Applications

User input is used in many real-world applications, including:

- 🔐 Login Systems
- 🏧 ATM Machines
- 🛒 Online Shopping Websites
- 🎓 Student Management Systems
- 🏦 Banking Applications
- 🧮 Calculator Programs
- 🧾 Billing Systems
- 🎫 Ticket Booking Applications
- 📋 Online Surveys
- 🎮 Games

---

# ❌ Common Mistake

### Incorrect

```python
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)
```

### Input

```
10
20
```

### Output

```
1020
```

**Reason:** Both values are stored as strings, so they are concatenated.

---

### Correct

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
```

### Output

```
30
```

---

# ✅ Advantages of User Input

- Makes programs interactive.
- Accepts dynamic values from users.
- Eliminates hardcoded values.
- Improves flexibility and reusability.
- Useful for real-world applications.

---

# 📝 Practice Programs

1. Read your name and print a welcome message.
2. Read your age and display it.
3. Read two numbers and calculate their sum.
4. Find the area of a rectangle.
5. Find the area of a circle.
6. Calculate the average of three numbers.
7. Convert Celsius to Fahrenheit.
8. Calculate a student's percentage.
9. Calculate the total bill of a product.
10. Swap two numbers without using a third variable.
11. Take input using `eval()` and display its data type.
12. Evaluate a mathematical expression entered by the user.

---

# 🎤 Interview Questions

### 1. Which function is used to take user input in Python?

**Answer:** `input()`

---

### 2. What is the return type of `input()`?

**Answer:** `str`

---

### 3. Why do we use `int()` with `input()`?

**Answer:** Because `input()` returns a string. `int()` converts it into an integer so mathematical operations can be performed.

---

### 4. What does `eval()` do?

**Answer:** `eval()` evaluates the input string as a Python expression and returns the corresponding data type or result.

---

### 5. How do you take multiple inputs in one line?

```python
a, b = map(int, input().split())
```

---

### 6. What is the difference between `input()` and `print()`?

| `input()`                  | `print()`                   |
|----------------------------|-----------------------------|
| Accepts data from the user | Displays data on the screen |
| Returns the entered value  | Displays output             |
| Makes programs interactive | Shows results               |

---

# 📚 Summary

- `input()` is used to take input from the keyboard.
- It always returns a **string (`str`)**.
- Use `int()` for integers and `float()` for decimal numbers.
- `eval()` automatically evaluates the entered value and returns its actual data type.
- `eval()` can also evaluate mathematical expressions.
- Avoid using `eval()` in production applications due to security risks.
- Use `map()` and `split()` to accept multiple values in one line.

---

## 📂 Folder Structure

```
Day02/
│── userinput.py
│── README.md
```

---

# 💻 Happy Coding!

> **"The better you understand data types today, the easier it becomes to master Python tomorrow."** 🚀
````