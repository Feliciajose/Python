#fibonacii series
f1=-1
f2=1
print(f1,f2)
n=int(input("enter the value of n"))
for i in range (0,n+1):
    f=f1+f2
    print(f)
    f1=f2
    f2=f