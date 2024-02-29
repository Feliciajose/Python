#6-C) Area of a shape
def fnSquare(s):
   return (s*s)
def fnRectangle(l,b):
    return (l*b)
def fnCircle(r):
    return 3.142*r*r
def fnTriangle(base,ht):
    return 0.5*base*ht
# square
s = int(input("Enter side of square : "))
l = int(input("Enter length of rectangle : "))
b = int(input("Enter the breadth of rectangle : "))
r = float(input("Enter circle radius : "))
base = int(input("Enter base of triangle : "))
ht = int(input("Enter height of triangle : "))

print("Area of square =",fnSquare(s))
print("Area of rectangle =",fnRectangle(l,b))
print("Area of circle =",fnCircle(r))
print("Area of triangle =",fnTriangle(base,ht))