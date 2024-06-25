#Task 1 : Area of rectangle
#Task 2: Area of Circle
#Task 3: Area of Triangle

'''
1. Define the rectangle, circle, and triangle area calculations as functions.
2. Create a function named square_perimeter that takes the side length of a square and returns its perimeter.
3. Write a function named circle_details that takes the radius of a circle as its only argument and prints out both the circumference and the area of the circle.
4. Write a function named geometry that takes the side length of a square and the radius of a circle. The function should print which shape has a larger perimeter/circumference and which shape has a larger area.
'''
import math


def rectangle (length, width):
    return length * width

def circle (radius):
    return math.pi * math.pow(radius, 2)

def triangle (base, height):
    return .5 * base * height

def square_perimeter(side):
    return side * 4

def circle_details(radius):
    circumference =  math.pi * (radius * 2)
    return circumference, circle(radius)

def geometry(length, radius):
    perim_square = square_perimeter(length)
    circum_circle = math.pi * (radius * 2)
    area_square = length ** 2
    area_circle = circle (radius)

    if (perim_square > circum_circle):
        print("The square has a greater perimiter")
    elif (perim_square < circum_circle):
        print("The cirlce has the greater circumference")
    else:
        print("They have the same perimiter and circumference")

    if (area_circle > area_square):
        print("The circle has a greater area")
    elif (area_square > area_circle):
        print("The square has a greater area")
    else:
        print("Both shapes have the same area")


print(circle_details)
print(geometry(5,3))
#print(f"The circle_detaile one prints out both {circle_details(3)}")
'''
x = int(input("What is the length of the rectangle? "))
y = int(input("What is the width of the rectangle? "))

area_rect = x * y

print(f"The area of the rectangle is: {area_rect}")

a = int(input("What is the radius of the circle? "))

area_cir = math.pi * math.pow(a,2)

print(f"The area of the circle is: {area_cir}")

d = int(input("What is the height of the triangle? "))
f = int(input("What is the base of the triangle? "))

area_tri = .5 * d * f

print(f"The area of the triangle is: {area_tri}")
'''