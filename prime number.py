no=int(input("enter the no"))
count=1
n=2
while(count<=no):
    for i in range(2,n):
        if(n%i==0):
            break
        else:
            print(n)
            count=count+1
n=n+1