# 🐍 Conditional Statements in Python

## 🎯 Objective

Learn how to use **conditional statements** in Python to make decisions based on conditions.

---

## 📖 What are Conditional Statements?

Conditional statements are used to execute different blocks of code depending on whether a condition is **True** or **False**.

### Real-Life Example

Suppose you want to withdraw money from an ATM:

* If balance is sufficient → Allow withdrawal
* Otherwise → Show "Insufficient balance"

Python can make this decision using conditional statements.

---

# 📌 Types of Conditional Statements

Python mainly provides:

1. `if`
2. `if-else`
3. `if-elif-else`
4. Nested `if`

---

# 1️⃣ `if` Statement

The `if` statement executes a block of code only when the condition is `True`.

### Syntax

```python
if condition:
    statement
```

### Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote")
```

### Output

```text
You are eligible to vote
```

---

# 2️⃣ `if-else` Statement

The `else` block executes when the `if` condition is `False`.

### Syntax

```python
if condition:
    statement
else:
    statement
```

### Example

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

### Output

```text
Not eligible to vote
```

---

# 3️⃣ `if-elif-else` Statement

The `elif` statement is used when we have **multiple conditions**.

### Syntax

```python
if condition1:
    statement
elif condition2:
    statement
elif condition3:
    statement
else:
    statement
```

### Example

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

### Output

```text
Grade B
```

---

# 4️⃣ Nested `if` Statement

An `if` statement inside another `if` statement is called a **nested if**.

### Example

```python
age = 25
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Not eligible because age is below 18")
```

### Output

```text
Eligible to vote
```

---

# 🔢 Comparison Operators

Conditional statements commonly use comparison operators.

| Operator | Meaning                  | Example  |
| -------- | ------------------------ | -------- |
| `==`     | Equal to                 | `a == b` |
| `!=`     | Not equal to             | `a != b` |
| `>`      | Greater than             | `a > b`  |
| `<`      | Less than                | `a < b`  |
| `>=`     | Greater than or equal to | `a >= b` |
| `<=`     | Less than or equal to    | `a <= b` |

### Example

```python
a = 10
b = 20

print(a == b)
print(a < b)
print(a != b)
```

Output:

```text
False
True
True
```

---

# 🔗 Logical Operators

Logical operators are used to combine multiple conditions.

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | Both conditions must be True        |
| `or`     | At least one condition must be True |
| `not`    | Reverses the result                 |

### `and`

```python
age = 25
salary = 50000

if age >= 18 and salary >= 30000:
    print("Eligible")
```

### `or`

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

### `not`

```python
is_raining = False

if not is_raining:
    print("You can go outside")
```

---

# 🎯 Conditional Statement with User Input

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
```

---

# 🧮 Real-Life Example: Even or Odd

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

# 💰 Real-Life Example: Shopping Discount

```python
amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final Amount:", final_amount)
```

---

# 📊 Real-Life Example: Student Grade

```python
marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")
```

---

# ⚠️ Important Points

### 1. Indentation is mandatory

Correct:

```python
if age >= 18:
    print("Eligible")
```

Incorrect:

```python
if age >= 18:
print("Eligible")
```

### 2. Use `:` after the condition

```python
if age >= 18:
```

### 3. Conditions produce Boolean values

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

---

# ❌ Common Mistakes

### Mistake 1: Using `=` instead of `==`

Incorrect:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

`=` → Assignment
`==` → Comparison

---

### Mistake 2: Forgetting indentation

Incorrect:

```python
if age >= 18:
print("Eligible")
```

Correct:

```python
if age >= 18:
    print("Eligible")
```

---

### Mistake 3: Forgetting `:`

Incorrect:

```python
if age >= 18
```

Correct:

```python
if age >= 18:
```

---

# 🌍 Real-World Applications

Conditional statements are used in:

* 🏧 ATM systems
* 🛒 E-commerce websites
* 🎓 Student grading systems
* 💳 Banking applications
* 🚗 Traffic signal systems
* 🔐 Login systems
* 🎟️ Ticket booking
* 💰 Salary and tax calculations
* 📊 Data analysis
* 🤖 Machine learning decision logic

---

# 💻 Practice Programs

Practice these programs:

1. Check whether a number is positive or negative.
2. Check whether a number is even or odd.
3. Find the greatest of two numbers.
4. Find the greatest of three numbers.
5. Check whether a person is eligible to vote.
6. Check whether a year is a leap year.
7. Calculate student grade based on marks.
8. Check whether a number is divisible by 5.
9. Check whether a person is eligible for a driving license.
10. Calculate electricity bill based on units.
11. Calculate discount based on shopping amount.
12. Check whether a character is a vowel or consonant.
13. Check whether a number is positive, negative, or zero.
14. Create a simple calculator using `if-elif-else`.
15. Check username and password using conditional statements.

---

# 🎤 Interview Questions

### Basic

1. What is a conditional statement?
2. What is the purpose of an `if` statement?
3. What is the difference between `if` and `if-else`?
4. What is the purpose of `elif`?
5. What is nested `if`?
6. What is indentation in Python?
7. What is the difference between `=` and `==`?
8. What are comparison operators?
9. What are logical operators?
10. Can we use multiple `elif` statements?

### Interview Example

**Question:** What happens if multiple `elif` conditions are True?

**Answer:** Python executes the **first condition that evaluates to True** and skips the remaining `elif` and `else` blocks.

Example:

```python
marks = 95

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
```

Output:

```text
Grade A
```

---

# 📌 Summary

Conditional statements allow Python programs to **make decisions**.

```text
if
 ↓
condition
 ↓
True → execute block
False → check elif/else
```

The main conditional structures are:

```text
if
if-else
if-elif-else
nested if
```

They are fundamental for writing programs that respond differently to different situations.

---

# 📂 Suggested Folder Structure

```text

Day-08-conditional_statements/
│
├── README.md
├── conditional_statements.py
```

---

## 🚀 Happy Coding!

Keep practicing conditional statements with real-life problems. Once you are comfortable with `if`, `elif`, and `else`.