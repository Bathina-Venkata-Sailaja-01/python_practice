## Type cast
- Changing one data type to another data type
- how to convert integer to float and int to string and int to bool vice versa

## Boolean TypeCasting
Examples:
- bool(100)    # True
- bool(-5)     # True
- bool(0.1)    # True
- bool(0)      # False

**Python treats these values as False:**

- 0
- 0.0
- 0j
- None
- Empty strings ""
- Empty lists []
- Empty tuples ()
- Empty dictionaries {}
- Empty sets set()


# Python Type Casting Functions

Python provides several built-in functions to convert one data type into another. This process is called **Type Casting**.

| Function    | Converts To | Example              | Output            |
|-------------|-------------|----------------------|-------------------|
| `int()`     | Integer     | `int("10")`          | `10`              |
| `float()`   | Float       | `float("10")`        | `10.0`            |
| `str()`     | String      | `str(100)`           | `"100"`           |
| `bool()`    | Boolean     | `bool(1)`            | `True`            |


# Real-Time Examples of Type Casting

In Python, **type casting** is used whenever we need to convert one data type into another. It is commonly used because the data entered by the user using `input()` is always stored as a **string**. To perform mathematical operations or comparisons, we must convert it to the appropriate data type.

---

## 1. ATM Withdrawal System 🏧

### Scenario
A customer enters the amount they want to withdraw from their bank account.

### Why Type Casting?
The withdrawal amount entered by the user is a **string**. To compare it with the account balance (an integer), it must be converted using `int()`.

### Code

```python
balance = 5000

withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")
```

### Input

```
Enter withdrawal amount: 2500
```

### Output

```
Withdrawal Successful
```

---

## 2. Online Shopping Cart 🛒

### Scenario
A customer purchases multiple items from an online store.

### Why Type Casting?
The quantity entered by the customer is a string. To calculate the total price, it must be converted into an integer.

### Code

```python
price = 250

quantity = int(input("Enter quantity: "))

total = price * quantity

print("Total Bill =", total)
```

### Input

```
Enter quantity: 4
```

### Output

```
Total Bill = 1000
```

---

## 3. Student Percentage Calculator 🎓

### Scenario
A student enters marks obtained in different subjects.

### Why Type Casting?
Marks can contain decimal values like **89.5**, so they should be converted into **float** values.

### Code

```python
math = float(input("Math Marks: "))
science = float(input("Science Marks: "))
english = float(input("English Marks: "))

percentage = (math + science + english) / 3

print("Percentage =", percentage)
```

### Input

```
Math Marks: 90
Science Marks: 85.5
English Marks: 92
```

### Output

```
Percentage = 89.17
```

---

## 4. Employee Salary Calculator 💼

### Scenario
An employee enters their monthly salary to calculate a bonus.

### Why Type Casting?
Salary may include decimal values, so it is converted into a float.

### Code

```python
salary = float(input("Enter Salary: "))

bonus = salary * 0.10

print("Bonus =", bonus)
```

### Input

```
Enter Salary: 45000.50
```

### Output

```
Bonus = 4500.05
```

---

## 5. Banking Interest Calculator 🏦

### Scenario
A bank calculates simple interest based on the principal amount, interest rate, and number of years.

### Why Type Casting?
- Principal and rate can contain decimal values (`float`).
- Time is usually a whole number (`int`).

### Code

```python
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Interest Rate: "))
time = int(input("Enter Time (Years): "))

interest = (principal * rate * time) / 100

print("Simple Interest =", interest)
```

### Input

```
Principal: 10000
Rate: 7.5
Years: 2
```

### Output

```
Simple Interest = 1500.0
```

---

## 6. OTP Login Verification 🔐

### Scenario
A user enters an OTP to log in.

### Why Type Casting?
The OTP entered by the user is a string. It must be converted into an integer before comparing it with the original OTP.

### Code

```python
otp = int(input("Enter OTP: "))

if otp == 4567:
    print("Login Successful")
else:
    print("Invalid OTP")
```

### Input

```
Enter OTP: 4567
```

### Output

```
Login Successful
```

---

## 7. Discount Calculator 🏷️

### Scenario
A shopping website gives a 20% discount on the total bill.

### Why Type Casting?
The bill amount may contain decimal values, so it is converted into a float.

### Code

```python
bill = float(input("Enter Bill Amount: "))

discount = bill * 0.20
final_bill = bill - discount

print("Discount =", discount)
print("Final Bill =", final_bill)
```

### Input

```
Enter Bill Amount: 2500
```

### Output

```
Discount = 500.0
Final Bill = 2000.0
```

---

## 8. Mobile Recharge System 📱

### Scenario
A user enters the recharge amount for their mobile number.

### Why Type Casting?
The recharge amount is converted into an integer to perform calculations like GST.

### Code

```python
recharge = int(input("Enter Recharge Amount: "))

gst = recharge * 0.18

print("GST =", gst)
```

### Input

```
Enter Recharge Amount: 299
```

### Output

```
GST = 53.82
```

---

## 9. Display Roll Number 📄

### Scenario
A school management system displays a student's roll number along with text.

### Why Type Casting?
The roll number is an integer, but string concatenation requires both values to be strings.

### Code

```python
roll = 101

print("Roll Number: " + str(roll))
```

### Output

```
Roll Number: 101
```

Without `str()`:

```python
print("Roll Number: " + roll)
```

Output:

```
TypeError: can only concatenate str (not "int") to str
```

---

## 10. Login Form Validation ✅

### Scenario
A website checks whether the user entered a password.

### Why Type Casting?
`bool()` converts an empty string into `False` and a non-empty string into `True`.

### Code

```python
password = input("Enter Password: ")

print(bool(password))
```

### Input

```
Python123
```

### Output

```
True
```

### Input

```

```

(User presses **Enter** without typing anything.)

### Output

```
False
```

---

# Summary

| Real-Time Application | Type Casting Used  | Purpose                                 |
|-----------------------|--------------------|-----------------------------------------|
| ATM Withdrawal        | `int()`            | Compare withdrawal amount with balance  |
| Online Shopping       | `int()`            | Calculate total bill                    |
| Student Percentage    | `float()`          | Calculate percentage with decimal marks |
| Salary Calculator     | `float()`          | Calculate employee bonus                |
| Banking Interest      | `float()`, `int()` | Calculate simple interest               |
| OTP Verification      | `int()`            | Verify login OTP                        |
| Discount Calculator   | `float()`          | Calculate discount amount               |
| Mobile Recharge       | `int()`            | Calculate GST                           |
| Display Roll Number   | `str()`            | Combine text and numbers                |
| Login Validation      | `bool()`           | Check whether the password is empty     |

---

## Key Takeaways

- **`int()`** is used for whole numbers such as age, quantity, OTP, and years.
- **`float()`** is used for decimal values such as salary, marks, price, and interest rate.
- **`str()`** is used to combine numbers with text.
- **`bool()`** is used to check whether a value is empty or not.
- Since **`input()` always returns a string**, type casting is essential before performing calculations or comparisons.
