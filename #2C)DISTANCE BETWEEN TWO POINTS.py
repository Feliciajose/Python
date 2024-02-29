#2C)DISTANCE BETWEEN TWO POINTS
import math
print("Enter coordinates for Point 1 : ")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
print("Enter coordinates for point 2 : ")
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
dist = math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) )
print("Distance between given points is", round(dist,2))