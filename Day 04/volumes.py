#Question

"""
Program to find volume of sphere and cylinder.
"""

#Program

pi = 3.14

#To find volume of the sphere
radSpr = float(input("Enter the Radius of Sphere: "))
volSpr = (4/3)*pi*(radSpr**3)
print("\nVolume of the Sphere is: ", volSpr)

#To find volume of the cylinder
radCyl = float(input("\nEnter the Radius of Cylinder: "))
heightCyl = float(input("Enter the Height of Cylinder: "))
volCyl = pi*(radCyl**2)*heightCyl
print("\nVolume of the Cylinder is: ", volCyl)

#Output
"""
Enter the Radius of Sphere: 10.2
Volume of the Sphere is:  4442.92416

Enter the Radius of Cylinder: 30
Enter the Height of Cylinder: 12.5
Volume of the Cylinder is:  35325.0
"""
