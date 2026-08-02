# 📘 Day 05 - Print Statement in Python

## 🎯 Objective

Learn how to display output in Python using the `print()` function and understand different ways to format output using commas, the `format()` method, and f-strings.

---

# 📖 What is `print()`?

The `print()` function is used to display output on the screen. It is one of the most commonly used functions in Python and is useful for displaying text, variables, calculations, and program results.

---

# 📝 Syntax

```python
print(object)
```

### Example

```python
print("Hello, World!")
```

### Output

```
Hello, World!
```

---

# ⚙️ How `print()` Works

1. Accepts one or more objects.
2. Converts them into strings (if necessary).
3. Displays them on the screen.
4. Moves the cursor to the next line after printing.

---

# 📖 Example 1: Printing a Calculated Result

```python
n1 = eval(input("Enter n1: "))
n2 = eval(input("Enter n2: "))
n3 = eval(input("Enter n3: "))

average = (n1 + n2 + n3) / 3

print(average)
```

### Output

```
Enter n1: 10
Enter n2: 20
Enter n3: 30
20.0
```

> **Note:** The above program calculates the **average** of three numbers. If you want the addition, remove `/3`.

---

# 📖 Example 2: Hardcoded Output

Suppose the client wants the output in the following format:

```
The addition of 10,20,30 is: 60
```

A beginner might write:

```python
print("The addition of 10,20,30 is: 60")
```

### Problem

This is called **hardcoding**.

No matter what values the user enters, the output will always remain the same.

---

# 📖 Example 3: Printing Variable Names

```python
print("The addition of n1, n2, n3 is: add")
```

### Output

```
The addition of n1, n2, n3 is: add
```

### Problem

Everything inside quotation marks is treated as a **string**, so Python prints the text exactly as written.

---

# 📖 Example 4: Printing Variables Using Commas

```python
n1 = eval(input("Enter n1: "))
n2 = eval(input("Enter n2: "))
n3 = eval(input("Enter n3: "))

add = n1 + n2 + n3

print("The addition of", n1, ",", n2, ",", n3, "is:", add)
```

### Output

```
Enter n1: 10
Enter n2: 20
Enter n3: 30

The addition of 10, 20, 30 is: 60
```

### Limitation

This method works well when there are only a few variables.

However, when a program contains many variables, the `print()` statement becomes longer and harder to read. It is also easier to make mistakes, such as forgetting a comma, a space, or a variable.

For this reason, Python provides better string formatting methods such as the **`format()` method** and **f-strings**, which make the code cleaner and easier to maintain.
---

# 📖 Example 5: Using the `format()` Method

The `format()` method allows us to insert variable values into a string using placeholders `{}`.

```python
n1 = eval(input("Enter n1: "))
n2 = eval(input("Enter n2: "))
n3 = eval(input("Enter n3: "))

add = n1 + n2 + n3

print("The addition of {}, {}, {} is: {}".format(n1, n2, n3, add))
```

### Output

```
Enter n1: 10
Enter n2: 20
Enter n3: 30

The addition of 10, 20, 30 is: 60
```

---

# 📖 Example 6: Using f-Strings

An **f-string** is the modern and recommended way to format strings.

```python
n1 = eval(input("Enter n1: "))
n2 = eval(input("Enter n2: "))
n3 = eval(input("Enter n3: "))

add = n1 + n2 + n3

print(f"The addition of {n1}, {n2}, and {n3} is: {add}")
```

### Output

```
Enter n1: 10
Enter n2: 20
Enter n3: 30

The addition of 10, 20, and 30 is: 60
```

---

# 📊 Comparison of Printing Methods

| Method           | Example              | Recommended |
|------------------|----------------------|-------------|
| Simple `print()` | `print(add)`         | ✅ Yes     |
| Using commas     | `print("Sum =", add)`| ✅ Yes     |
| Using `format()` | `"{}".format(value)` | ✅ Yes     |
| Using f-strings  | `f"{value}"`         | ⭐ Best    |

---

# 📌 Difference Between `format()` and f-Strings

| `format()`                              | f-String                             |
|-----------------------------------------|--------------------------------------|
| Uses `{}` placeholders with `.format()` | Uses `{}` directly inside the string |
| Slightly longer syntax                  | Shorter and easier to read           |
| Introduced in Python 2.6                | Introduced in Python 3.6             |
| Still supported                         | Recommended in modern Python         |

---

# ⚠️ Common Mistakes

## ❌ Printing Variables Inside Quotes

```python
print("n1")
```

### Output

```
n1
```

Python prints the text instead of the value.

---

## ✅ Correct

```python
print(n1)
```

### Output

```
10
```

---

## ❌ Hardcoding Values

```python
print("The addition of 10,20,30 is: 60")
```

This always prints the same output.

---

## ✅ Correct

```python
print(f"The addition of {n1}, {n2}, and {n3} is: {add}")
```

---

# 🌍 Real-Time Applications

The `print()` function is commonly used for:

- 🖥️ Displaying program output
- 🧪 Debugging programs
- 📊 Showing calculation results
- 📝 Displaying reports
- 📋 Printing menus
- 🎮 Displaying game scores
- 🧾 Billing applications
- 🏦 Banking applications
- 🎓 Student management systems
- 🛒 Online shopping applications

---

# 💻 Practice Programs

1. Print your name.
2. Print your age.
3. Print the sum of two numbers.
4. Print the product of two numbers.
5. Print the average of three numbers.
6. Display a student's details.
7. Print today's date.
8. Use commas to print variables.
9. Use `format()` to print variables.
10. Use an f-string to print variables.
11. Compare `format()` and f-strings.
12. Design a formatted output for a bill.

---

# 🎤 Interview Questions

### 1. Which function is used to display output in Python?

**Answer:** `print()`

---

### 2. What is the purpose of the `print()` function?

**Answer:** It displays output on the screen.

---

### 3. What are the different ways to print variables?

**Answer:**

- Using commas
- Using the `format()` method
- Using f-strings

---

### 4. Which formatting method is recommended in modern Python?

**Answer:** **f-Strings**

---

### 5. Why are f-strings preferred?

**Answer:** They are shorter, easier to read, and provide better readability.

---

### 6. What is hardcoding?

**Answer:** Writing fixed values directly in the program instead of using variables.

---

# 📚 Summary

- `print()` is used to display output.
- Strings are enclosed in quotation marks.
- Variables should not be placed inside quotes.
- Avoid hardcoding values.
- Use commas, `format()`, or f-strings for formatted output.
- f-Strings are the most readable and widely used formatting method in modern Python.

---

## 📂 Folder Structure

```
Day05/
│── print_statement.py
│── README.md
```

---

# 💻 Happy Coding!

> **"A well-formatted output makes your programs easier to read, understand, and debug."** 🚀