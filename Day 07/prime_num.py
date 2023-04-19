# Question 

"""
Day 07 - Program to check wheaher the input recived from user is prime or not.
""" 

# Program 
num = int(input("Enter the number to check prime or not: "))

if num>1:
    for i in range(2,num):
        if num % i == 0:
            print(num,"is not prime number.")
            break
    else:
        print(num,"is a prime number.")
else:
    print(num,"is not prime number.")
            
# Output

"""
Enter the number to check prime or not: 7
7 is a prime number.

Enter the number to check prime or not: 55
55 is not prime number.
"""
