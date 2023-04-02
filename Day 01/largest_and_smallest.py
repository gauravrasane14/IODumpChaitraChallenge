#Question

""" Day 01 - Program to find the largest and smallest of the given 5 numbers. """

#Program

n1 = int(input("Enter 1st Number: "))

n2 = int(input("Enter 2nd Number: "))

n3 = int(input("Enter 3rd Number: "))

n4 = int(input("Enter 4th Number: "))

n5 = int(input("Enter 5th Number: "))

#Largest Number out of 5

if n1>n2 and n1>n3 and n1>n4 and n1>n5 :

    print("Largest Number is ",n1)

elif n2>n1 and n2>n3 and n2>n4 and n2>n5 :

    print("Largest Number is ",n2)

elif n3>n1 and n3>n2 and n3>n4 and n3>n5 :

    print("Largest Number is ",n3)

elif n4>n1 and n4>n2 and n4>n3 and n4>n5 :

    print("Largest Number is ",n4)

elif n5>n1 and n5>n2 and n5>n3 and n5>n4 :

    print("Largest Number is ",n5)

else:

    print("Please Enter Valid Data")


#Smallest Number out of 5

if n1<n2 and n1<n3 and n1<n4 and n1<n5 :

    print("Smallest Number is", n1)

elif n2<n1 and n2<n3 and n2<n4 and n2<n5 :

    print("Smallest Number is ",n2)

elif n3<n1 and n3<n2 and n3<n4 and n3<n5 :

    print("Smallest Number is ",n3)

elif n4<n1 and n4<n2 and n4<n3 and n4<n5 :

    print("Smallest Number is ",n4)

elif n5<n1 and n5<n2 and n5<n3 and n5<n4 :

    print("Smallest Number is ",n5)

else:

    print("Please Enter Valid Data")    

    
#Output

"""

Enter 1st Number: 1

Enter 2nd Number: 2

Enter 3rd Number: 3

Enter 4th Number: 4

Enter 5th Number: 5


Largest Number is  5

Smallest Number is 1
"""
