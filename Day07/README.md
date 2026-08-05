# 📘 Day 07 - Packages in Python

## 🎯 Objective

By the end of this lesson, you will be able to:

* Understand what Packages and Modules are.
* Learn why Python provides packages.
* Import built-in and third-party packages.
* Use commonly used functions from the `random` module.
* Understand how Python imports packages.
* Write cleaner, shorter, and reusable Python programs.

---

# 📖 What are Packages?

A **Package** is a collection of related modules that are organized in a directory.

Packages help programmers organize code in a structured manner. Instead of keeping everything inside a single Python file, we divide the code into multiple modules and group similar modules into a package.

Python provides many built-in packages, and we can also install thousands of third-party packages.

Some popular packages are:

* `random`
* `math`
* `time`
* `os`
* `datetime`
* `numpy`
* `pandas`
* `matplotlib`
* `streamlit`

Packages make programming easier because we don't need to write every function ourselves.

---

## 📦 What is a Module?

A **Module** is a single Python file (`.py`) that contains variables, functions, and classes.

Whenever we write a Python file and save it with the `.py` extension, it becomes a module.

Python also provides many built-in modules.

Example:

```python
import math
```

Here,

* `math` is a module.
* Inside the `math` module there are many useful functions like `sqrt()`, `pow()`, `ceil()`, etc.

Another example:

```python
import random
```

Here,

* `random` is a module.
* It contains functions to generate random numbers and random selections.

---

# 📚 Difference between Module and Package

| Module                                   | Package                                    |
| ---------------------------------------- | ------------------------------------------ |
| A single Python file.                    | A collection of related modules.           |
| Has a `.py` extension.                   | Contains multiple modules inside a folder. |
| Stores functions, variables and classes. | Organizes multiple modules together.       |
| Smaller unit of code.                    | Larger collection of modules.              |
| Example: `math.py`                       | Example: `numpy`, `pandas`                 |

### Example Structure

```text
Package
│
├── module1.py
├── module2.py
├── module3.py
└── __init__.py
```

---

# ❓ Why Do We Use Packages?

Imagine you want to calculate the square root of a number.

Without the `math` module, you would have to write the square root logic yourself.

Similarly,

* Generating random numbers
* Working with dates and time
* Creating graphs
* Building web applications

would all require writing hundreds of lines of code.

Python packages solve this problem by providing ready-made functions.

### Advantages of Packages

✅ Saves time

✅ Reduces coding effort

✅ Reusable code

✅ Easy to understand

✅ Easy to maintain

✅ Well-tested functions

✅ Improves productivity

---

# 📝 Syntax

## Import Entire Module

```python
import module_name
```

Example

```python
import math
```

---

## Import Multiple Modules

```python
import math
import random
import time
```

---

## Import Multiple Modules in One Line

```python
import math, random, time
```

---

## Import Specific Function

```python
from math import sqrt
```

Now you can directly write

```python
print(sqrt(25))
```

instead of

```python
print(math.sqrt(25))
```

---

## Import All Functions

```python
from math import *
```

Now every function inside the module becomes directly accessible.

Example

```python
print(pi)
print(sqrt(81))
```

---

## Import with Alias

```python
import streamlit as st
```

Here,

* `streamlit` is the package.
* `st` is an alias (short name).

Instead of writing

```python
streamlit.title()
```

we simply write

```python
st.title()
```

---

# ⚙️ How Import Works

Whenever Python sees an `import` statement, it follows these steps:

### Step 1

Searches for the requested module.

↓

### Step 2

Loads the module into memory.

↓

### Step 3

Executes the module only once.

↓

### Step 4

Makes all functions, variables, and classes available.

↓

### Step 5

We access them using **dot (`.`) notation**.

Example

```python
import math

print(math.sqrt(64))
```

Output

```text
8.0
```

---

# 📖 `random` Module

The **random** module is a built-in Python module used to generate random numbers and randomly select items.

It is commonly used in:

* Games
* OTP Generation
* Password Generation
* Lottery Systems
* AI Simulations
* Machine Learning
* Data Science

Import Statement

```python
import random
```

---

# 🔹 random.randint()

## Definition

Returns a random integer between the given start and end values (both inclusive).

### Syntax

```python
random.randint(start, end)
```

### Parameters

| Parameter | Description     |
| --------- | --------------- |
| start     | Starting number |
| end       | Ending number   |

### Example

```python
import random

print(random.randint(1,10))
```

Possible Output

```text
7
```

Another Possible Output

```text
2
```

Since the value is random, the output changes every time.

---

# 🔹 random.random()

## Definition

Returns a random floating-point number between **0.0** and **1.0**.

### Syntax

```python
random.random()
```

### Example

```python
import random

print(random.random())
```

Possible Output

```text
0.672548
```

Another Possible Output

```text
0.128963
```

Every execution produces a different decimal number.

---

# 🔹 random.choice()

## Definition

Returns one random element from a sequence such as a list, tuple, or string.

### Syntax

```python
random.choice(sequence)
```

### Example

```python
import random

items = ['a', 'b', 'c', 10, 20, 30]

print(random.choice(items))
```

Possible Output

```text
20
```

Another Possible Output

```text
b
```

Each execution randomly selects one item from the list.

---

# 🔹 random.shuffle()

## Definition

Randomly rearranges the elements of a list.

Unlike `choice()`, it does not return a new list. Instead, it modifies the original list.

### Syntax

```python
random.shuffle(list_name)
```

### Example

```python
import random

items = ['a', 'b', 'c', 10, 20, 30]

random.shuffle(items)

print(items)
```

Possible Output

```text
['b', 20, 'a', 30, 'c', 10]
```

Another Possible Output

```text
[30, 'c', 10, 'a', 'b', 20]
```

Every time you run the program, the order of the list changes.

---

## 📌 Summary of `random` Module

| Function              | Purpose                                  | Return Type              |
| --------------------- | ---------------------------------------- | ------------------------ |
| `randint(start, end)` | Returns a random integer                 | Integer                  |
| `random()`            | Returns a random decimal between 0 and 1 | Float                    |
| `choice(sequence)`    | Returns one random element               | Any Data Type            |
| `shuffle(list)`       | Randomly rearranges a list               | None (modifies the list) |

---

## 💡 Real-Time Uses of `random`

* OTP Generation
* Password Generator
* Dice Games
* Card Games
* Lottery Systems
* Quiz Applications
* Random Question Generator
* Machine Learning
* AI Simulations
* Data Sampling

---

# 📖 `math` Module

The **math** module is a built-in Python module that provides mathematical constants and functions.

It is widely used in:

* Mathematics
* Engineering
* Data Science
* Machine Learning
* Artificial Intelligence
* Scientific Calculations
* Statistics

Import Statement

```python
import math
```

---

# 🔹 `math.pi`

## Definition

`math.pi` returns the mathematical constant **π (Pi)**.

The value of π is approximately **3.141592653589793**.

It is commonly used to calculate the area and circumference of circles.

### Syntax

```python
math.pi
```

### Example

```python
import math

print(math.pi)
```

### Output

```text
3.141592653589793
```

### Example 2: Area of Circle

```python
import math

radius = 7

area = math.pi * radius ** 2

print("Area =", area)
```

### Output

```text
Area = 153.93804002589985
```

---

# 🔹 `math.e`

## Definition

`math.e` returns **Euler's Number**.

Its approximate value is **2.718281828459045**.

It is widely used in exponential calculations, Machine Learning, Statistics, and Data Science.

### Syntax

```python
math.e
```

### Example

```python
import math

print(math.e)
```

### Output

```text
2.718281828459045
```

---

# 🔹 `math.ceil()`

## Definition

The `ceil()` function rounds a decimal number **upwards** to the nearest integer.

Even if the decimal value is very small, the number is increased to the next integer.

### Syntax

```python
math.ceil(number)
```

### Parameter

| Parameter | Description                          |
| --------- | ------------------------------------ |
| number    | Any integer or floating-point number |

### Example 1

```python
import math

print(math.ceil(8.2))
```

### Output

```text
9
```

---

### Example 2

```python
import math

print(math.ceil(12.99))
```

### Output

```text
13
```

---

# 🔹 `math.pow()`

## Definition

The `pow()` function raises one number to the power of another.

### Syntax

```python
math.pow(base, exponent)
```

### Parameters

| Parameter | Description |
| --------- | ----------- |
| base      | Base number |
| exponent  | Power value |

### Example

```python
import math

print(math.pow(5,2))
```

### Output

```text
25.0
```

---

### Example 2

```python
import math

print(math.pow(2,5))
```

### Output

```text
32.0
```

---

# 🔹 `math.sqrt()`

## Definition

The `sqrt()` function returns the square root of a given number.

### Syntax

```python
math.sqrt(number)
```

### Example

```python
import math

print(math.sqrt(81))
```

### Output

```text
9.0
```

---

### Example 2

```python
import math

print(math.sqrt(625))
```

### Output

```text
25.0
```

---

# 📌 Summary of `math` Module

| Function      | Purpose                    | Returns |
| ------------- | -------------------------- | ------- |
| `math.pi`     | Value of π                 | Float   |
| `math.e`      | Euler's Number             | Float   |
| `math.ceil()` | Rounds upward              | Integer |
| `math.pow()`  | Raises a number to a power | Float   |
| `math.sqrt()` | Square root                | Float   |

---

# 💡 Real-Time Uses of `math`

* Area of Circle
* Engineering Calculations
* Banking Applications
* Scientific Research
* Machine Learning
* Data Science
* Artificial Intelligence
* Statistical Analysis
* Physics Calculations
* Financial Applications

---

# 📖 `time` Module

The **time** module provides functions for working with time and delays.

It is commonly used for:

* Timers
* Stopwatches
* Delays
* Measuring Program Execution Time
* Automation

Import Statement

```python
import time
```

---

# 🔹 `time.sleep()`

## Definition

Pauses the execution of the program for the specified number of seconds.

### Syntax

```python
time.sleep(seconds)
```

### Example

```python
import time

print("Start")

time.sleep(3)

print("End")
```

### Output

```text
Start
(wait for 3 seconds)
End
```

---

# 🔹 `time.time()`

## Definition

Returns the current time in seconds since **January 1, 1970 (Unix Epoch).**

### Syntax

```python
time.time()
```

### Example

```python
import time

print(time.time())
```

### Possible Output

```text
1754386125.3789
```

The value changes every second.

---

# 🔹 `time.ctime()`

## Definition

Converts the current system time into a human-readable date and time.

### Syntax

```python
time.ctime()
```

### Example

```python
import time

print(time.ctime())
```

### Possible Output

```text
Wed Aug 05 18:30:15 2026
```

The displayed date and time depend on your system clock.

---

# 📌 Summary of `time` Module

| Function  | Purpose                 |
| --------- | ----------------------- |
| `sleep()` | Pause program execution |
| `time()`  | Current timestamp       |
| `ctime()` | Current date and time   |

---

# 💡 Real-Time Uses of `time`

* Countdown Timers
* Stopwatch Applications
* Delay Between API Calls
* Performance Measurement
* Automation Scripts
* Games
* Scheduling Programs
* Loading Animations

---

# 📖 `streamlit` Package

`streamlit` is a **third-party Python package** used to build beautiful web applications using only Python.

It is especially popular among:

* Data Scientists
* Machine Learning Engineers
* AI Developers
* Python Developers

Unlike the previous modules, Streamlit must be installed separately.

---

## Installation

```bash
pip install streamlit
```

---

## Import Statement

```python
import streamlit as st
```

Here,

* `streamlit` is the package.
* `st` is an alias.

---

# 🔹 `st.title()`

## Definition

Displays a large heading on the web page.

### Syntax

```python
st.title("Your Title")
```

### Example

```python
import streamlit as st

st.title("My First Streamlit App")
```

### Output

A large heading is displayed on the web page.

---

# 🔹 `st.write()`

## Definition

Displays text, numbers, lists, tables, variables, and many other Python objects.

### Syntax

```python
st.write(data)
```

### Example

```python
import streamlit as st

st.write("Welcome to Streamlit!")
```

### Output

```text
Welcome to Streamlit!
```

---

## Complete Example

```python
import streamlit as st

st.title("Student Information")

st.write("Name : Sailaja")

st.write("Course : Data Science")

st.write("Welcome to my first Streamlit Application.")
```

Run the application

```bash
streamlit run app.py
```

---

# 📌 Summary of `streamlit`

| Function     | Purpose               |
| ------------ | --------------------- |
| `st.title()` | Displays a page title |
| `st.write()` | Displays any data     |

---

# 💡 Real-Time Uses of `streamlit`

* Machine Learning Projects
* Data Science Dashboards
* AI Applications
* Data Visualization
* Portfolio Projects
* Business Reports
* Interactive Forms
* Analytics Dashboards

---

# 📊 Comparison Tables

## 📌 Comparison of Python Packages

| Package     | Purpose                            | Commonly Used Functions                          |
| ----------- | ---------------------------------- | ------------------------------------------------ |
| `random`    | Generate random values             | `randint()`, `random()`, `choice()`, `shuffle()` |
| `math`      | Perform mathematical calculations  | `pi`, `e`, `ceil()`, `pow()`, `sqrt()`           |
| `time`      | Work with time and delays          | `sleep()`, `time()`, `ctime()`                   |
| `streamlit` | Build interactive web applications | `st.title()`, `st.write()`                       |

---

## 📌 Comparison of `random` Module Functions

| Function              | Description                                     | Return Type   |
| --------------------- | ----------------------------------------------- | ------------- |
| `randint(start, end)` | Returns a random integer between two numbers    | Integer       |
| `random()`            | Returns a random decimal number between 0 and 1 | Float         |
| `choice(sequence)`    | Returns a random element from a sequence        | Any Data Type |
| `shuffle(list)`       | Rearranges the elements of a list randomly      | None          |

---

## 📌 Comparison of `math` Module Functions

| Function      | Description                   | Return Type |
| ------------- | ----------------------------- | ----------- |
| `math.pi`     | Returns the value of π        | Float       |
| `math.e`      | Returns Euler's Number        | Float       |
| `math.ceil()` | Rounds a number upward        | Integer     |
| `math.pow()`  | Returns the power of a number | Float       |
| `math.sqrt()` | Returns the square root       | Float       |

---

## 📌 Comparison of `time` Module Functions

| Function  | Description                       |
| --------- | --------------------------------- |
| `sleep()` | Pauses program execution          |
| `time()`  | Returns the current timestamp     |
| `ctime()` | Returns the current date and time |

---

## 📌 Comparison of `streamlit` Functions

| Function     | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| `st.title()` | Displays a large heading                                     |
| `st.write()` | Displays text, numbers, lists, tables and many other objects |

---

# 📌 Notes

* A **Module** is a single Python file (`.py`).
* A **Package** is a collection of related modules.
* Python provides many built-in modules such as `math`, `random`, and `time`.
* Third-party packages like `streamlit` must be installed using `pip`.
* Import only the modules or functions you need.
* Using packages reduces coding effort and increases productivity.
* Packages make programs cleaner, reusable, and easier to maintain.
* The `random` module is useful whenever unpredictable values are required.
* The `math` module provides accurate mathematical functions and constants.
* The `time` module helps create delays and work with system time.
* `streamlit` allows Python developers to build web applications without HTML, CSS, or JavaScript.

---

# ⚠️ Common Mistakes

## ❌ Forgetting to Import the Module

```python
print(math.sqrt(25))
```

### Error

```text
NameError: name 'math' is not defined
```

### ✅ Correct

```python
import math

print(math.sqrt(25))
```

---

## ❌ Incorrect Module Name

```python
import Maths
```

### Error

```text
ModuleNotFoundError
```

### ✅ Correct

```python
import math
```

---

## ❌ Forgetting Parentheses

```python
import random

print(random.random)
```

### Output

Displays the function object instead of generating a random number.

### ✅ Correct

```python
print(random.random())
```

---

## ❌ Using `shuffle()` with a String

```python
random.shuffle("Python")
```

### Error

```text
TypeError
```

### ✅ Correct

```python
items = ['P','y','t','h','o','n']

random.shuffle(items)

print(items)
```

---

## ❌ Forgetting to Install Streamlit

```python
import streamlit
```

### Error

```text
ModuleNotFoundError
```

### ✅ Correct

```bash
pip install streamlit
```

---

# 🌍 Real-Time Applications

## 🎲 `random` Module

* OTP Generation
* Password Generator
* Online Games
* Lottery Systems
* Dice Simulation
* Card Games
* Random Quiz Generator

---

## 📐 `math` Module

* Area and Perimeter Calculations
* Engineering Applications
* Scientific Research
* Machine Learning
* Artificial Intelligence
* Data Science
* Financial Calculations

---

## ⏰ `time` Module

* Stopwatch Applications
* Countdown Timers
* Automation Scripts
* Delay Between API Requests
* Performance Measurement
* Loading Screens
* Scheduling Tasks

---

## 🌐 `streamlit` Package

* Data Science Dashboards
* Machine Learning Projects
* AI Applications
* Business Analytics
* Data Visualization
* Portfolio Projects
* Interactive Reports

---

# 💻 Practice Programs

### Beginner Level

1. Generate a random number between **1 and 100**.
2. Generate a random decimal number.
3. Select a random fruit from a list.
4. Shuffle a list of names.
5. Print the value of `math.pi`.
6. Print Euler's Number.
7. Find the square root of **625**.
8. Calculate **8²** using `math.pow()`.
9. Round **18.2** upward using `ceil()`.
10. Print the current system time.

---

### Intermediate Level

11. Create a Dice Simulator.
12. Create a Lucky Draw Program.
13. Generate a Random Password.
14. Build a Random Quiz Question Generator.
15. Measure the execution time of a program.
16. Display the current date and time.
17. Build a simple Streamlit application with a title and welcome message.
18. Create a Streamlit page showing your personal information.
19. Calculate the area of a circle using `math.pi`.
20. Generate ten random numbers and store them in a list.

---

# 🎤 Interview Questions

### Basic Questions

1. What is a Package?
2. What is a Module?
3. What is the difference between a Package and a Module?
4. Why do we use Packages in Python?
5. How do you import a module?
6. How do you import multiple modules?
7. What is an alias in Python?

---

### `random` Module

8. What does `random.randint()` do?
9. What is the difference between `random()` and `randint()`?
10. What is `random.choice()` used for?
11. What is `random.shuffle()` used for?
12. Does `shuffle()` return a new list?

---

### `math` Module

13. What is the value of `math.pi`?
14. What is Euler's Number?
15. What does `math.ceil()` do?
16. What is `math.sqrt()`?
17. What is `math.pow()`?

---

### `time` Module

18. What is the purpose of `time.sleep()`?
19. What does `time.time()` return?
20. What does `time.ctime()` return?

---

### `streamlit`

21. What is Streamlit?
22. Why do Data Scientists use Streamlit?
23. How do you install Streamlit?
24. What is `st.title()`?
25. What is `st.write()`?

---

# 📚 Summary

* Python provides built-in and third-party packages to simplify programming.
* A **Module** is a single Python file that contains reusable code.
* A **Package** is a collection of related modules.
* The `random` module is used to generate random values and perform random selections.
* The `math` module provides mathematical constants and functions.
* The `time` module helps work with timestamps, delays, and current system time.
* `streamlit` is a powerful third-party package used to build interactive web applications using Python.
* Using packages improves code reusability, readability, and development speed.

---

# 📂 Folder Structure

```text
Day07_Packages/
│
├── README.md
├── packages.py
```

---

# 💻 Happy Coding!

> **"Packages are one of Python's greatest strengths. Instead of writing everything from scratch, learn to use the right package at the right time. Mastering Python packages will help you write cleaner, faster, and more professional programs."** 🚀

**Keep Learning • Keep Practicing • Keep Building!** ❤️
