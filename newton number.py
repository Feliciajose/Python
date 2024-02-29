def newtonsqrt(n):
    root=n/2
    for i in range(5):
        root=(root+n/root)/2
        print(root)
n=eval(input("enter number to find sqrt:"))
newtonsqrt(n)