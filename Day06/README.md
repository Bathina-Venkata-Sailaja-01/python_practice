# 📘 Day 06 - `round()` Function, `end`, and `sep` in Python

## 🎯 Objective

Learn how to:

- Use the `round()` function to round numbers.
- Understand how the `round()` function works with decimal places.
- Round numbers to the nearest integer, tens, hundreds, and thousands.
- Identify common mistakes while using the `round()` function.
- Explore real-world applications of the `round()` function.

---

# 📖 What is `round()`?

The `round()` function is a built-in Python function used to round a number to the nearest integer or to a specified number of decimal places.

It is commonly used when displaying numbers in a clean and readable format, especially in financial calculations, reports, billing systems, and scientific applications.

---

# 📝 Syntax

```python
round(number, digits)
```

### Parameters

| Parameter | Description |
|------------|-------------|
| `number` | The number that needs to be rounded. |
| `digits` *(optional)* | The number of decimal places to round to. |

---

### Return Value

The `round()` function returns the rounded value.

---

# ⚙️ How `round()` Works

The `round()` function works based on the value of the second parameter (`digits`).

### Case 1: Without `digits`

Python rounds the number to the nearest integer.

```python
round(12.7)
```

Output

```
13
```

---

### Case 2: Positive `digits`

Python rounds the number to the specified number of decimal places.

```python
round(3.14159265, 2)
```

Output

```
3.14
```

---

### Case 3: Negative `digits`

Python rounds the number to tens, hundreds, thousands, etc.

```python
round(786, -2)
```

Output

```
800
```

---

# 📖 Example 1: Round to the Nearest Integer

```python
num = 12.7

print(round(num))
```

### Output

```
13
```

---

# 📖 Example 2: Round to Two Decimal Places

```python
pi = 3.14159265

print(round(pi, 2))
```

### Output

```
3.14
```

---

# 📖 Example 3: Round to Four Decimal Places

```python
pi = 3.14159265

print(round(pi, 4))
```

### Output

```
3.1416
```

---

# 📖 Example 4: Round to the Nearest Tens

```python
num = 786

print(round(num, -1))
```

### Output

```
790
```

---

# 📖 Example 5: Round to the Nearest Hundreds

```python
num = 786

print(round(num, -2))
```

### Output

```
800
```

---

# 📖 Example 6: Using User Input

```python
num = float(input("Enter a decimal number: "))

print("Rounded Value:", round(num, 2))
```

### Sample Output

```
Enter a decimal number: 15.6789

Rounded Value: 15.68
```

---

# 📊 Comparison of `round()` Examples

| Function Call | Output | Description |
|---------------|--------|-------------|
| `round(12.7)` | `13` | Nearest integer |
| `round(12.2)` | `12` | Nearest integer |
| `round(3.14159, 2)` | `3.14` | Two decimal places |
| `round(3.14159, 4)` | `3.1416` | Four decimal places |
| `round(786, -1)` | `790` | Nearest tens |
| `round(786, -2)` | `800` | Nearest hundreds |

---

# 📌 Notes

- `digits` is optional.
- If omitted, Python rounds to the nearest integer.
- Positive values round decimal places.
- Negative values round tens, hundreds, thousands, etc.
- `round()` does not permanently change the original value unless you assign it to a variable.

Example:

```python
num = 15.678

round(num, 2)

print(num)
```

Output

```
15.678
```

---

# ⚠️ Common Mistakes

## ❌ Forgetting the Parentheses

```python
round
```

This only refers to the function.

---

## ✅ Correct

```python
print(round(15.7))
```

Output

```
16
```

---

## ❌ Passing a String

```python
print(round("15.7"))
```

### Error

```
TypeError
```

---

## ✅ Correct

```python
print(round(float("15.7")))
```

Output

```
16
```

---

## ❌ Using Too Many Arguments

```python
round(10, 2, 3)
```

### Error

```
TypeError
```

---

## ✅ Correct

```python
round(10, 2)
```

---

# 🌍 Real-Time Applications

The `round()` function is widely used in:

- 💰 Banking applications for rounding currency values.
- 🧾 Billing and invoice systems.
- 📊 Data analysis and reporting.
- 📈 Percentage calculations.
- 🌦️ Weather applications for displaying temperatures.
- 🧪 Scientific calculations.
- 📉 Statistical analysis.
- 📱 Mobile applications.
- 🛒 E-commerce websites.
- 🎓 Student result management systems.

---

**Next Part:** `end` Parameter in `print()` 

# 📖 What is the `end` Parameter?

The `end` parameter is an optional parameter of the `print()` function that specifies **what should be printed after the output**.

By default, the `print()` function ends with a **new line**, which means the next `print()` statement starts on the next line.

The `end` parameter allows us to change this default behavior by printing a space, comma, arrow, tab, or any custom string after the output.

---

# 📝 Syntax

```python
print(object, end="value")
```

### Parameter

| Parameter | Description |
|-----------|-------------|
| `object` | The value or values to be printed. |
| `end` | Specifies what should be printed after the output. |

---

### Default Value

```python
print("Hello", end="\n")
```

The default value of `end` is:

```python
"\n"
```

which means **move the cursor to the next line** after printing.

---

# ⚙️ How the `end` Parameter Works

Normally, every `print()` statement automatically moves the cursor to the next line.

Example:

```python
print("Python")
print("Programming")
```

Output

```
Python
Programming
```

When you use the `end` parameter, Python prints the specified value instead of moving to the next line.

Example:

```python
print("Python", end=" ")
print("Programming")
```

Output

```
Python Programming
```

---

# 📖 Example 1: Default Behavior

```python
print("Python")
print("Programming")
```

### Output

```
Python
Programming
```

---

# 📖 Example 2: Using a Space

```python
print("Python", end=" ")
print("Programming")
```

### Output

```
Python Programming
```

---

# 📖 Example 3: Using an Arrow

```python
print("A", end=" -> ")
print("B", end=" -> ")
print("C")
```

### Output

```
A -> B -> C
```

---

# 📖 Example 4: Printing Numbers on One Line

```python
for i in range(1, 6):
    print(i, end=" ")
```

### Output

```
1 2 3 4 5
```

---

# 📖 Example 5: Using a Comma

```python
print("Apple", end=", ")
print("Banana", end=", ")
print("Mango")
```

### Output

```
Apple, Banana, Mango
```

---

# 📖 Example 6: Using a Pipe Symbol

```python
print("Python", end=" | ")
print("Java", end=" | ")
print("C++")
```

### Output

```
Python | Java | C++
```

---

# 📖 Example 7: Printing Without Any Separator

```python
print("Hello", end="")
print("World")
```

### Output

```
HelloWorld
```

---

# 📖 Example 8: Printing a Pattern

```python
for i in range(5):
    print("*", end=" ")
```

### Output

```
* * * * *
```

---

# 📊 Common Values of `end`

| `end` Value | Result |
|-------------|--------|
| `"\n"` | New line (Default) |
| `" "` | Space |
| `","` | Comma |
| `" | "` | Pipe symbol |
| `" -> "` | Arrow |
| `"\t"` | Tab space |
| `""` | No space or new line |

---

# 📊 Comparison of `print()` with and without `end`

| Without `end` | With `end=" "` |
|---------------|----------------|
| Output appears on different lines. | Output appears on the same line. |
| Uses the default new line. | Uses a custom ending. |
| Suitable for normal printing. | Suitable for formatted output. |

---

# ⚠️ Common Mistakes

## ❌ Forgetting Quotes

```python
print("Python", end= )
```

### Error

```
SyntaxError
```

---

## ✅ Correct

```python
print("Python", end=" ")
```

---

## ❌ Using the Wrong Parameter Name

```python
print("Python", End=" ")
```

### Error

```
TypeError
```

Python is **case-sensitive**.

---

## ✅ Correct

```python
print("Python", end=" ")
```

---

## ❌ Expecting a New Line

```python
print("Hello", end=" ")
print("World")
```

### Output

```
Hello World
```

If you use `end=" "`, Python **does not** move to the next line.

---

# 🌍 Real-Time Applications

The `end` parameter is commonly used in:

- 🖥️ Displaying menu items on the same line.
- 📊 Formatting reports.
- 📈 Printing tables.
- 🎮 Displaying game scores.
- ⏳ Showing loading or progress indicators.
- 🧾 Generating invoices.
- 📋 Printing lists in a single line.
- 📚 Displaying numbered sequences.
- 🛒 Billing applications.
- 🎓 Student result management systems.

---

> **Note:** The `end` parameter only controls **what is printed after the current output**. It does **not** change the values being printed.


# 📖 What is the `sep` Parameter?

The `sep` parameter is an optional parameter of the `print()` function that specifies **the separator between multiple values** passed to the `print()` function.

By default, Python separates multiple values with a **single space**.

The `sep` parameter allows us to replace the default space with any character or string such as a comma, hyphen, pipe symbol, colon, or arrow.

---

# 📝 Syntax

```python
print(object1, object2, object3, sep="separator")
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| `object1, object2...` | Values to be printed. |
| `sep` | Specifies the separator between multiple values. |

---

### Default Value

```python
print("Python", "Java", "C")
```

Python internally uses:

```python
sep=" "
```

### Output

```
Python Java C
```

---

# ⚙️ How the `sep` Parameter Works

Whenever multiple values are passed to the `print()` function, Python automatically inserts a **space** between them.

Using the `sep` parameter, we can replace that space with any separator.

Example:

```python
print("Python", "Java", "C", sep="-")
```

Output

```
Python-Java-C
```

---

# 📖 Example 1: Default Separator

```python
print("Python", "Java", "C")
```

### Output

```
Python Java C
```

---

# 📖 Example 2: Hyphen Separator

```python
print("Python", "Java", "C", sep="-")
```

### Output

```
Python-Java-C
```

---

# 📖 Example 3: Pipe Separator

```python
print("Python", "Java", "C", sep=" | ")
```

### Output

```
Python | Java | C
```

---

# 📖 Example 4: Colon Separator

```python
print("10", "30", "45", sep=":")
```

### Output

```
10:30:45
```

---

# 📖 Example 5: Comma Separator

```python
print("Apple", "Banana", "Mango", sep=", ")
```

### Output

```
Apple, Banana, Mango
```

---

# 📖 Example 6: Arrow Separator

```python
print("A", "B", "C", sep=" -> ")
```

### Output

```
A -> B -> C
```

---

# 📖 Example 7: Star Separator

```python
print(10, 20, 30, sep=" * ")
```

### Output

```
10 * 20 * 30
```

---

# 📖 Example 8: Using `sep` and `end` Together

```python
print("Python", "Java", "C", sep=" | ", end=" <-- Languages")
```

### Output

```
Python | Java | C <-- Languages
```

---

# 📊 Common Values of `sep`

| `sep` Value | Result |
|--------------|--------|
| `" "` | Space (Default) |
| `","` | Comma |
| `", "` | Comma with space |
| `"-"` | Hyphen |
| `" | "` | Pipe |
| `":"` | Colon |
| `" -> "` | Arrow |
| `" * "` | Star |

---

# 📊 Difference Between `end` and `sep`

| `end` | `sep` |
|--------|-------|
| Prints a value after the output. | Prints a value between multiple outputs. |
| Used once at the end of `print()`. | Used between every object in `print()`. |
| Default value is `"\n"`. | Default value is `" "`. |
| Controls line ending. | Controls separation of values. |

---

# ⚠️ Common Mistakes

## ❌ Using `sep` with a Single Value

```python
print("Python", sep="-")
```

### Output

```
Python
```

There is no separator because only one value is printed.

---

## ✅ Correct

```python
print("Python", "Java", sep="-")
```

### Output

```
Python-Java
```

---

## ❌ Wrong Parameter Name

```python
print("Python", "Java", Sep="-")
```

### Error

```
TypeError
```

Python is case-sensitive.

---

## ✅ Correct

```python
print("Python", "Java", sep="-")
```

---

## ❌ Forgetting Quotes

```python
print("A", "B", sep=-)
```

### Error

```
SyntaxError
```

---

## ✅ Correct

```python
print("A", "B", sep="-")
```

---

# 🌍 Real-Time Applications

The `sep` parameter is commonly used in:

- 🧾 Printing bills and invoices.
- 📊 Displaying tables.
- 📈 Formatting reports.
- 📅 Printing dates.
- ⏰ Displaying time.
- 📋 Printing CSV-style data.
- 🛒 E-commerce applications.
- 🎓 Student management systems.
- 🏦 Banking applications.
- 📱 Mobile applications.

---

# 💻 Practice Programs

### `round()` Function

1. Round `18.7654` to **2 decimal places**.
2. Round `945` to the nearest **tens**.
3. Round `945` to the nearest **hundreds**.
4. Accept a decimal number from the user and round it to **3 decimal places**.

---

### `end` Parameter

5. Print numbers from **1 to 20** on the same line.
6. Print your name and city on the same line.
7. Print the alphabets **A to E** separated by arrows.
8. Print five stars (`*`) in one line using a loop.

---

### `sep` Parameter

9. Print your name, age, and city separated by `" | "`.
10. Print the current time using a colon (`:`) separator.
11. Print fruits separated by commas.
12. Use both `sep` and `end` in a single `print()` statement.

---

# 🎤 Interview Questions

### 1. What is the purpose of the `round()` function?

**Answer:** It is used to round a number to the nearest integer or to a specified number of decimal places.

---

### 2. What is the default value of the `end` parameter?

**Answer:** `"\n"` (new line).

---

### 3. What is the default value of the `sep` parameter?

**Answer:** `" "` (single space).

---

### 4. What is the difference between `end` and `sep`?

**Answer:** `end` controls what is printed after the output, whereas `sep` controls what is printed between multiple values.

---

### 5. Can we use `end` and `sep` together?

**Answer:** Yes. Both parameters can be used in the same `print()` statement.

---

### 6. What happens if `digits` is omitted in `round()`?

**Answer:** The number is rounded to the nearest integer.

---

### 7. Can `round()` round numbers to hundreds or thousands?

**Answer:** Yes. Use negative values for the `digits` parameter.

Example:

```python
round(1256, -2)
```

---

### 8. Which parameter controls the separator between values?

**Answer:** `sep`

---

### 9. Which parameter controls the ending of the output?

**Answer:** `end`

---

### 10. Are `end` and `sep` parameters of the `print()` function?

**Answer:** Yes.

---

# 📚 Summary

- `round()` is used to round numbers to the nearest integer or a specified number of decimal places.
- Positive `digits` round decimal places, while negative `digits` round tens, hundreds, and thousands.
- The `end` parameter controls what is printed after the output.
- The default value of `end` is `"\n"`.
- The `sep` parameter controls the separator between multiple values.
- The default value of `sep` is a single space (`" "`).
- Both `end` and `sep` are optional parameters of the `print()` function.
- Using `round()`, `end`, and `sep` helps produce clean, readable, and professional output.

---

## 📂 Folder Structure

```text
Day06/
│── round_end_separator.py
│── README.md
```

---

# 💻 Happy Coding!

> **"Clean and well-formatted output makes your programs easier to read, understand, and maintain. Master `round()`, `end`, and `sep` to write professional Python programs!"** 🚀


