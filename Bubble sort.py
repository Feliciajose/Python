#bubble sort 
a=[3,5,7,2,4]
print("unsorted list",a)
n=len(a)
for i in range (0,n-1):
    for j in range (0,n-i-1):
        if(a[j]>a[j+1]):
           a[j],a[j+1]=a[j+1],a[j]
print("sorted list:",a)