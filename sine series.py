import math
sine = 0
x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
for i in range(n):
    sign = (-1)**i
    pi=22/7
    y=x*(pi/180)
    sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
print(sine)