````markdown
# 📘 Day 02 - Python Data Types

## 🎯 Objective

Learn about Python data types, how to declare variables, identify their types using the `type()` function, and understand their real-world applications.

---

# 📖 What are Data Types?

A **data type** defines the kind of value a variable can store. Python automatically detects the data type based on the value assigned to the variable.

Python provides **15 built-in data types**.

## 📋 Built-in Data Types

- Integer (`int`)
- Float (`float`)
- Boolean (`bool`)
- Complex (`complex`)
- String (`str`)
- List (`list`)
- Tuple (`tuple`)
- Dictionary (`dict`)
- Set (`set`)
- Frozenset (`frozenset`)
- Range (`range`)
- Bytes (`bytes`)
- Bytearray (`bytearray`)
- Memoryview (`memoryview`)
- NoneType (`None`)

---

# 📝 Declaring Variables

Assign values to variables and use the `type()` function to identify their data type.

```python
a = 10
b = 25.5
c = True
d = "Python"

print(type(a))
print(type(b))
print(type(c))
print(type(d))
```

### Output

```
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'str'>
```

---

# 🔧 Common Built-in Functions

Python provides many built-in functions for working with data.

| Function| Description                         |
|---------|-------------------------------------|
| `type()`| Returns the data type of a variable |
| `len()` | Returns the length of an object     |
| `sum()` | Returns the sum of values           | 
| `max()` | Returns the largest value           |
| `min()` | Returns the smallest value          |

---

# 🔢 Integer (`int`)

Integers are whole numbers without decimal points.

### Example

```python
age = 22
marks = 95

print(type(age))
```

---

# 🔹 Float (`float`)

Floats are numbers with decimal points.

### Example

```python
price = 199.99
temperature = 36.5
```

Python also supports **scientific notation**.

```python
a = 10e1
b = 10e2
c = 10e3

print(a)
print(b)
print(c)
```

### Output

```
100.0
1000.0
10000.0
```

### Explanation

- `10e1` = 10 × 10¹ = 100.0
- `10e2` = 10 × 10² = 1000.0
- `10e3` = 10 × 10³ = 10000.0

---

# 📝 String (`str`)

Strings are sequences of characters enclosed in **single quotes (`'`)** or **double quotes (`"`).**

### Correct Examples

```python
name = "Sailu"
city = 'Hyderabad'
```

### Highlighting Text

```python
sentence = "This is an 'Example'"
```

### Incorrect Example

```python
name = 'Sailu"
```

Python raises a **SyntaxError** because the quotation marks do not match.

---

# ✔️ Boolean (`bool`)

A Boolean value can have only two values.

- `True`
- `False`

### Example

```python
a = True
b = False

print(type(a))
```

---

# ❌ Falsy Values in Python

The following values are considered **False** when converted using `bool()`.

| Value            | Example      | `bool()` Result |
|------------------|--------------|:---------------:|
| Boolean False    | `False`      | False           |
| None             | `None`       | False           |
| Integer Zero     | `0`          | False           |
| Float Zero       | `0.0`        | False           |
| Complex Zero     | `0j`         | False           |
| Empty String     | `""` or `''` | False           |
| Empty List       | `[]`         | False           |
| Empty Tuple      | `()`         | False           |
| Empty Dictionary | `{}`         | False           |
| Empty Set        | `set()`      | False           |
| Empty Range      | `range(0)`   | False           |

> **Note:** Every value other than the above is considered **True**.

---

# 📄 Doc String

A **Doc String** is a multi-line string enclosed within triple quotes.

```python
"""
This is a Doc String.
It can span multiple lines.
It is used to provide documentation.
"""
```

### Why Use Doc Strings?

- Explain modules
- Describe classes
- Document functions
- Improve code readability
- Help other developers understand your code

---

# 🌍 Real-Time Examples

## Example 1: Student Information

```python
name = "Sailu"
age = 22
cgpa = 8.9
```

---

## Example 2: Bank Account

```python
account_balance = 25000.75
is_active = True
```

---

## Example 3: Shopping Cart

```python
items = ["Laptop", "Mouse", "Keyboard"]
```

---

## Example 4: Employee Details

```python
employee = {
    "Name": "Rahul",
    "Salary": 50000
}
```

---

## Example 5: Temperature Record

```python
temperature = 36.7
```

---

# ✅ Advantages

- Easy to learn and use.
- Automatically identifies data types.
- Supports many built-in data types.
- Makes coding faster.
- Improves code readability.
- Suitable for beginners and professionals.

---

# ❌ Disadvantages

- Dynamic typing can cause runtime errors.
- Uses more memory than statically typed languages.
- Slightly slower than compiled languages.
- Type-related bugs are detected during execution.

---

# 📝 Summary

- Python has **15 built-in data types**.
- Variables store different types of data.
- Use the `type()` function to identify a variable's data type.
- Strings are enclosed in single or double quotes.
- Floats support scientific notation using `e`.
- Boolean values are either `True` or `False`.
- Doc Strings are written using triple quotes.
- Choosing the correct data type improves code quality and performance.

---

# 📂 Folder Structure

```
Day02/
│── datatypes.py
│── README.md
```

---

# 💻 Happy Coding!

> **"The better you understand data types today, the easier it becomes to master Python tomorrow."** 🚀
````
