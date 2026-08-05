"""
====================================================
📘 Day 07 - Packages in Python
====================================================

Topics Covered
--------------
1. random Module
    • randint()
    • random()
    • choice()
    • shuffle()

2. math Module
    • pi
    • e
    • ceil()
    • pow()
    • sqrt()

3. time Module
    • sleep()
    • time()
    • ctime()

4. streamlit Package
    • st.title()
    • st.write()

====================================================
"""

# ==================================================
# Importing Packages
# ==================================================

import random
import math
import time

# Streamlit is optional.
# Uncomment the below line after installing Streamlit.
# import streamlit as st


# ==================================================
# RANDOM MODULE
# ==================================================

print("=" * 60)
print("RANDOM MODULE")
print("=" * 60)

# Example 1 : randint()

print("\nExample 1 : random.randint()")
num = random.randint(1, 10)
print("Random Integer :", num)


# Example 2 : random()

print("\nExample 2 : random.random()")
print("Random Decimal :", random.random())


# Example 3 : choice()

print("\nExample 3 : random.choice()")

items = ['a', 'b', 'c', 10, 20, 30]

print("Items :", items)

print("Random Choice :", random.choice(items))


# Example 4 : shuffle()

print("\nExample 4 : random.shuffle()")

numbers = [10,20,30,40,50]

print("Before Shuffle :", numbers)

random.shuffle(numbers)

print("After Shuffle  :", numbers)


# ==================================================
# MATH MODULE
# ==================================================

print("\n" + "=" * 60)
print("MATH MODULE")
print("=" * 60)


# Example 5 : pi

print("\nExample 5 : math.pi")

print("Value of PI :", math.pi)


# Example 6 : e

print("\nExample 6 : math.e")

print("Euler Number :", math.e)


# Example 7 : ceil()

print("\nExample 7 : math.ceil()")

print(math.ceil(5.1))
print(math.ceil(7.99))
print(math.ceil(15.0001))


# Example 8 : pow()

print("\nExample 8 : math.pow()")

print("5² =", math.pow(5,2))
print("2⁵ =", math.pow(2,5))
print("10³ =", math.pow(10,3))


# Example 9 : sqrt()

print("\nExample 9 : math.sqrt()")

print("Square Root of 25 :", math.sqrt(25))
print("Square Root of 81 :", math.sqrt(81))
print("Square Root of 625 :", math.sqrt(625))


# ==================================================
# TIME MODULE
# ==================================================

print("\n" + "=" * 60)
print("TIME MODULE")
print("=" * 60)


# Example 10 : sleep()

print("\nExample 10 : time.sleep()")

print("Program Started...")

time.sleep(2)

print("Program Continued After 2 Seconds")


# Example 11 : time()

print("\nExample 11 : time.time()")

current_time = time.time()

print("Current Timestamp :", current_time)


# Example 12 : ctime()

print("\nExample 12 : time.ctime()")

print("Current Date & Time :", time.ctime())


# ==================================================
# STREAMLIT PACKAGE
# ==================================================

print("\n" + "=" * 60)
print("STREAMLIT PACKAGE")
print("=" * 60)

print("""
Streamlit is a third-party package.

Install it using:

pip install streamlit

Import Statement:

import streamlit as st
""")


# Example 13

print("""
Example:

import streamlit as st

st.title("My First Streamlit App")
""")


# Example 14

print("""
import streamlit as st

st.write("Welcome to Streamlit")
""")


# Example 15

print("""
import streamlit as st

st.title("Student Information")

st.write("Name : Sailaja")

st.write("Course : Data Science")

st.write("Welcome to my first Streamlit Application.")
""")


# Run Command

print("""
Run Streamlit Application

streamlit run app.py
""")


# ==================================================
# END OF PROGRAM
# ==================================================

print("\n" + "=" * 60)
print("Day 07 - Packages Completed Successfully")
print("=" * 60)