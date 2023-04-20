# Question 

"""
Day 12 - Program to reverse the digits of given number.
""" 

# Program


num_ip = int(input("Enter the number to reverse: "))

rvd_num = 0

while num_ip != 0:
    digit = num_ip % 10
    rvd_num = rvd_num * 10 + digit
    num_ip //= 10

print("Reversed number is: ",rvd_num)
# Output

"""
Enter the number to reverse: 4456123
Reversed number is:  3216544
"""
