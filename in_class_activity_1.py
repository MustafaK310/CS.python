# -*- coding: utf-8 -*-
"""In_Class_Activity_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/zugurbil/CSC101/blob/main/In_Class_Activity_1.ipynb

##Instructions for In Class Activity 1

You must find all errors in your scripts. But because you are communicating with a machine, not a person, you have to be exact: the computer cannot understand you at all if there are errors, bugs, in your code. Or the computer may do exactly what you wrote, but not what you meant to do.

Add a comment to the file that describes what you did.

Change the file name to "your name In Class Activity 1" and hand in these corrected Python scripts!

Question 1
"""

x = 15
y = 5
z = 3
# I changed the second y value to a number that is not 0 because you can not divide by 0 when finding another variable.
y = 3
k = x / y
print(k)

"""Question 2"""

x = 10
y = 20
z = 30
# There was an indent for "print(x, y, z)" which caused an error, so I just back spaced so it wasn't indented.
print(x, y, z)

"""Question 3"""

# This program converts miles to km

miles = 10
multiplier = 1.609344
# multiplie was spelled wrong but I corrected it so the program would run correctly.
km = miles * multiplier
print(km)

"""Question 4"""

x = 1
y = 10
z = 2
t = 15
# A parenthesis was forgotten in the print section of the program that stopped the prodcut from calculating.
print((x * t) / (y / z))
print('Done')

"""Question 5"""

fruit = "kiwi"
# Fruit was spelled wrong but was corrected from 'frut'.
print(fruit, fruit, fruit)