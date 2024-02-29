#selection sorting 
a=[6,5,4,1,2]
print("un sorted list",a)
n=len(a)
for i in range (0,n-1):
    mini=i
    for j in range (i+1,n):
        if (a[mini]>a[j]):
            mini=j
    a[mini],a[i]=a[i],a[mini]
print("sorted list",a)