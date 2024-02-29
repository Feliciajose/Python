#6-A) Functions - factorial of a number using recursion
def fact(n):
    if(n==0):
      return 1
    else:
      return(n*fact(n-1))
n=int(input("Enter Number : "))
f=fact(n)
print("Factorial of",n,"is",f)