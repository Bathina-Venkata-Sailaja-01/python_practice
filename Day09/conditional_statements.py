# =========================================================
# DAY 08 - CONDITIONAL STATEMENTS
# =========================================================

# 1. Check whether a number is positive
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")


# 2. Check whether a number is positive or negative
num = int(input("Enter a number: "))

if num >= 0:
    print("Positive number")
else:
    print("Negative number")


# 3. Check whether a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 4. Check whether a person is eligible to vote
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 5. Find the greater of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
else:
    print("Second number is greater")


# 6. Find the greatest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("A is greatest")
elif b >= a and b >= c:
    print("B is greatest")
else:
    print("C is greatest")


# 7. Check pass or fail
marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 8. Grade calculation
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


# 9. Check whether a number is divisible by 5
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


# 10. Simple ATM
balance = float(input("Enter balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= balance:
    balance = balance - withdrawal
    print("Withdrawal successful")
    print("Remaining balance:", balance)
else:
    print("Insufficient balance")


# 11. Check temperature
temperature = float(input("Enter temperature: "))

if temperature >= 35:
    print("Very hot")
elif temperature >= 25:
    print("Warm")
elif temperature >= 15:
    print("Cool")
else:
    print("Cold")


# 12. Check username and password
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")


# 13. Check whether a year is a leap year
year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# 14. Check voting category
age = int(input("Enter your age: "))

if age < 18:
    print("Not eligible to vote")
elif age >= 60:
    print("Senior citizen voter")
else:
    print("Eligible voter")


# 15. Electricity bill calculation
units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
else:
    bill = units * 5

print("Electricity bill:", bill)