# Question 

"""
Day 08 - Program to print multiplication table of number using for loop.
""" 

# Program 

n = int(input("Enter the number to print multiplication table: "))

print("The multiplication table of",n,"is:")
for i in range(1,11):
    t = i * n
    print(n,"×",i,"=",t)

# Output

"""
Enter the number to print multiplication table: 5
5 × 1 = 5
5 × 2 = 10
5 × 3 = 15
5 × 4 = 20
5 × 5 = 25
5 × 6 = 30
5 × 7 = 35
5 × 8 = 40
5 × 9 = 45
5 × 10 = 50
"""
