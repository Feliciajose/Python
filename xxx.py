#3-A) Python Program to find the Sum of the Series: x + x^2/2 + x^3/3 +... x^n/n
n=int(input("Enter the number of terms:"))
x=int(input("Enter the value of x:"))
sum=0
for i in range(1,n+1):
    sum=sum+((x**i)/i)
    print("The sum of series is",round(sum,2))