#Question

"""

Q3 Program to find Area of Triangle, Rectangle and Square.

"""

#Program

#Area of Triangle

baseTri = float(input(" Enter the Base of triangle: "))

heightTri = float(input("Enter the Height of triangle: "))

areaTri = 0.5*baseTri*heightTri

print("\nArea of triangle is ", areaTri)

#Area of Rectangle

lengthRect = float(input("\nEnter the Length of rectangle: "))

breathRect = float(input("Enter the Breath of rectangle: "))

areaRect = lengthRect*breathRect

print("\nArea of Rectangle is ", areaRect)

#Area of Square

sideSq = float(input("\nEnter the Side of square: "))

areaSq = sideSq**2

print("\nArea of Square is ", areaSq)

#Output

"""

Enter the Base of triangle: 2

Enter the Height of triangle: 3

Area of triangle is  3.0

Enter the Length of rectangle: 5

Enter the Breath of rectangle: 4

Area of Rectangle is  20.0

Enter the Side of square: 4

Area of Square is  16.0

"""

