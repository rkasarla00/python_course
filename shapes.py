#Task 1 : Area of rectangle
#Task 2: Area of Circle
#Task 3: Area of Triangle
import math

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