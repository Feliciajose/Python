import math 
n=int(input("enter the no of terms"))
x=int(input("enter the value of x"))
sum=1
for i in range (2,n+1,2):
    sum=sum+(x**i)/math.factorial(i)
print("the sum of series is",round(sum,2))