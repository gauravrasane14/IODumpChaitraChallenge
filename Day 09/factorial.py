# Question 

"""
Day 09 - Program to find factorial of given number.
""" 

# Program

#Method 1

n = int(input("Enter the number to find factorial: "))
f1 = 1
f2 = 1
for i in range(1,n+1):
    f1 = f1*i
print("Factorial of given number is: ",f1)

#Method 2

import math
f2 = math.factorial(n)
print("Factorial by inbuilt math function: ",f2)

# Output

"""
Enter the number to find factorial: 10
Factorial of given number is:  3628800
Factorial by inbuilt math function:  3628800
"""
