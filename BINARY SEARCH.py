#BINARY SEARCH
a=[20,30,40,50,60]
print(a)
no=int(input("enter the value of no to search"))
start=0
stop=len(a)-1
while(start<=stop):
    mid=(start+stop)//2
    if(no==a[mid]):
        print("no found at the ps:",mid+1)
        break
    elif(no<a[mid]):
        stop=mid-1
    else:
        start=mid+1
else:
    ("no not found")