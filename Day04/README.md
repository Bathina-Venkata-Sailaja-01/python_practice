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

## 4️⃣ Two Integer Inputs

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
```

---

## 5️⃣ Multiple Inputs in One Line

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

### 4. How do you take multiple inputs in one line?

```python
a, b = map(int, input().split())
```

---

### 5. What is the difference between `input()` and `print()`?

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
- Use `map()` and `split()` to accept multiple values in one line.
- User input is essential for building interactive Python applications.

---

## 📂 Folder Structure

```
Day04/
│── userinput.py
│── README.md
```

---

### ⭐ Happy Coding! Keep Practicing Python Every Day.