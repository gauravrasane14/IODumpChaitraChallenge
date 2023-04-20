#Question
"""
Program to print sum of first n numbers.
"""

#Program

num = int(input("How many numbers do you want to print? Enter: "))
n = 1
sum=0

while (num>=n):
    sum = sum + n
    n = n + 1
    
print("The sum of first",num,"natural number is ",sum)

#Output
"""
How many numbers do you want to print? Enter: 10
The sum of first 10 natural number is  55
"""
