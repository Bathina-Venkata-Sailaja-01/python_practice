# 🐍 Day 07 - Types of Errors in Python

## 📘 Title

**Types of Errors in Python**

---

# 🎯 Objective

After completing this topic, you will be able to:

* Understand what an error is.
* Learn the different types of errors in Python.
* Identify syntax, runtime, and logical errors.
* Debug Python programs efficiently.
* Write error-free Python code.

---

# 📖 Introduction

An **error** is a problem in a program that prevents it from running correctly or producing the expected output.

Python reports errors with helpful messages that indicate:

* The line where the error occurred.
* The type of error.
* A brief description of the problem.

Learning to read these messages is one of the most important programming skills.

---

# 📚 Types of Errors in Python

Python errors are mainly classified into three types:

1. **Syntax Errors**
2. **Runtime Errors (Exceptions)**
3. **Logical Errors**

---

# 1️⃣ Syntax Errors

## 📖 What is a Syntax Error?

A **Syntax Error** occurs when the rules (syntax) of Python are violated.

The program cannot even start because Python cannot understand the code.

---

## 📝 Example 1

```python
print("Hello"
```

### ❌ Output

```
SyntaxError: '(' was never closed
```

---

## 📝 Example 2

```python
if 10 > 5
    print("True")
```

### ❌ Output

```
SyntaxError: expected ':'
```

---

## 📝 Example 3

```python
for i in range(5)
    print(i)
```

### ❌ Output

```
SyntaxError: expected ':'
```

---

## 📝 Example 4

```python
print("Hello')
```

### ❌ Output

```
SyntaxError: unterminated string literal
```

---

## 📝 Example 5

```python
x = 10
 if x > 5:
    print(x)
```

### ❌ Output

```
IndentationError: unexpected indent
```

---

## 📌 Common Causes

* Missing colon (`:`)
* Missing brackets
* Wrong indentation
* Incorrect quotes
* Misspelled keywords

---

# 2️⃣ Runtime Errors (Exceptions)

## 📖 What is a Runtime Error?

A runtime error occurs **after the program starts executing**.

The syntax is correct, but something unexpected happens while running the program.

---

## 📝 Example 1 – ZeroDivisionError

```python
a = 10
b = 0
print(a / b)
```

### ❌ Output

```
ZeroDivisionError
```

---

## 📝 Example 2 – NameError

```python
print(age)
```

### ❌ Output

```
NameError
```

---

## 📝 Example 3 – TypeError

```python
print(10 + "20")
```

### ❌ Output

```
TypeError
```

---

## 📝 Example 4 – ValueError

```python
num = int("Hello")
```

### ❌ Output

```
ValueError
```

---

## 📝 Example 5 – IndexError

```python
numbers = [10,20,30]
print(numbers[5])
```

### ❌ Output

```
IndexError
```

---

## 📝 Example 6 – KeyError

```python
student = {"name":"Rahul"}

print(student["age"])
```

### ❌ Output

```
KeyError
```

---

## 📝 Example 7 – FileNotFoundError

```python
file = open("demo.txt")
```

### ❌ Output

```
FileNotFoundError
```

---

## 📝 Example 8 – AttributeError

```python
num = 10
num.append(5)
```

### ❌ Output

```
AttributeError
```

---

# 📌 Common Runtime Errors

* ZeroDivisionError
* NameError
* TypeError
* ValueError
* IndexError
* KeyError
* AttributeError
* FileNotFoundError
* ImportError
* ModuleNotFoundError

---

# 3️⃣ Logical Errors

## 📖 What is a Logical Error?

A logical error is the hardest error to identify.

The program:

* Runs successfully ✅
* Produces no error message ✅
* Gives the wrong output ❌

---

## 📝 Example 1

```python
length = 10
breadth = 5

area = 2 * (length + breadth)

print(area)
```

### ❌ Output

```
30
```

### ✅ Correct Output

```
50
```

Reason:

Area formula should be

```python
length * breadth
```

---

## 📝 Example 2

```python
marks = [50,60,70]

average = sum(marks)

print(average)
```

### ❌ Output

```
180
```

### ✅ Correct Output

```
60
```

Correct code

```python
average = sum(marks)/len(marks)
```

---

## 📝 Example 3

```python
age = 16

if age >= 21:
    print("Eligible to Vote")
else:
    print("Not Eligible")
```

The program runs correctly, but the voting age condition is incorrect for many countries.

---

# ⚙️ How to Debug Errors

## Step 1

Read the error message carefully.

---

## Step 2

Find the line number mentioned.

---

## Step 3

Identify the error type.

---

## Step 4

Correct the mistake.

---

## Step 5

Run the program again.

---

# 📊 Comparison Table

| Feature           | Syntax Error | Runtime Error | Logical Error |
| ----------------- | ------------ | ------------- | ------------- |
| Program Starts    | ❌ No         | ✅ Yes         | ✅ Yes         |
| Error Message     | ✅ Yes        | ✅ Yes         | ❌ No          |
| Program Stops     | ✅ Yes        | ✅ Usually     | ❌ No          |
| Wrong Output      | ❌            | Sometimes     | ✅ Always      |
| Difficult to Find | Easy         | Medium        | Hard          |

---

# 📌 Notes

* Every syntax error must be fixed before execution.
* Runtime errors occur while the program is running.
* Logical errors require testing and careful debugging.
* Reading traceback messages helps locate errors quickly.
* Use meaningful variable names to reduce mistakes.

---

# ⚠️ Common Mistakes

* Forgetting a colon (`:`)
* Incorrect indentation
* Using undefined variables
* Dividing by zero
* Mixing incompatible data types
* Accessing invalid list indexes
* Using wrong dictionary keys
* Writing incorrect formulas

---

# 🌍 Real-Time Applications

* Debugging software applications
* Web development
* Data Science projects
* Machine Learning models
* Automation scripts
* Game development
* Banking software
* Healthcare systems

---

# 💻 Practice Programs

1. Create a Syntax Error intentionally and fix it.
2. Write a program that produces a ZeroDivisionError.
3. Create a NameError and resolve it.
4. Demonstrate a TypeError using different data types.
5. Generate an IndexError using a list.
6. Produce a KeyError with a dictionary.
7. Write a program containing a logical error and correct it.
8. Identify and fix three errors in a given Python program.
9. Compare Syntax Error and Runtime Error with examples.
10. Write a program that handles a runtime error using `try` and `except`.

---

# 🎤 Interview Questions

### 1. What is an error in Python?

### 2. What are the three main types of errors?

### 3. What is the difference between Syntax Error and Runtime Error?

### 4. What is a Logical Error?

### 5. Which error is the hardest to detect?

### 6. What is an Exception?

### 7. Give examples of Runtime Errors.

### 8. What is a ZeroDivisionError?

### 9. What is the purpose of debugging?

### 10. How can you handle runtime errors in Python?

---

# 📚 Summary

* Errors are problems in a program that affect execution or output.
* Python has three major error categories:

  * Syntax Errors
  * Runtime Errors (Exceptions)
  * Logical Errors
* Syntax errors prevent execution.
* Runtime errors occur during execution.
* Logical errors produce incorrect results without displaying an error.
* Understanding error messages and debugging techniques helps you write reliable Python programs.

---

# 📂 Folder Structure

```
Day-07-Types-of-Errors/
│
├── README.md
├── errors_examples.py
└── images/
```

---

# 💻 Happy Coding!

> "Every error is an opportunity to learn. The best programmers become experts by fixing thousands of bugs."
