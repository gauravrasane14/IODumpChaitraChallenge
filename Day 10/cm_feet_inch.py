# Question 

"""
Day 10 - Accept the height of the person in cm and convet in into the feet and inches.
""" 

# Program

htCM = float(input("Enter height in Centimeter: "))
htFT = 0.0328084 * htCM
htIN = 0.393701 * htCM

print("Height in Feets: ",htFT,"Feet")
print("Height in Inches: ",htFT,"Inch")

# Output

"""
Enter height in Centimeter: 162
Height in Feets:  5.314960800000001 Feet
Height in Inches:  5.314960800000001 Inch
"""
