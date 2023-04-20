# Question 

"""
Day 11 - Program to find the length of the string without using inbuilt function.
""" 

# Program

def len_string(string_ip):
    length = 0;
    for chr in string_ip:
        length = length + 1;
    return length;

string_ip = input("Enter the string to count the length: ")
op = len_string(string_ip)
print("The length of the sting is: ",op)
# Output

"""
Enter the string to count the length: Hello World
The length of the sting is:  11
"""
